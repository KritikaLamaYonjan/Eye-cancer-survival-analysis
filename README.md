# Biology or Budget: What Drives Eye Cancer Survival?

## Project Overview

This project is a **Streamlit-based interactive dashboard** that explores the relationship between clinical, genetic, and macro-economic factors and eye cancer survival.

The dashboard allows users to interactively analyze patient survival patterns based on:

- Economic spending levels
- Cancer stage at diagnosis
- Genetic markers
- Age
- GDP expenditure
- Survival time
- Genetic testing status

## Project Objectives

The main objectives of this project are to:

- Analyze eye cancer survival trends over time.
- Investigate the relationship between cancer stage and survival.
- Examine the impact of genetic markers on survival.
- Analyze differences in diagnostic testing across economic tiers.
- Explore the relationship between age, national spending, and survival.
- Identify correlations between clinical, genetic, and economic variables.

## Dashboard Visualizations

The dashboard contains six interactive visualizations:

### 1. 5-Year Survival Trends
Shows average survival time across different economic spending tiers from 2019 to 2023.

### 2. Survival Distribution by Stage
Compares the distribution of survival time across cancer stages and economic tiers.

### 3. Diagnostic Gap Analysis
Shows the difference in genetic testing status across economic spending tiers.

### 4. Mean Survival: Genetic Impact
Compares average survival between patients with BRAF mutations and those who were not tested.

### 5. Age & National Spending Interaction
Explores the relationship between patient age, survival time, and GDP expenditure.

### 6. Statistical Correlation Matrix
Shows correlations between survival time, GDP expenditure, cancer stage, age, and genetic profile.

## Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Jupyter Notebook

## Project Files

| File | Description |
|---|---|
| `Dashboard.py` | Main Streamlit dashboard application |
| `evecancercode.ipynb` | Jupyter Notebook containing data analysis and exploration |
| `Eye_Cancer_Merged_data_set.csv` | Merged dataset used for the dashboard |
| `eye_cancer_patients.csv` | Eye cancer patient dataset |
| `GDP_indicator.csv` | GDP expenditure indicator data |
| `aggregated_survival_summary.csv` | Aggregated survival analysis data |
| `Task3_Exploratory_Visuals.png` | Exploratory data visualizations |
| `requirements.txt` | Python libraries required to run the project |

## Installation

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Clone the Repository

Clone this repository to your local computer:

```bash
git clone https://github.com/KritikaLamaYonjan/Eye-cancer-survival-analysis.git