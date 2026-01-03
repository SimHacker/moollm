# Basic Skill Template

> *Minimal starter template for creating new MOOLLM skills.*

Copy this directory to create a new skill.

---

## Contents

| File | Purpose |
|------|---------|
| [SKILL.md](./SKILL.md) | Protocol documentation |
| [PROTOTYPE.yml](./PROTOTYPE.yml) | Machine-readable definition |
| [template/](./template/) | Files copied on instantiation |

---

## Usage

```bash
cp -r skills/templates/basic-skill skills/my-new-skill
```

Then:
1. Edit `SKILL.md` with your protocol
2. Edit `PROTOTYPE.yml` with name, tier, tools
3. Edit `template/` files for instance creation
4. **Add README.md** (like this one, but for your skill)
5. Register in [INDEX.yml](../INDEX.yml)

---

## Dovetails With

- [skill-instantiation-protocol.md](../../skill-instantiation-protocol.md) — How skills are born
- [play-learn-lift/](../../play-learn-lift/) — LIFT stage creates new skills
- [PROTOCOLS.yml](../../../PROTOCOLS.yml) — Symbol index

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [templates/](../) |
| ⬆️⬆️ Skills | [skills/](../../) |
| 🏠 Root | [MOOLLM](../../../) |
