import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    layout="wide",
    page_title="Biology or Budget: Strategic Intelligence"
)




st.markdown("""
    <style>

       

        .stApp {
            background-color: #f4f5f7 !important;
        }

        .main {
            background-color: #f4f5f7 !important;
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }


        
           

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }


       

        h1 {
            color: #000000 !important;
            font-weight: 700 !important;
        }


        /* Horizontal line */

        hr {
            border-color: #d0d3d8 !important;
        }


        

        [data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 1px solid #e1e4e8;
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label {
            color: #000000 !important;
        }


        /* Sidebar header */

        [data-testid="stSidebar"] .stMarkdown {
            color: #000000 !important;
        }


        
        [data-testid="stMultiSelect"] {
            color: #000000 !important;
        }

        [data-testid="stMultiSelect"] label {
            color: #000000 !important;
        }

        /* Selected tags */

        [data-baseweb="tag"] {
            background-color: #ff4b4b !important;
            color: #ffffff !important;
        }

        [data-baseweb="tag"] span {
            color: #ffffff !important;
        }


        

        [data-testid="stMetric"] {
            background-color: transparent !important;
        }

        [data-testid="stMetricLabel"] {
            color: #000000 !important;
            font-weight: 600 !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 2rem !important;
            font-weight: 700 !important;
            color: #b00808 !important;
        }

        [data-testid="stMetricDelta"] {
            color: #000000 !important;
        }


        

        div[data-testid="stVerticalBlock"] > div:has(div.stPlotlyChart) {
            background-color: #ffffff !important;
            border: 1px solid #e1e4e8 !important;
            padding: 15px !important;
            border-radius: 10px !important;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.05) !important;
        }




        .stMarkdown,
        .stText,
        p,
        label {
            color: #000000;
        }


    </style>
""", unsafe_allow_html=True)



st.title(
    "Biology or Budget: Clinical vs. Macro-Economic Drivers in Eye Cancer Survival"
)

st.markdown("---")


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("Eye_Cancer_Merged_data_set.csv")


df_raw = load_data()



st.sidebar.header("Dashboard Controls")

year_range = st.sidebar.slider(
    "Timeline",
    2019,
    2023,
    (2019, 2023)
)

selected_tiers = st.sidebar.multiselect(
    "Economic Tier",
    options=df_raw["Economic_Tier"].unique(),
    default=df_raw["Economic_Tier"].unique()
)

selected_genetics = st.sidebar.multiselect(
    "Genetic Profile",
    options=df_raw["Genetic_Markers"].unique(),
    default=df_raw["Genetic_Markers"].unique()
)




df = df_raw[
    (df_raw["Year"].between(year_range[0], year_range[1])) &
    (df_raw["Economic_Tier"].isin(selected_tiers)) &
    (df_raw["Genetic_Markers"].isin(selected_genetics))
].copy()




df["Genetic_Numeric"] = df["Genetic_Markers"].map({
    "BRAF Mutation": 1,
    "Not Tested": 0
})

df["Stage_Numeric"] = df["Stage_at_Diagnosis"].map({
    "Stage I": 1,
    "Stage II": 2,
    "Stage III": 3,
    "Stage IV": 4
})




k1, k2, k3, k4, k5 = st.columns(5)

k1.metric(
    "Patient Count",
    f"{len(df)}"
)

k2.metric(
    "Testing Rate",
    f"{(df['Genetic_Markers'] != 'Not Tested').mean() * 100:.1f}%"
)

k3.metric(
    "Avg Survival",
    f"{df['Survival_Time_Months'].mean():.1f} Mo"
)

k4.metric(
    "GDP Spend",
    f"{df['GDP_Expenditure_Percent'].mean():.2f}%"
)

k5.metric(
    "BRAF Mutation",
    f"{(df['Genetic_Markers'] == 'BRAF Mutation').mean() * 100:.1f}%"
)




CHART_HEIGHT = 310




def style_chart(fig):

    
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",

        font=dict(
            family="Arial",
            size=12,
            color="black"
        ),

        title=dict(
            font=dict(
                family="Arial",
                size=16,
                color="black"
            ),
            x=0.02
        ),

        legend=dict(
            font=dict(
                family="Arial",
                size=11,
                color="black"
            )
        ),

        margin=dict(
            l=5,
            r=5,
            t=40,
            b=5
        )
    )


    

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#e0e0e0",
        zeroline=False,

        title_font=dict(
            family="Arial",
            size=12,
            color="black"
        ),

        tickfont=dict(
            family="Arial",
            size=10,
            color="black"
        ),

        linecolor="#999999",
        linewidth=1
    )


    

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#e0e0e0",
        zeroline=False,

        title_font=dict(
            family="Arial",
            size=12,
            color="black"
        ),

        tickfont=dict(
            family="Arial",
            size=10,
            color="black"
        ),

        linecolor="#999999",
        linewidth=1
    )


    

    if fig.layout.annotations:
        fig.update_annotations(
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )


    return fig




