# Technical Design Document

## 1. Objectives
The goal of this project is to develop a robust data pipeline that extracts, transforms, and visualizes data. The solution utilizes:
- **Azure Data Factory** for data ingestion
- **Databricks with PySpark** for data transformation
- **Spark SQL** for analysis
- **Power BI** for visualization

---

## 2. Project Architecture Diagram
> to be inserted

---

## 3. Project Architecture Overview
The project adopts a **Medallion Architecture** with bronze, silver, and gold data layers. This model organizes data into distinct layers based on their level of processing and refinement.

### 3.1. Data Ingestion (Bronze Layer):
- **Source**: Raw data (CSV file)
- **Ingestion Tool**: Azure Data Factory
- **Storage**: Azure Data Lake Storage Gen2

### 3.2. Data Transformation (Silver Layer):
- **Processing Tool**: Azure Databricks with PySpark
- **Storage**: Delta Lake tables

### 3.3. Data Refinement (Gold Layer):
- **Final Dataset**: Refined, analytical data stored in Delta Lake tables

### 3.4. Data Analysis & Visualization:
- **Tools for Analysis**: Databricks (SQL queries)
- **Visualization Tool**: Power BI or Databricks visualizations

---

## 4. Implementation Plan

### 4.1. Data Ingestion and Storage
- Identify the raw data sources (e.g., CSV files).
- Set up an Azure Data Factory pipeline for ingestion.
  - Configure activities like the Copy Activity to transfer data from source systems to Azure Data Lake Storage Gen2.

### 4.2. Data Transformation and Cleaning
- Establish an Azure Databricks workspace.
- Use PySpark to clean and transform the data.
- Apply performance optimization techniques:
  - **Caching**
  - **Partitioning**
  - **Indexing**
- Store the transformed data in Delta Lake tables for efficient querying and updates.

### 4.3. Data Analysis and Visualization
- Prepare transformed data for analysis with additional cleaning or transformations.
- Use Databricks notebooks for SQL-based analysis.
- Create interactive dashboards and reports using Power BI or Databricks visualizations.

---

## 5. Tools and Services

| **Process**         | **Tools/Services**                |
|----------------------|-----------------------------------|
| Data Ingestion       | Azure Data Factory               |
| Data Storage         | Azure Data Lake, Azure Delta Tables |
| Data Transformation  | Databricks, PySpark              |
| Data Analytics       | Spark SQL                        |
| Data Visualization   | Power BI                         |

---

## 6. Schema Design

### Raw Data Schema (Bronze Layer)
| **Column**    | **Data Type** | **Description**                           |
|---------------|---------------|-------------------------------------------|
| id            | STRING        | Unique identifier for each restaurant.    |
| name          | STRING        | Restaurant name.                         |
| city          | STRING        | City where the restaurant is located.    |
| rating        | DOUBLE        | Restaurant rating.                       |
| rating_count  | STRING        | Number of people who rated.              |
| cost          | DOUBLE        | Cost per person.                         |
| cuisine       | STRING        | Types of cuisines offered.               |
| lic_no        | STRING        | License number.                          |
| address       | STRING        | Full address of the restaurant.          |
| menu          | STRING        | Menu details of each restaurant.         |
| link          | STRING        | Restaurant URLs.                         |

### Transformed Data Schema (Silver/Gold Layer)
| **Column**      | **Data Type** | **Description**                           |
|------------------|---------------|-------------------------------------------|
| Restaurant_ID    | STRING        | Unique identifier for each restaurant.    |
| Name             | STRING        | Restaurant name.                         |
| City             | STRING        | City where the restaurant is located.    |
| Cuisine          | STRING        | Comma-separated cuisines served.         |
| Rating           | DOUBLE        | Numeric rating.                          |
| Rating_Count     | INT           | Number of ratings derived from string.   |
| Lic_no           | STRING        | License number.                          |
| Cost             | DOUBLE        | Average cost per person.                 |
| Address          | STRING        | Full address of the restaurant.          |
| TimeStamp        | DATETIME      | Data inserted timestamp.                 |

### Audit Table Schema
| **Column**      | **Data Type** | **Description**                           |
|------------------|---------------|-------------------------------------------|
| Id              | STRING        | Unique ID for the pipeline execution.    |
| Process_Id      | STRING        | Unique ID for the specific process.      |
| Process_Name    | STRING        | Name of the process.                     |
| Start_Time      | TIMESTAMP     | Pipeline execution start time.           |
| End_Time        | TIMESTAMP     | Pipeline execution end time.             |
| Status          | STRING        | Pipeline execution status (Success/Failure). |
| Message         | STRING        | Log messages, if any.                    |

---

## 7. Testing

### Data Accuracy

| **Test Case ID** | **Description**                                   | **Steps**                              | **Expected Outcome**                         | **Negative Scenario**                      |
|-------------------|--------------------------------------------------|----------------------------------------|---------------------------------------------|--------------------------------------------|
| DA-01            | Verify all required fields are present.          | Check id, name, city, etc., for null.  | All fields are present.                     | Missing fields result in an error.         |
| DA-02            | Verify `id` is unique.                           | Check for duplicates in `id`.          | No duplicate ids.                           | Duplicate ids trigger an error.            |
| DA-03            | Validate `rating` values.                        | Ensure ratings are between 0-5.        | Ratings within range.                       | Invalid or out-of-range ratings.           |

### Data Quality

| **Test Case ID** | **Description**                                   | **Steps**                              | **Expected Outcome**                         | **Negative Scenario**                      |
|-------------------|--------------------------------------------------|----------------------------------------|---------------------------------------------|--------------------------------------------|
| DQ-01            | Verify null/NaN fields.                          | Check for null/NaN values.             | No null values in columns.                  | Presence of null values.                   |
| DQ-08            | Validate unique license numbers.                 | Check for duplicates in `lic_no`.      | Each restaurant has a unique license.       | Duplicate license numbers.                 |

---

## 8. Data Security

| **Test Case ID** | **Description**                                   | **Steps**                              | **Expected Outcome**                         | **Negative Scenario**                      |
|-------------------|--------------------------------------------------|----------------------------------------|---------------------------------------------|--------------------------------------------|
| DS-01            | Verify sensitive data exposure.                  | Check if `lic_no` is encrypted.        | `lic_no` is encrypted or masked.            | Plain-text `lic_no` is stored or transmitted. |
