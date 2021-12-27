from pkg_resources import DistributionNotFound
import streamlit as st
import pandas as pd

import numpy as np

st.sidebar.markdown("""
[자료 다운받기 사이트로 이동하기](https://share.streamlit.io/kuick1kim/01colap/main/streamlit/naver_news.py/)
""")


########################여기는 추가넣는부분##############



uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    


#########################성공###########################

llll = len(df)


many = st.slider('기간',  0, llll, (0, llll))
df1 = df.iloc[many[0]:many[1],:]

df1





