from pkg_resources import DistributionNotFound
import streamlit as st
import pandas as pd

import numpy as np




########################여기는 추가넣는부분##############
spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
if spectra is not None:
    try:
        df = pd.read_excel(spectra)
    except:
        df = pd.read_csv(spectra)
    dataset_name='외부데이터' 
else :
    df = "데이터를 넣어주세요"
#########################성공###########################


df
# many = st.sidebar.slider('기간',  0, akiml, (0, akiml))
# df = df.iloc[many[0]:many[1],:]


st.sidebar.markdown("""
[자료 다운받기 사이트로 이동하기](https://share.streamlit.io/kuick1kim/01colap/main/streamlit/naver_news.py/)
""")

