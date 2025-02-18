import streamlit as st
import plotly.graph_objs as go
import util

if __name__ == '__main__':
    ticker_symbol = st.sidebar.text_input(
    "Please enter the stock symbol", 'MSFT'
    )
    data_period = st.sidebar.text_input('Period', '10d')
    data_interval = st.sidebar.radio('Interval', ['15m','30m','1h','1d','5d'])
    ema1 = st.sidebar.text_input('EMA 1', 20)
    ema2 = st.sidebar.text_input('EMA 2', 50)

    st.header(ticker_symbol)

    ticker_data = util.get_ticker_data(ticker_symbol, data_period, data_interval)
    ticker_data = util.get_ema(ticker_data, int(ema1))
    ticker_data = util.get_ema(ticker_data, int(ema2))

    candle_fig = util.get_candle_chart(ticker_data)
    candle_fig = util.add_ema_trace(candle_fig, ticker_data.index, ticker_data['ema_' + ema1], 'EMA ' + ema1, "#ffeb3b")
    candle_fig = util.add_ema_trace(candle_fig, ticker_data.index, ticker_data['ema_' + ema2], 'EMA ' + ema2, "#2962ff")
    st.write(candle_fig)