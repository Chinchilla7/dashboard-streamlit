import streamlit as st
import pandas as pd
import numpy as np


DATE_COLUMN = 'date'
DATA_URL = ('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/hospitalizations/covid-hospitalizations.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data = load_data(1000)

st.title('COVID-19 hospitalizations & excess mortality')

code = '''def test():
    print("Hello, this is a testing code-block")'''
st.code(code, language='python')

st.subheader('Raw data')
st.write(data)

hist_values = np.histogram(
    data['value'], bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Raw data 2')

DATE_COLUMN_2 = 'date'
DATA_URL_2 = ('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/excess_mortality/excess_mortality.csv')

def load_data_2(nrows):
    data2 = pd.read_csv(DATA_URL_2, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN_2] = pd.to_datetime(data[DATE_COLUMN])
    return data2

data2 = load_data_2(1000)
st.write(data2)

bar_values = np.histogram(
    data2['p_scores_all_ages'], bins=24, range=(0,24))[0]
st.bar_chart(bar_values)
