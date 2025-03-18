import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Post grad'
    return 'Less than a Bachelor’s degree'

@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_survey_results.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### The information is extracted from Stack Overflow Developer Survey 2024 edition
        """
    )

    st.write("""### Mean Salary Based on Country (USD) per year""")

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending = True)
    st.bar_chart(data)

    st.write("""### Mean Salary Based on Experience (USD) per year""")

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending = True)
    st.line_chart(data)

    data = df["Country"].value_counts()

    st.write("""### Number of Data from different countries""")
    
    st.bar_chart(data)
    