# Data Pipeline and Analysis of Restaurant Data

## Overview  
This project develops a data engineering pipeline to analyze restaurant data from various cities on the Swiggy platform. Using PySpark, Spark SQL, and Azure Data Factory, the data is processed and transformed to generate insights on ratings, cuisines, and trends, presented through databricks dashboard.

> For detailed documentaion See [Technical Design Document](Documentation.md)

## Features  
- **Data Ingestion**: Data from JSON and other sources is ingested into Azure Data Lake using Azure Data Factory.  
- **Data Transformation**: PySpark is used to cleanse, transform, and enrich the data.  
- **Data Quality Assurance**: Techniques to ensure data accuracy and consistency, such as null handling, bias elimination, and integrity validation.  
- **SQL Analysis**: Spark SQL queries to extract insights and create materialized views.  
- **Visualization**: Dashboards created using Databricks or Power BI to visualize restaurant trends.  
- **Audit Logging**: Execution logs for process monitoring stored in Azure Log Analytics or tables.  

## Tools Used
1. Python 3.8
2. PySpark  
3. Azure Data Factory  
4. Databricks (for transformations and visualization)  
5. Azure Data Lake Storage Gen2
6. Azure Key Vault
7. Azure Log Analytics
 

## Pipeline Workflow  
### 1. Data Ingestion  
- Data is ingested from JSON, CSV files containing restaurant details using Azure Data Factory.  


### 2. Data Transformation  
- **Null Handling**: Missing data replaced or flagged for validation.  
- **Rating Count Conversion**: Convert fields like `50+ ratings` into numerical values.  
- **Cuisine Parsing**: Identify and process multiple cuisines for restaurants.  
- **SQL Queries**: Execute Spark SQL for custom queries.  

### 3. Audit Logging  
- An audit table logs pipeline executions with fields such as process ID, start time, end time, errors, etc.  

### 4. Visualization  
- Generate dashboards for insights.  

## Project Structure  
```plaintext  
restaurant-data-pipeline/  
├── Datasets/  
│   └── swiggy.csv 
│   └── data.json
├── Notebooks/  
│   ├── extract.ipynb  
│   ├── transform.ipynb  
│   ├── aggregate.ipynb  
│   └── analyze.ipynb 
├── Images/  
│   ├── Architecture/
│   ├── Screenshots/
├── DOCUMENTATION.md
├── README.md  
└── LICENSE  
```  

## Results  
- Insights into restaurant trends and performance.  
- Improved data quality and accuracy.  
- Real-time monitoring with audit logs.  

## License  
This project is licensed under the The GNU General Public License v3.0. See the `LICENSE` file for details.  

## Acknowledgments  
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)  
- [Azure Data Factory Documentation](https://learn.microsoft.com/en-us/azure/data-factory/introduction)  
- [Databricks Documentation](https://learn.microsoft.com/en-us/azure/databricks/)
- [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)  
