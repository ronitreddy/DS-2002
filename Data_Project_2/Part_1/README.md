# Part 1: Data Ingestion & Analysis

## Overview
This project entailed the creation and deployment of a data ingestion system that operates continuously for one hour, pulling data from a remote API every minute. The aim was to analyze changes over time in the data retrieved, which includes calculated values of π (pi) and associated factors, and to store these in a structured database.

## Procedure
1. **Database Design:**
- Developed a database schema for storing data retrieved from the API, structured around the `pi_data` table.
- Created `pi_data.sql` to define the schema with appropriate fields for `factor`, `pi`, and `time`.

2. **Data Extraction and Transformation:**
- Implemented a Python script to fetch data from the provided remote data API.
- Ensured data fetched each minute was transformed to align with the database schema, particularly focusing on the timestamp formatting to ensure consistency.

3. **Data Loading:**
- Loaded the transformed data into the `pi_data` table within the database, confirming each insertion was executed at the start of every minute.
- Managed database connections and transactions within the Python environment to maintain data integrity.

4. **Data Integrity and Validation:**
- Applied primary key constraints in the `pi_data` table to prevent duplicate entries and ensure data uniqueness.
- Validated the data ingestion process by monitoring logs and using SQL queries to check data consistency.

5. **Performance Benchmarking:**
- Monitored and recorded the performance and timing of data retrieval and database operations, ensuring that the process adhered to the requirement of executing once per minute.
- Analyzed system logs to identify any operational issues or delays in data handling.

6. **Queries and Analysis:**
- Authored various SQL queries to examine relationships between data fields and to observe patterns over time, as detailed in the Jupyter Notebook `Data_Ingestion_and_Analysis.ipynb`.
- Conducted a detailed analysis of the data collected, documented in `Data_Fields_Analysis.md`.

7. **Conclusion:**
- Successfully deployed a data ingestion system that accurately captured and analyzed data from a remote API, running continuously for one hour as required.
- Demonstrated the capability to handle time-series data and perform analytical assessments on the changing values within the dataset.

## Provided Files and Used Resources

### Provided Files
- `pi_data.sql`: SQL file used to generate the database schema.
- `Data_Ingestion_and_Analysis.ipynb`: Jupyter Notebook containing the complete Python code used for data extraction, loading, and analysis.
- `Database_Table_Contents.csv`: CSV file containing the data loaded into the database.
- `Database_Table_Screenshot.png`: Screenshot verifying the consistent execution of data ingestion every minute.
- `Data_Fields_Analysis.md`: Markdown file containing analysis of the remote data API's data fields and the observed changes over time.

### Used Resources
- **[Remote Data API](https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi)**: Utilized to retrieve data for ingestion into the database system.
