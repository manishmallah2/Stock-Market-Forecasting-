import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st


start = '2005-01-01'
end = '2023-02-28'


st.title('Stock Price Inclination Forecast')
st.caption("This is a web app that allows users to analyze and forecast the stock price trend.")


from datetime import datetime
import pandas as pd
import yfinance as yf


# Get the stock ticker from the user
user_input = st.text_input('Enter Stock Ticker', 'AMZN')


# Convert the start and end dates to datetime objects
start_date = datetime.strptime(start, '%Y-%m-%d')
end_date = datetime.strptime(end, '%Y-%m-%d')


# Use the yfinance module to get the stock data
data = yf.download(user_input, start=start_date, end=end_date)


# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)


# Describing Data Visually
st.subheader('Data From Year 2005 - 2023')
st.write(df.describe())


st.subheader('Volume Chart Vs Time Chart')
st.caption("A Volume chart displays the volume of a specific asset or security over a certain time period.")
st.bar_chart(df)


# Chart Visualisation
st.subheader('Closing Price Vs Time Chart')
st.caption("A Closing price chart displays the closing price of an asset or security over a certain time period.")
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close,'m')
st.pyplot(fig)


st.subheader('Closing Price Vs Time Chart with 100MA')
st.caption("A Time chart with 100MA displays prices and average of last 100 days.")
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100, 'r')
plt.plot(df.Close,'b')
st.pyplot(fig)