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
    st.table(df)


# spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
# if spectra is not None:
    
#     df = pd.read_excel(spectra)
    
#     dataset_name='외부데이터' 
# else :
#     df = "데이터를 넣어주세요"
#########################성공###########################


# df
# # many = st.sidebar.slider('기간',  0, akiml, (0, akiml))
# df = df.iloc[many[0]:many[1],:]




