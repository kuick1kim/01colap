import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import re
import base64
import io


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
    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)    
        return data
    df = load_data()
    df 
    
    

##################################################################################
######################################################################################################

def ranking2():
    st.header('언론사별 주요뉴스 ')
    DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog3.csv')
    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)    
        return data
    df = load_data()
    df 
    
    

##################################################################################



if __name__ == '__main__':
    get_dataset(dataset_name)
