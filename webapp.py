import streamlit as st
import plotly.express as px
import pandas

import dbHelper

# df = pandas.read_csv("temperaturedata.txt")
df = dbHelper.query_all("temperatures_times")
dates = [item[0] for item in df]
temp = [item[1] for item in df]

figure = px.line(x=dates, y=temp,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)