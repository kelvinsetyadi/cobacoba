import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import yfinance as yf

def get_ema(ticker_data, period):
    ema = ticker_data['Close'].ewm(span=period).mean()
    column_name = 'ema_' + str(period)
    ticker_data[column_name] = ema
    return ticker_data

def get_ticker_data(ticker_symbol, data_period, data_interval):
    ticker_data = yf.download(tickers=ticker_symbol, period=data_period, interval=data_interval)

    if len(ticker_data) == 0:
        st.write('Could not find the ticker data. Modify ticker symbol or reduce the Period value.')
    else:
        #Format the x-axis to skip dates with missing values
        ticker_data.index = ticker_data.index.strftime("%d-%m-%Y %H:%M")
    return ticker_data

def get_candle_chart(ticker_data):
    candle_fig = go.Figure()
    candle_fig.add_trace(
        go.Candlestick(x=ticker_data.index,
        open=ticker_data['Open'],
        close=ticker_data['Close'],
        low=ticker_data['Low'],
        high=ticker_data['High'],
        name='Market Data'
        )
    )
    candle_fig.update_layout(
        height=800,
    )
    return candle_fig

def add_ema_trace(candle_fig, timestamp, ema, trace_name, color):
    candle_fig.add_trace(
        go.Scatter(
            x=timestamp,
            y=ema,
            name=trace_name,
            line=dict(color=color)
        )
    )
    return candle_fig
