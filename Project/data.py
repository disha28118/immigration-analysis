import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

@st.cache_data
def load_data():
    df=pd.read_csv("Placement_Data_Full_Class.csv")
    df.head()
    return df

st.set_page_config(
layout='wide',
page_title='Placement Data Analysis',
page_icon='@',
)

with st.spinner('Loading data...'):
    df=load_data()
    st.sidebar.success('Data Loaded Successfully!!!')

#creating the ui interface
c1,c2,c3=st.columns([2,1,1])
c1.title('Placement Analysis')
c2.header('Summary of Data')
st.title('Placement Data Analysis')
st.write('## Data Overview')
st.write(df.head())
st.write('## Average Academic Point vs Employability Test Point')
p = df[['degree_p', 'etest_p']].describe()
plt.figure(figsize=(10, 6))
plt.title("Average Academic Point vs Employability Test Point")
plt.plot(p.degree_p.iloc[1:8], label='Average Academic Point')
plt.ylabel("Points")
plt.plot(p.etest_p.iloc[1:8], label='Employability Test Point')
plt.legend()
st.pyplot(plt)
df = df.set_index('status')
placed = df.loc['Placed']
st.write(f'Number of students placed: {placed.shape[0]}')
st.write('## Number of Students Placed')
plt.figure(figsize=(10, 6))
placed['salary'].plot(kind='line')
plt.title('Number of Students Placed')
plt.xlabel('Placed')
plt.ylabel('Package')
st.pyplot(plt)
st.write('## Gender Distribution in Campus')
gen = df.gender.value_counts(normalize=True) * 100
plt.figure(figsize=(6, 6))
plt.title('Gender Distribution in Campus')
labels = ['Male', 'Female']
plt.pie(gen, labels=labels, autopct='%.0f%%', startangle=90)
st.pyplot(plt)

st.write("## Statistics of Various Academic Points")
plt.figure(figsize=(10, 6))
plt.title("Statistics of Various Academic Points")
plt.ylabel("Points")
plt.plot(df[['ssc_p', 'hsc_p', 'degree_p', 'mba_p', 'etest_p']].iloc[0], label='Female')
plt.plot(df[['ssc_p', 'hsc_p', 'degree_p', 'mba_p', 'etest_p']].iloc[1], label='Male')
plt.legend()
st.pyplot(plt)
st.write('## Placement Stats Of Different Specialisations')
special = df.groupby('specialisation').value_counts(normalize=True) * 100
st.write(special)
p_s = df.loc['Placed']['specialisation']
spc = df.specialisation.value_counts(normalize=True) * 100
plt.figure(figsize=(6, 6))
spc.plot(kind='pie', autopct='%.0f%%', startangle=90)
st.pyplot(plt)
st.write("## Work Experience Distribution")
work = df.workex.value_counts(normalize=True) * 100
plt.figure(figsize=(10, 6))
work.plot(kind='bar')
plt.title('Work Experience Distribution')
plt.xlabel('Work Experience')
plt.ylabel('Percentage')
st.pyplot(plt)
st.write("## Top Scores of Employability Test for Marketing & Finance")
mfe = df[df.specialisation == 'Mkt&Fin'].nlargest(10, 'etest_p')
plt.figure(figsize=(10, 6))
plt.plot(mfe.index, mfe.etest_p, "o-c")
plt.title('Top Scores of Employability Test for Marketing & Finance')
plt.xlabel('Id of student')
plt.ylabel('Score')
st.pyplot(plt)


st.write("## SSC Percentage by Placement Status")
plt.figure(figsize=(10, 6))
plt.plot(df.ssc_p)
plt.title('SSC Percentage by Placement Status')
plt.xlabel('Placement Status')
plt.ylabel('SSC Percentage')
st.pyplot(plt)
st.write("## Pie Chart of Work Experience")
plt.figure(figsize=(7, 6))
plt.pie(df['workex'].value_counts(), labels=['Yes', 'No'], startangle=90, autopct='%.1f%%')
plt.title("Pie Chart of Work Experience")
st.pyplot(plt)
st.write("## Distribution of Salary for Placed Students")
plt.figure(figsize=(10, 6))
plt.hist(df['salary'].dropna(), bins=20, color='green')
plt.title('Distribution of Salary for Placed Students')
plt.xlabel('Salary')
plt.ylabel('Frequency')
st.pyplot(plt)
st.sidebar.header('Display Options')
columns_to_display = st.sidebar.multiselect('Select columns to display', df.columns.tolist(), default=df.columns.tolist())
st.write('## Selected Columns Data')
st.dataframe(df[columns_to_display])
st.sidebar.success('Data Loaded Successfully!!!')