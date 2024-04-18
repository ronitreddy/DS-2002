# Part 1: Data Ingestion & Analysis

## Overview
This project involves the creation and deployment a robust data ingestion system that operates continuously for an hour, collecting data every minute from a remote API. The goal is to demonstrate proficiency in scheduling tasks, handling real-time data streams, and analyzing time-series data to identify patterns and explain their implications.

## Procedure

### System Setup and Scheduling
- **Design and Implementation of Database Schema**: Created a database schema to store the retrieved data efficiently, with fields designed to capture the `factor`, `pi`, and `time` values from the API response.
- **Configuration of Data Retrieval**: Set up a scheduled process in Python that calls the remote data API once every minute, ensuring the process starts at the beginning of a minute and runs continuously for 60 minutes.

### Data Retrieval and Database Interaction
- **Data Extraction and Transformation**: Developed a function within the scheduler to fetch data from the API and format it as required by the database schema.
- **Data Loading**: Implemented mechanisms to insert the formatted data into the database without duplication, using timestamp verification to ensure each entry is unique.

### Validation and Performance Monitoring
- **System Monitoring**: Ensured that the data retrieval and insertion processes were executed as scheduled without any misses or delays.
- **Performance Optimization**: Monitored the performance of the database operations and optimized queries to handle the influx of data every minute efficiently.

### Analysis and Reporting
- **Data Analysis**: Examined the relationships between the relevant data fields (`factor`, `pi`, and `time`) and how these relationships change over the course of an hour, and documented findings.
- **Documentation and Results Presentation**: Compiled the analysis results and insights regarding observed patterns within the data fields and potential explanations for these changes into a comprehensive Markdown document (`Data_Fields_Analysis.md`).

### Conclusion and Submission
- **Project Wrap-Up**: Reviewed the entire process to ensure that all benchmarks were met, including the precise execution of data retrieval and consistent database updates.
- **Repository Management**: All code, documentation, and additional resources (such as `Database_Table_Contents.csv` and `Database_Table_Screenshot.png`) were organized and uploaded for evaluation.

## Provided Files and Used Resources

### Provided Files
- `pi_data.sql`: SQL file used to generate the database schema.
- `Data_Ingestion_and_Analysis.ipynb`: Jupyter Notebook containing the complete Python code used for data extraction, loading, and analysis.
- `Database_Table_Contents.csv`: CSV file containing the data recorded in the database after the execution of the data ingestion process.
- `Database_Table_Screenshot.png`: PNG screenshot verifying the consistent execution of data ingestion every minute.
- `Data_Fields_Analysis.md`: Markdown file containing analysis of the data fields extracted from the remote data API and the observed changes over time.

### Used Resources
- **[Remote Data API](https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi)**: Utilized to retrieve data for ingestion into the database system.
