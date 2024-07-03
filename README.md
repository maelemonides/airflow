# Airflow DAG: Process Real Estate CSV Files

## Overview

This Airflow DAG (`process_real_estate_csv`) automates the processing of real estate CSV files. It reads CSV files from a designated directory, calculates the average price, stores the result, and moves the processed files to another directory. The DAG is scheduled to run every minute.

## Components

### DAG Definition

- **DAG ID**: process_real_estate_csv
- **Description**: Process real estate CSV files every minute.
- **Schedule Interval**: * * * * * (executes every minute)

### Tasks

- **process_files**: PythonOperator task that executes the `process_files` function defined in `myairflow.py`.

## Directory Structure

Ensure your directory structure is set up as follows for the DAG to function correctly:

```
booster/
├── dags/
│   └── process_real_estate_csv.py  <- Airflow DAG definition
├── scripts/
│   └── myairflow.py      <- Script to process CSV files
└── data/
    ├── toProcess/        <- Place CSV files here for processing
    ├── result/           <- Processed results will be saved here
    └── already_processed/ <- Processed CSV files will be moved here
```

## Usage

1. **Place CSV Files**: Put CSV files containing real estate data into `booster/data/toProcess/`.
   
2. **Start Airflow Scheduler**: Ensure your Airflow scheduler is running to execute the DAG periodically.

3. **Monitor Execution**: Use the Airflow UI or CLI to monitor the execution of the `process_real_estate_csv` DAG. You should see tasks being executed every minute as per the schedule.

4. **Result Files**: Processed CSV files with average price calculations will be saved in `booster/data/result/`. The original files will be moved to `booster/data/already_processed/`.

## Notes

- **Dependencies**: Ensure `pandas` is installed in your Airflow environment to run the processing script (`myairflow.py`).
- **Adjustments**: Modify paths or scheduling intervals in `process_real_estate_csv.py` as needed for your specific requirements.
- **Logging**: Check Airflow logs for detailed information on task execution and any errors encountered.

---
