import streamlit as st
from cryptocmd import CmcScraper
import pandas_datareader as pdr
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd




st.write('# 비트코인 데이터 Web app')
#이름쓰기




# 메뉴바
st.sidebar.header('Menu')

name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT'])

sevendayago = datetime.today() - timedelta(90)


start_date = st.sidebar.date_input('Start date', sevendayago)
end_date = st.sidebar.date_input('End date', datetime.today())


# 여기까지가 옆에 있는 바이다. //////////////////////



# name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT','005930.KS'])

# https://coinmarketcap.com
scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
# 스크래퍼는 이것이다. 

df = scraper.get_dataframe()

fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='가격')
fig_volume = px.line(df, x='Date', y=['Volume'], title='Volume')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)

#############################################여기까지는 잘된다##############






st.write('''
# 삼성전자 주식 데이터
마감 가격과 거래량을 차트로 보여줍니다!
''')

# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
dr = pdr.get_data_yahoo('005930.KS',start_date,end_date)
# dr=pd.DataFrame(dr)
# st.line_chart(dr.Close)
# st.line_chart(dr.Volume)



fig_close1 = px.line(dr, x=index, y=['Open', 'High', 'Low', 'Close'], title='가격')
# fig_volume1 = px.line(dr, x='Date', y=['Volume'], title='Volume')

st.plotly_chart(fig_close1)
# st.plotly_chart(fig_volume1)
