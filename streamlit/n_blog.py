import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import re
import base64
import io

from selenium.webdriver.common.action_chains import ActionChains

import time

import glob
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")





dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('큰검색','세부검색', '검색기S',"검색기B")
)

def get_dataset(name):
    if name == '큰검색':          
        ranking()
    else name == '세부검색':
        ranking3() 
    

######################################################################################################
def ranking():
    st.header('블로그 검색기 대 ')
    DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.csv')
    df = pd.read_csv(DATA_URL)      
    
    ########################여기는 추가넣는부분##############
    spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
    if spectra is not None:
        try:
            df = pd.read_csv(spectra)
        except:
            df = pd.read_excel(spectra)
        dataset_name='외부데이터' 

    list = st.sidebar.slider( '여러가지 검색해 보세요', 0, len(df)-1, 5)

    df1 = df.iloc[list:list+1, :]
    df1
    for bb in df1["내용"]:
        bb1=bb.split("\t")
        
        
        for cc in bb1:
            if cc != "" :
                st.write(cc)

    
######################################################################################################
def ranking3():
    st.header('블로그 검색기 소')
    DATA_URL1 = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog3.csv')
    df1 = pd.read_csv(DATA_URL1)  
    
    
    ########################여기는 추가넣는부분##############
    spectra2 = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
    if spectra2 is not None:
        try:
            df1 = pd.read_csv(spectra2)
        except:
            df1 = pd.read_excel(spectra2)
        
        dataset_name='외부데이터' 
    
    word = st.sidebar.text_input("검색하고 싶은 내용검색/ 아무것도 안넣으면, 엄청돌아감",'마시고')
    df2 = df1[df1["내용"].str.contains(word)].copy()
    
    df2= df2.sample(frac=1)
    
    for k in df2['내용']:
        st.write(k)  
    




if __name__ == '__main__':
    get_dataset(dataset_name)
