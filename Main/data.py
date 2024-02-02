# stock_utils.py

import yfinance as yf
import requests
from bs4 import BeautifulSoup
from yahoo_fin.stock_info import get_live_price
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor

def price_ticker(ticker):
    price = round(get_live_price(ticker), 2)

    tker = yf.Ticker(ticker)

    previous_ticker_data = tker.info['previousClose']

    change = round(price - previous_ticker_data, 2)

    percentage_change = round((change / previous_ticker_data) * 100 if previous_ticker_data != 0  else 0, 2)
    percentage_change = str(percentage_change) + ' %'

    price = '$' + str(price)
    if change > 0:
        change = '+' + str(change)
        percentage_change = '+' + percentage_change
    return price, change, percentage_change

def main_page_data(ticker):
    url = "https://finance.yahoo.com/quote/BTC-USD"

    # Make an HTTP request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the required data
    price = soup.find_all("fin-streamer")
    change = soup.find_all(attrs={"class": "e3b14781"})
    change_percentage = soup.find_all(attrs={"class": "e3b14781"})

    return price, change, change_percentage

def generate_candlestick_chart(ticker):
    bitcoin_data = yf.download(ticker, start='2014-01-01', end='2024-01-01')
    fig = go.Figure(data=[go.Candlestick(x=bitcoin_data.index, 
                                         open=bitcoin_data['Open'],
                                         high=bitcoin_data['High'],
                                         low=bitcoin_data['Low'],
                                         close=bitcoin_data['Close'])])
    
    fig.update_layout(xaxis_title='Date',
                      yaxis_title='Price',
                      template='plotly_dark',
                      xaxis_rangeslider_visible=True)
    
    df = pd.DataFrame(bitcoin_data)
    h_df = df.head(4)
    t_df = df.tail(3)
    combined_df = pd.concat([h_df, t_df])
    df_html = combined_df.to_html(classes='table table-striped', index=True)
    return fig, df_html

def prediction_chart(ticker):
    bitcoin_data = yf.download(ticker, start='2014-01-01', end='2024-01-01')

    # Select 'Close' prices for prediction
    df = bitcoin_data[['Close']].copy()

    # Feature scaling
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Create lag features for time series prediction
    for i in range(1, 6):  # Use lag features from t-1 to t-5
        df[f'Close(t-{i})'] = df['Close'].shift(i)

    # Drop missing values
    df = df.dropna()

    # Split the data into training and testing sets
    train_size = int(len(df) * 0.8)
    train_data, test_data = df.iloc[:train_size], df.iloc[train_size:]

    # Separate features and target variable
    X_train, y_train = train_data.drop('Close', axis=1), train_data['Close']
    X_test, y_test = test_data.drop('Close', axis=1), test_data['Close']

    # Train an MLPRegressor (you can tune hyperparameters as needed)
    model = MLPRegressor(hidden_layer_sizes=(50, 25), max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Prepare data for plotting
    actual_data = go.Scatter(x=test_data.index, y=test_data['Close'], mode='lines', name='Actual Data')
    predicted_data = go.Scatter(x=test_data.index, y=predictions, mode='lines', name='Predicted Data')

    # Create Plotly chart
    chart_data = [actual_data, predicted_data]
    layout = go.Layout(xaxis_title='Date',
                        yaxis_title='Closing Price',
                        template='plotly_dark',
                        xaxis_rangeslider_visible=True)
    fig = go.Figure(data=chart_data, layout=layout)

    return fig