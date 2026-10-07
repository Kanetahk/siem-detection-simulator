# SIEM Detection Simulator

**Bottom line:** generates synthetic, clearly-labeled log events matching
the shape of specific attack techniques, used to validate Splunk
detection logic (SPL searches, correlation rules) before pointing them
at real telemetry. No real attack, network connection, or system call is
performed by any script here.

*Read this in: [Português](./locales/pt-BR/README.md)*

## Why this exists

Building a detection search against real attack traffic means either
running something genuinely risky, or waiting for the real thing to
happen on its own. This repo writes log lines in the exact format a real
event would produce, so a detection's logic, field extraction,
correlation, threshold, can be tested and iterated on quickly,
independent of whether a live attack scenario is running.

Detections validated this way should still be confirmed against real
telemetry before being trusted, see
[splunk-alert-response-pipeline](https://github.com/Kanetahk/splunk-alert-response-pipeline)
and [soc-lab](https://github.com/Kanetahk/soc-lab) for where that happens.

## Project structure
```
siem-detection-simulator/
├── .venv/
├── locales/
│   └── pt-br/
│       └── README.md
├── src/
│   ├── gui/
│   │   └── __init__.py
│   └── generator/
│       ├── __init__.py
│       └── beaconing/
│           ├── __init__.py
│           └── beaconing.py
├── tests/
│   └── tkinter
│       └── test-app.py
│
├── .gitignore
├── app.py
└── README.md
```

## Generators

| Script | Simulates | MITRE ATT&CK |
|---|---|---|
| `generators/beaconing.py` | C2 beaconing: regular-interval outbound connection | T1071 (Command and Control) |

## Usage

```bash
python generators/beaconing.py
```

Each generator writes its own log file, next to the script, in the
format documented in its own header comment.

## Related projects

- [soc-lab](https://github.com/Kanetahk/soc-lab) - Splunk detection engineering, consumes these logs
- [splunk-alert-response-pipeline](https://github.com/Kanetahk/splunk-alert-response-pipeline) - the automation pipeline these detections feed into.