# Azure Data Engineering Project (Bronze → Silver → Gold)

## 📌 Overview

Built an end-to-end data pipeline using Azure and Databricks implementing Medallion Architecture.

## 🏗 Architecture

* Azure Data Lake Storage (ADLS Gen2)
* Azure Data Factory (ADF)
* Azure Databricks (Serverless)
* Unity Catalog

## 🔄 Data Flow

API → ADF → Bronze (ADLS) → Databricks → Silver → Gold

## 📂 Layers

* Bronze: Raw JSON data
* Silver: Cleaned & structured data (Delta format)
* Gold: Business-ready curated data

## ⚙️ Key Features

* End-to-end pipeline
* Delta Lake implementation
* Data deduplication & cleaning
* Secure access using Managed Identity
* Unity Catalog integration

## 🚀 Future Enhancements

* SCD Type 2 implementation
* Power BI dashboards
* Pipeline orchestration improvements

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