row1_1, row1_2, row1_3 = st.columns(3)

row2_1, row2_2, row2_3 = st.columns(3)




with row1_1:

    with st.container():

        trend_df = (
            df.groupby(
                ["Year", "Economic_Tier"]
            )["Survival_Time_Months"]
            .mean()
            .reset_index()
        )

        fig1 = px.line(
            trend_df,
            x="Year",
            y="Survival_Time_Months",
            color="Economic_Tier",
            markers=True,

            title="1. 5-Year Survival Trends",

            color_discrete_map={
                "High-Spending": "#b00808",
                "Mid-Spending": "grey",
                "Low-Spending": "#f1c40f"
            },

            height=CHART_HEIGHT
        )

        fig1.update_layout(
            showlegend=False
        )

        fig1 = style_chart(fig1)

        st.plotly_chart(
            fig1,
            use_container_width=True
        )




with row1_2:

    with st.container():

        fig2 = px.box(
            df,
            x="Stage_at_Diagnosis",
            y="Survival_Time_Months",
            color="Economic_Tier",

            title="2. Survival Distribution by Stage",

            color_discrete_map={
                "High-Spending": "#b00808",
                "Mid-Spending": "grey",
                "Low-Spending": "#f1c40f"
            },

            category_orders={
                "Stage_at_Diagnosis": [
                    "Stage I",
                    "Stage II",
                    "Stage III",
                    "Stage IV"
                ]
            },

            height=CHART_HEIGHT
        )

        fig2.update_layout(
            showlegend=False
        )

        fig2 = style_chart(fig2)

        st.plotly_chart(
            fig2,
            use_container_width=True
        )



with row1_3:

    with st.container():

        diag_summary = (
            df.groupby(
                ["Economic_Tier", "Genetic_Markers"]
            )
            .size()
            .reset_index(name="count")
        )

        fig3 = px.bar(
            diag_summary,
            x="Economic_Tier",
            y="count",
            color="Genetic_Markers",

            title="3. Diagnostic Gap Analysis",

            color_discrete_map={
                "BRAF Mutation": "#b00808",
                "Not Tested": "grey"
            },

            height=CHART_HEIGHT
        )

        fig3.update_layout(
            legend=dict(
                orientation="h",
                y=-0.2,
                title=None
            )
        )

        fig3 = style_chart(fig3)

        st.plotly_chart(
            fig3,
            use_container_width=True
        )




with row2_1:

    with st.container():

        summary_4 = (
            df.groupby(
                ["Economic_Tier", "Genetic_Markers"]
            )["Survival_Time_Months"]
            .agg(["mean", "std"])
            .reset_index()
        )

        fig4 = px.scatter(
            summary_4,
            x="Economic_Tier",
            y="mean",
            color="Genetic_Markers",

            error_y="std",

            title="4. Mean Survival: Genetic Impact",

            color_discrete_map={
                "BRAF Mutation": "#b00808",
                "Not Tested": "grey"
            },

            height=CHART_HEIGHT
        )

        fig4.update_traces(
            marker=dict(
                size=10
            )
        )

        fig4.update_layout(
            showlegend=False
        )

        fig4 = style_chart(fig4)

        st.plotly_chart(
            fig4,
            use_container_width=True
        )


# ============================================================
# POSITION 5
# AGE & NATIONAL SPENDING INTERACTION
# ============================================================

with row2_2:

    with st.container():

        sample_df = df.sample(
            min(300, len(df)),
            random_state=42
        )

        fig5 = px.scatter(
            sample_df,
            x="Age",
            y="Survival_Time_Months",

            size="GDP_Expenditure_Percent",

            color="Genetic_Markers",

            opacity=0.6,

            title="5. Age & National Spending Interaction",

            color_discrete_map={
                "BRAF Mutation": "#b00808",
                "Not Tested": "grey"
            },

            size_max=12,

            height=CHART_HEIGHT
        )

        fig5.update_layout(
            showlegend=False
        )

        fig5 = style_chart(fig5)

        st.plotly_chart(
            fig5,
            use_container_width=True
        )



with row2_3:

    with st.container():

        cols = [
            "Survival_Time_Months",
            "GDP_Expenditure_Percent",
            "Stage_Numeric",
            "Age",
            "Genetic_Numeric"
        ]

        corr = df[cols].corr()

        fig6 = px.imshow(
            corr,

            text_auto=".3f",

            color_continuous_scale="RdYlGn",

            title="6. Statistical Correlation Matrix",

            height=CHART_HEIGHT
        )

        fig6.update_layout(
            coloraxis_showscale=False
        )

        # Force heatmap values to black
        fig6.update_traces(
            textfont=dict(
                color="black",
                size=11
            )
        )

        fig6 = style_chart(fig6)

        st.plotly_chart(
            fig6,
            use_container_width=True
        )