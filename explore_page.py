import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories,cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x == 'More than 50 years':
        return 50
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
    return 'Less than a Bachelors'

@st.cache_data
def load_data():
    df = pd.read_csv(r"survey_results_public.csv")
    df_1 = df[['Country','EdLevel','YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    df_1 = df_1.rename({'ConvertedCompYearly':'Salary'}, axis=1)
    df_1 = df_1[df_1['Salary'].notnull()]
    df_1 = df_1.dropna()
    df_1 = df_1[df_1['Employment'] == 'Employed, full-time']
    df_1 = df_1.drop('Employment',axis=1)

    country_map = shorten_categories(df_1.Country.value_counts(),400)
    df_1['Country'] = df_1['Country'].map(country_map)
    df_1 = df_1[df_1['Salary'] <= 250000]
    df_1 = df_1[df_1['Salary'] >= 10000]
    df_1 = df_1[df_1['Country'] != 'Other'] 
    df_1['YearsCodePro'] = df_1['YearsCodePro'].apply(clean_experience)
    df_1['EdLevel'] = df_1['EdLevel'].apply(clean_education)
    return df_1

df_1 = load_data()

def show_explore_page():
    st.title('Explore software engineer Salaries')

    st.write("""### Stack Overflow Developer Survey 2023""")

    data = df_1['Country'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", startangle=45)
    ax1.axis('equal')

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)


    st.write("""
    #### Mean Salary Based On Country
""")
    
    data = df_1.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""
    #### Mean Salary Based On Experience
""")
    data = df_1.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)

