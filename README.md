Biology or Budget:What drives Eve Cancer Survival

This project is a Streamlit-based interactive dashboard.

To run the application on your local machine, follow the instructions provided below.

Prerequisites:

1.Before running the dashboard, ensure that you have Python installed on your system. You will also need the following Python libraries:
streamlit, pandas, plotly, numpy

2.Required Files:
Ensure that the following files are located in the same directory:

A.Dashboard.py (The main Streamlit script)
B.Eye_Cancer_Merged_data_set.csv (The dataset used for the visualizations)

Installation Steps:

1.Open your terminal or command prompt and navigate to the folder containing the project files.

2.Install the necessary dependencies by typing the following command:
pip install streamlit pandas plotly numpy

Execution:

Once the libraries are installed, you can launch the dashboard by running the following command in your terminal:

streamlit run Dashboard.py

Dashboard Usage:

After running the command, a new tab will open in your default web browser displaying the dashboard. You can use the controls located in the sidebar on the left side of the screen to filter the data. These filters include:

1.Timeline: Use the slider to select a specific range of years (2019–2023).

2.Economic Tier: Choose one or multiple economic categories (e.g., High-Spending, Mid-Spending, Low-Spending).

3.Genetic Profile: Filter data based on genetic markers (e.g., BRAF Mutation, Not Tested).

The KPIs and all six visualizations will update automatically based on your selections. The layout is optimized to display all charts clearly in a structured grid without unnecessary scrolling.