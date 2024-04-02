# Order Management Database Project

## Overview
This project involved creating an order management database for a fictional company using data from multiple sources, including an existing database, a CSV file, and an API. The order management database was designed to store information about customers, products, orders, and suppliers.

## Procedure
1. **Database Design:**
   - Designed a `order_management` database schema with tables for customers, products, orders, order details (items), and suppliers.
  
2. **Data Extraction and Transformation:**
   - Extracted comprehensive data from an existing `Northwind` database, transforming it to match the `order_management` database schema.
   - Extracted comprehensive data from a CSV file, transforming it to match the `order_management` database schema.
   - Extracted product data from an API call, transforming it to fit the `order_management` database schema.

3. **Data Loading:**
   - Loaded the transformed data from the `Northwind` database into the `order_management` database.
   - Loaded the transformed data from the CSV file into the `order_management` database.
   - Loaded the transformed product data from the API call into the `order_management` database.

4. **Data Integrity and Validation:**
   - Ensured data integrity by defining primary and foreign key constraints.
   - Validated data consistency and correctness during the transformation and loading processes.

5. **Performance Benchmarking:**
   - Recorded and analyzed the performance of the ETL process for each data source.
   - Identified and resolved potential operation failures to improve performance.

6. **Queries and Analysis:**
   - Authored numerous SQL queries to retrieve data from multiple tables:
     - `SELECT` data from customers, orders, and order items tables.
     - Performed aggregation using `SUM`, `COUNT`, and `AVERAGE` functions, grouped by customer ID and other relevant columns.

7. **Conclusion:**
   - Successfully created an order management database with accurate and consistent data from multiple sources.
   - Demonstrated the ability to extract, transform, and load various data formats and sources in a database project.

## Provided Files and Used Resources

### Provided Files
- **order_management.sql**: SQL file used to generate my designed `order_management` database.
- **northwind.sql**: SQL file containing the `Northwind` database schema.
- **northwind-data.sql**: SQL file containing the `Northwind` database data.
- **sales_data_sample.csv**: CSV file containing sample sales data.
- **Data_Project_1.ipynb**: Jupyter Notebook containing the completed ETL work code for this data project. 

### Used Resources
- **[Northwind Database](https://github.com/Microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs)**: Used for demonstrating database design/querying to extract data from one or more SQL database tables, and populating the order_management database.
- **[Sales Data CSV](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)**: Used for retrieving a local data file, converting its original format, and populating the order_management database.
- **[Fake Store API](https://fakestoreapi.com/)**: Used for retrieving additional product information through an API call, and populating the order_management database.
