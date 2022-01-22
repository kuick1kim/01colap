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
    list = st.sidebar.slider( '여러가지 검색해 보세요', 0, len(df)-1, 5)

    df1 = df.iloc[list:list+1, :]
    for bb in df1["내용"]:
        bb1=bb.split("\t")
        for cc in bb1:
            if bb != "" :
                st.write(bb)

    
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
    df2 = df1[df1["내용"].str.contains(word)].copy()
    
    df2= df2.sample(frac=1)
    for k in df2['내용']:
        st.write(k)
    
    

##################################################################################

if __name__ == '__main__':
    get_dataset(dataset_name)
