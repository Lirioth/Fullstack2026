# 🌍 Daily Challenge – Climate Monitoring Concept

## 🚧 Current Status

This directory does **not** include an implemented climate-monitoring system. The outline below documents the original challenge idea for future reference.

---

## 🧠 Challenge Overview

Design a modular climate-monitoring pipeline capable of ingesting historical CSV data and live weather APIs, validating and transforming records, persisting the cleaned dataset, and raising alerts for extreme events.

---

## 🗂️ Suggested Structure

```text
DailyChallenge/
├── data/
│   ├── historical_weather.csv        # Placeholder – create when you start building the solution 🌦️
│   └── processed_weather.json        # Placeholder output file
├── alerts/
│   └── alerts_log.txt                # Placeholder log file
├── src/
│   ├── ingest.py                     # Placeholder module entrypoints
│   ├── processor.py
│   ├── storage.py
│   ├── alert_system.py
│   └── report.py
├── main.py                           # Placeholder orchestrator
└── README.md
```

Create the files when you are ready to implement the pipeline.

---

## ✅ Success Criteria (When Implemented)

- Combine at least one historical CSV dataset with live API data.
- Validate and normalize fields (dates, units, missing values).
- Persist cleaned data and alert logs to disk.
- Generate readable daily or weekly reports.
- Handle API and I/O errors gracefully with clear logging.

---

## 📝 Next Steps

1. Gather sample weather data and choose a public API (e.g., OpenWeatherMap).
2. Define the schema for processed records and alerts.
3. Implement modules iteratively, starting with ingestion and validation.
4. Add unit tests and documentation as functionality grows.

This README will be updated once a working implementation is added. 🌤️
