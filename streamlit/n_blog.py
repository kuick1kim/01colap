import streamlit as st
import pandas as pd





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









dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('블로그 검색1', '블로그 검색2')
)

@st.cache
def load_data(name):
    data = None
    if name == '블로그 검색1':
        kms()        
        
    elif name == '블로그 검색2':
        DATA_URL='https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.xlsx'
        data = pd.read_csv(DATA_URL)  
        df
    else:
        DATA_URL= kms()        
        data = pd.read_csv(DATA_URL)     
#     return data







    
def kms():
    st.header('검색된 뉴스서비스')
    query = st.text_input('검색어를 넣어주세요. ex)검색어 ','')
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    df = pd.DataFrame(columns=["날짜","category","제목","내용","네이버링크","기사링크","사진링크"])
    try:
        for num in range(0,51,1):

            num1=num*10+1

            news_url = 'https://search.naver.com/search.naver?where=news&query={}&sm=tab_opt&sort=0&start={}'.format(query,num1)
            if num%10 ==0:
                st.write(num," : 50페이지 긁어오는중 입니다. 검색어 : ",query)
            req = requests.get(news_url, headers = headers)
            soup = BeautifulSoup(req.text, "html.parser")

            ul= soup.find("ul","list_news")
            lili= ul.find_all("li", "bx")

            for i in range(len(lili)):
                li = ul.find_all("li","bx")[i]
                dan1 = li.find("div", "info_group")
                unlonsa = dan1.find("a").text
                time = dan1.find("span","info").text
                try:
                    potallink = dan1.find_all("a")[1]['href']
                except:
                    potallink = "네이버 링크는 없음"

                link = li.find_all("a")[5]['href']
                try:
                    img = li.find_all('img')[1]['src']
                except:
                    img = "이미지는 없슴"
                title = li.find('a','news_tit').text
                article1 = li.find('div','news_dsc').text.replace("\n","")
                gisa1 = re.compile(r'[^ A-Za-z0-9가-힣+]').sub('',article1)
                df = df.append({"날짜":time,"category":unlonsa,"제목":title,"내용":gisa1,
                                "네이버링크":potallink,"기사링크":link,"사진링크":img}, ignore_index=True)    
    except:
        st.header("검색어를 넣어주세요")   
    
    towrite = io.BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    qu=query  # some strings
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="[검색어]{qu}.xlsx">내가 검색한 자료 다운받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    
    df
    
    for h, i,j,k,kk in zip(df["category"], df['날짜'],df['제목'],df['기사링크'],df['내용']):
            st.write(i," = = ",h)
            st.write(j)
            st.write(k)
            st.write(kk)

        
    return 




#     a = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.csv'  
#     df = pd.read_csv(a)  
    
# #     spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
# #     if spectra is not None:
# #         df = pd.read_csv(spectra)
#     list = st.sidebar.slider( '선택하세요',0, len(df)-1, 5)
#     st.write(list)
#     df1 = df.iloc[list:list+1, :]


#     for i,j in zip(df1['내용'],df1['링크']):
#         st.write(j)
#         hh1=i.split('\t')
#         a=1
#         for nn in hh1:
#             if nn is not None or nn != " " or nn != "" :                
#                 st.write(nn)
#                 a=a+1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# df = load_data(dataset_name)

# spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
# if spectra is not None:
#     df = pd.read_csv(spectra)
# #     dataset_name='외부데이터' 




# list = st.sidebar.slider( '선택하세요',0, len(df)-1, 5)
# st.write(list)
# df1 = df.iloc[list:list+1, :]


# for i,j in zip(df1['내용'],df1['링크']):
#     st.write(j)
#     hh1=i.split('\t')
#     a=1
#     for nn in hh1:
#         if nn is not None or nn != " " or nn != "" :                
#             st.write(nn)
#             a=a+1
         

    



        
        
        
        


