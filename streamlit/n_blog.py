import pandas as pd
import streamlit as st
import re
import base64
import io





dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('ranking','news', 'blog')
)

def get_dataset(name):
    if name == 'ranking':          
        ranking()
    elif name == 'blog':
        ranking3() 
    else:
        ranking3()


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
def ranking3():
    st.header('언론사별 주요뉴스 ')
    DATA_URL1 = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog3.csv')
    df1 = pd.read_csv(DATA_URL1)  
    
    
    ########################여기는 추가넣는부분##############
    spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
    if spectra is not None:
        df1 = pd.read_csv(spectra)
        dataset_name='외부데이터' 
    
    word = st.sidebar.text_input("검색하고 싶은 말씀을 넣어주세요",'')
    df2 = df1[df1["말씀"].str.contains(word)].copy()
    df2
    
    

##################################################################################

if __name__ == '__main__':
    get_dataset(dataset_name)
