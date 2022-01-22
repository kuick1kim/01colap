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
        ranking() 
    else:
        ranking()


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
    
    
    
    
    
    
    
    
#     date = st.text_input('날짜를 넣어주세요.. 자료가 없을수도 있어요. ex)20210324')
    
    
    
    
    
    
#     news_url = 'https://news.naver.com/main/ranking/popularDay.nhn?date={}'.format(date)

#     headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
#     req = requests.get(news_url, headers = headers)
#     soup = BeautifulSoup(req.text, 'html.parser')
#     df = pd.DataFrame(columns=["category",'기사','날짜','링크'])
#     h111 = soup.select('.rankingnews_box')
#     num = 0
    
#     for i in range(len(h111)):        
#         h112=h111[i].find('strong').text
#         lll= h111[i].find_all('div')
#         kkk= h111[i].find_all('li')       
        
#         for j in range(len(lll)):
#             aa = lll[j].find('span').text
#             bb1 = lll[j].find('a').text
#             cc = lll[j].find('a').get('href')
#             num=num+1
#             df=df.append({"category":h112,'날짜': aa,'기사':bb1,'링크':cc}, ignore_index=True)

#     st.write(num)  

#     ki = st.sidebar.slider( '기사', 0, num, (0, num))    
#     df1 = df.loc[ki[0]:ki[1], :]
    
#     unlonsa = st.sidebar.text_input("검색하고 싶은 언론사를 넣어주세요",'')    
#     df3 = df1[df1["category"].str.contains(unlonsa)].copy()
    
#     kiki = st.sidebar.text_input("검색하고 싶은 기사단어를 넣어주세요",'')    
#     df2 = df3[df3['기사'].str.contains(kiki)].copy()
    


#     st.write(df2) 
    
             
#     towrite = io.BytesIO()
#     downloaded_file = df2.to_excel(towrite, encoding='utf-8', index=True, header=True)
#     towrite.seek(0)  # reset pointer
#     b64 = base64.b64encode(towrite.read()).decode()  # some strings
#     linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="뉴스다운.xlsx">선택하신 자료 다운받기</a>'
#     st.markdown(linko, unsafe_allow_html=True)
#     #===============================인코딩이 안되서 csv를 안씀================================
    
    
#     st.write('================================================================')
#     st.write('　')

#     for h, i,j,k in zip(df2["category"], df2['날짜'],df2['기사'],df2['링크']):
#         st.write(h," = = ",i,"=====",j,"<br>",k)
        


##################################################################################













if __name__ == '__main__':
    get_dataset(dataset_name)
