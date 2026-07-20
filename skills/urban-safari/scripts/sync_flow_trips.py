#!/usr/bin/env python3
"""Pull new Bosch eBike Flow .fit files from a USB-connected iPhone.

Usage:
  pip install pymobiledevice3
  python sync_flow_trips.py --dest ./rides
  python sync_flow_trips.py --dry-run
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

FLOW_BUNDLE_ID = "com.bosch.ebike.flow"


async def sync(dest: Path, dry_run: bool) -> int:
    try:
        from pymobiledevice3.lockdown import create_using_usbmux
        from pymobiledevice3.services.house_arrest import DOCUMENTS_ROOT, HouseArrestService
    except ImportError:
        print("Install pymobiledevice3: pip install pymobiledevice3", file=sys.stderr)
        return 1

    dest.mkdir(parents=True, exist_ok=True)
    lockdown = await create_using_usbmux()

    pulled = 0
    skipped = 0

    async with await HouseArrestService.create(
        lockdown, FLOW_BUNDLE_ID, documents_only=True
    ) as service:
        names = await service.listdir(DOCUMENTS_ROOT)
        fit_names = sorted(n for n in names if n.lower().endswith(".fit"))

        if not fit_names:
            print("No .fit files in Flow Documents.")
            return 0

        for name in fit_names:
            remote = f"{DOCUMENTS_ROOT}/{name}"
            local = dest / name

            if local.exists() and local.stat().st_size > 0:
                skipped += 1
                continue

            if dry_run:
                print(f"would pull: {name}")
                pulled += 1
                continue

            print(f"pulling: {name}")
            await service.pull(remote, str(local))
            pulled += 1

    print(f"Done — pulled {pulled}, skipped {skipped} (already present) → {dest}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Flow FIT files from iPhone USB")
    parser.add_argument("--dest", type=Path, default=Path("rides"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return asyncio.run(sync(args.dest.resolve(), args.dry_run))


if __name__ == "__main__":
    raise SystemExit(main())
