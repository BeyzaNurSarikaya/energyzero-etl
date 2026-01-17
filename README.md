# ⚡ EnergyZero ETL & Automation Pipeline

<p align="center">
<img src="[https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Python-3776AB%3Fstyle%3Dfor-the-badge%26logo%3Dpython%26logoColor%3Dwhite)" />
<img src="[https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Pandas-150458%3Fstyle%3Dfor-the-badge%26logo%3Dpandas%26logoColor%3Dwhite)" />
<img src="[https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Docker-2496ED%3Fstyle%3Dfor-the-badge%26logo%3Ddocker%26logoColor%3Dwhite)" />
<img src="[https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Apache_Airflow-017CEE%3Fstyle%3Dfor-the-badge%26logo%3Dapache-airflow%26logoColor%3Dwhite)" />
</p>

## 📌 Project Overview

This project is a high-performance **ETL (Extract, Transform, Load)** pipeline designed to handle real-time energy price data. By leveraging **Dockerized Apache Airflow**, it automates the transition from raw API data to analytical-ready storage.

---

## 🚀 Key Features

| Phase | Description | Tools |
| --- | --- | --- |
| **Extract** | Retrieval of hourly energy prices from EnergyZero API. | `Requests`, `JSON` |
| **Transform** | Data cleaning, VAT calculation (21%), and date/time engineering. | `Pandas` |
| **Load** | Compressed and schema-enforced storage in Parquet format. | `PyArrow` |
| **Orchestrate** | Fully automated scheduling and monitoring. | `Airflow` |

---

## 🏗️ Architecture & Workflow

1. **Extract:** A Python script fetches the last 7 days of electricity prices.
2. **Transform:**
* Splits `ReadingDate` into separate `Date` and `Time` columns.
* Calculates `Price_with_VAT` (Base Price * 1.21).
* Enforces correct data types for downstream analytics.


3. **Load:** Saves the resulting dataframe as a `.parquet` file in the `data/processed/` directory.

---

## 📂 Folder Structure

```bash
energyzero_etl/
├── 📁 dags/                # Airflow DAG definitions
├── 📁 scripts/             # Python ETL logic
├── 📁 data/
│   ├── 📁 raw/             # Raw JSON landing zone
│   └── 📁 processed/       # Optimized Parquet files
├── 🐳 Dockerfile           # Custom Airflow image
├── 🚢 docker-compose.yml   # Infrastructure as Code
└── 📄 requirements.txt     # Dependency list

```

---

## 🛠️ Quick Start Guide

> **Prerequisite:** Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running.

### 1. Deployment

```bash
git clone https://github.com/BeyzaNurSarikaya/energyzero-etl.git
cd energyzero-etl
docker-compose up --build -d

```

### 2. Monitoring

Access the Airflow Dashboard at **`http://localhost:8080`**:

* **User:** `admin`
* **Pass:** `admin`

---

## 📈 Future Enhancements

* [ ] Integrate a **PostgreSQL** database as the final "Load" destination.
* [ ] Add a **Streamlit** dashboard for real-time price visualization.
* [ ] Implement **Slack/Email alerts** for failed pipeline tasks.

---

### 👩‍💻 Author

**Beyza Nur Sarıkaya**

* LinkedIn: [beyza-nur-sarikaya](https://www.linkedin.com/in/beyza-nur-sarikaya/)

