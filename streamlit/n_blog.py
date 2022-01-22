import pandas as pd
import streamlit as st
import re
import base64
import io




st.sidebar.markdown("""
[뉴스 분석 사이트로 이동](https://share.streamlit.io/kuick1kim/01colap/main/streamlit/newss.py/)
""")
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('ranking','news', 'blog')
)

def get_dataset(name):
    if name == 'ranking':          
        ranking()
    elif name == 'blog':
        ranking2() 
    else:
        ranking2()


######################################################################################################

def ranking():
    st.header('언론사별 주요뉴스 ')
    DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.csv')
    df = pd.read_csv(DATA_URL)  
    
    
    ########################여기는 추가넣는부분##############
    spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
    if spectra is not None:
        df = pd.read_csv(spectra)
        dataset_name='외부데이터' 
    df 
    
    
######################################################################################################

def ranking2():
    st.header('언론사별 주요뉴스 ')
    DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog3.csv')
    df = pd.read_csv(DATA_URL)  
    
    
    ########################여기는 추가넣는부분##############
    spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
    if spectra is not None:
        df = pd.read_csv(spectra)
        dataset_name='외부데이터' 
    df 
    
    

##################################################################################


if __name__ == '__main__':
    get_dataset(dataset_name)
