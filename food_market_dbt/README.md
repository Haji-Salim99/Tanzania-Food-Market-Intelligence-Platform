# 🇹🇿 Tanzania Food Market Intelligence Platform

> An end-to-end cloud data engineering and analytics project that transforms raw food market data into interactive business intelligence dashboards using Python, Google BigQuery, dbt, and Power BI.

<!-- ====================================================== -->
<!-- HERO IMAGE -->
<!-- Replace with your project overview image -->
![Project Overview](images/platform.png)

---

## 📖 Project Overview

The **Tanzania Food Market Intelligence Platform** is an end-to-end data engineering and analytics solution built to help analyze food market prices across Tanzania.

The project automates the entire analytics pipeline—from extracting raw food price data to delivering interactive dashboards for market intelligence.

The solution demonstrates modern cloud data engineering practices including:

- Automated ELT pipelines
- Cloud data warehousing
- Analytics engineering using dbt
- Data quality testing
- Interactive business intelligence dashboards

---

## 🎯 Business Problem

Food prices fluctuate across regions and markets due to factors such as supply, demand, transportation costs, and seasonality.

Without a centralized analytics platform, decision makers must manually inspect large datasets to answer questions such as:

- Which regions have the highest food prices?
- Which commodities are becoming more expensive?
- How have prices changed over time?
- Which markets provide the most historical data?
- Which regions have the largest market coverage?

This project addresses those challenges by building a scalable cloud-based analytics platform.

---

## 🏗 Solution Architecture

The solution follows a modern analytics engineering workflow:

```
HDX / WFP Dataset
        │
        ▼
Python ELT Pipeline
        │
        ▼
Google BigQuery
        │
        ▼
dbt Staging Models
        │
        ▼
dbt Analytics Marts
        │
        ▼
Power BI Dashboards
```

---

# ⚙ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Data extraction, cleaning and loading |
| Google BigQuery | Cloud Data Warehouse |
| dbt | SQL transformations, testing and documentation |
| Power BI | Interactive dashboards |
| Git & GitHub | Version control |
| VS Code | Development environment |

---

# 📂 Dataset

**Source**

Humanitarian Data Exchange (HDX)

Publisher:

World Food Programme (WFP)

Coverage:

- Tanzania
- 2017 – 2026

Project statistics:

- 17 Regions
- 45 Markets
- 30+ Commodities
- 28,000+ Historical Records

---

# 🔄 ELT Pipeline

The ELT pipeline consists of four major stages.

### 1. Extract

Python downloads and validates historical food market data.

### 2. Load

Validated data is loaded into Google BigQuery.

### 3. Transform

dbt creates staging models and business-ready analytics marts.

### 4. Visualize

Power BI connects directly to analytics marts to build dashboards.

---

# 🗄 Data Warehouse

Raw data is stored inside Google BigQuery.

<!-- BIGQUERY IMAGE -->
![BigQuery Dataset](images/gcpp.png)

Warehouse objects include:

```
raw_food_prices

stg_food_prices

mart_region_summary

mart_region_commodity

mart_market_summary

mart_price_trends
```

---

# 🔧 Analytics Engineering (dbt)

dbt was used to transform raw datasets into reusable analytical models.

Features implemented:

- Modular SQL models
- Staging layer
- Analytics marts
- Documentation
- Data lineage
- Automated testing

<!-- DBT LINEAGE -->
![dbt Lineage](images/dbt-graph.png)

Analytics marts created:

| Mart | Purpose |
|------|----------|
| mart_region_summary | Regional market coverage |
| mart_region_commodity | Commodity analysis by region |
| mart_market_summary | Market-level insights |
| mart_price_trends | Historical price trends |

---

# ✅ Data Quality

The project includes automated dbt tests to validate transformed data.

Examples:

- Not Null Tests
- Model Documentation
- Data Lineage

All tests passed successfully during development.

---

# 📊 Power BI Dashboard Screenshots

These dashboards provide interactive market intelligence for decision makers.

<!-- DASHBOARD OVERVIEW -->
![Dashboard Overview](images/graph2.png)

Dashboard Pages

## Monthly Price Trends And Commodity Trends Comparison

<!-- EXECUTIVE DASHBOARD -->
![Executive Dashboard](images/graph3.png)

---

## Regional Analysis

<!-- REGIONAL DASHBOARD -->
![Regional Dashboard](images/graph1.png)

Provides:

- Regional comparisons
- Commodity distribution
- Market coverage

---


# 📁 Repository Structure

```
food-market-intelligence/

│

├── data/

├── notebooks/

├── scripts/

├── food_market_dbt/

├── dashboards/

├── images/

├── README.md

└── requirements.txt
```

---

# 🚀 How to Run

Clone repository

```bash
git clone https://github.com/<Haji-Salim99>/tanzania-food-market-intelligence-platform.git
```

Create virtual environment

```bash
python -m venv venv
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run ELT pipeline

```bash
python main.py
```

Run dbt

```bash
dbt run
dbt test
dbt docs generate
```

Open Power BI and connect to Google BigQuery to explore the analytics dashboards.

---

# 📈 Key Learnings

This project strengthened my skills in:

- Data Engineering
- Analytics Engineering
- SQL
- Python
- Cloud Data Warehousing
- Google BigQuery
- dbt
- Power BI
- Data Modeling
- Data Quality
- Data Visualization

---

# 🔮 Future Improvements

Possible future enhancements include:

- Incremental dbt models
- Star Schema implementation
- Apache Airflow orchestration
- Docker deployment
- CI/CD pipeline
- Machine Learning price forecasting
- Real-time data ingestion

---

# 👨‍💻 Author

**Haji**

Data Engineer

LinkedIn: *(https://www.linkedin.com/in/haji-salim-7951ba236/)*