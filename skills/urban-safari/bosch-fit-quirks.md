# Bosch eBike Flow — FIT format quirks

Reference for agents analyzing raw exports. Source: [Processing Bosch eBike Flow FIT Files (2023)](https://hacdias.com/2023/10/11/processing-bosch-ebike-flow-fit-files/) and [2025 update](https://hacdias.com/2025/12/13/processing-bosch-ebike-flow-fit-files/).

XOSS G and most Garmin exports do **not** split records per timestamp — the merge logic in
`fit_io.py` is harmless on clean FITs.

## Duplicate records per timestamp

FitCSVTool CSV shows **two `Data` rows** for the same `timestamp`:

```
Definition,0,record,timestamp,1,,position_lat,1,,position_long,1,,...
Data,0,record,timestamp,"1061488539",s,position_lat,...,position_long,...

Definition,0,record,timestamp,1,,altitude,1,,cadence,1,,distance,1,,speed,1,,power,1,,...
Data,0,record,timestamp,"1061488539",s,altitude,"17.2",m,cadence,"65",rpm,distance,"2214.0",m,speed,"5.303",m/s,power,"82",watts,...
```

Importers expect **one** record with lat, lon, alt, cadence, distance, speed, power together.

## Missing messages (Bosch raw export)

| Message | In raw Bosch FIT? | Impact |
|---------|-------------------|--------|
| `record` | Yes (often split) | Track + metrics |
| `lap` | Often one lap only | Calorie distribution wrong |
| `session` | Partial | Summary stats incomplete |
| `activity` | **No** | Garmin Connect rejects file |
| `event` (pause/stop) | **No** | Pauses show as 0 speed |

## Tools

- **Fix Bosch FIT:** [flowfit](https://github.com/hacdias/flowfit) (browser)
- **Inspect:** `python scripts/inspect_fit.py ride.fit`
- **Python read:** `fitparse`
