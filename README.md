# Azure Data Engineering Project

## 📌 Project Overview

This project demonstrates an end-to-end data engineering pipeline using Azure services.

## 🏗 Architecture

* Azure Data Factory (ADF)
* Azure Data Lake Storage (ADLS Gen2)
* Azure Databricks (Serverless)
* Unity Catalog

## 🔄 Data Flow

1. Raw data ingested into Bronze layer (ADLS)
2. Data transformed in Databricks (Bronze → Silver)
3. Clean data stored in Delta format
4. Business-ready data prepared in Gold layer

## 📂 Layers

* Bronze → Raw JSON data
* Silver → Cleaned & structured data (Delta)
* Gold → Business-ready data

## ⚙️ Technologies Used

* Azure Data Factory
* Azure Data Lake Storage
* Azure Databricks (PySpark)
* Delta Lake
* Unity Catalog

## 🚀 Key Features

* End-to-end ETL pipeline
* Serverless Databricks compute
* Secure access using Managed Identity
* Delta Lake implementation

## 📌 Future Enhancements

* SCD Type 2 implementation
* Power BI integration
* CI/CD using Azure DevOps

