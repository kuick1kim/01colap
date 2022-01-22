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





dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('큰검색','세부검색', '검색기')
)

def get_dataset(name):
    if name == '큰검색':          
        ranking()
    elif name == '세부검색':
        ranking3() 
    else:
        blog_main()


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
    df1
#     for bb in df1["내용"]:
#         bb1=bb.split("\t")
#         st.write(bb1)
        
#         for cc in bb1:
#             if bb != "" :
#                 st.write(bb)

    
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
    
    word = st.sidebar.text_input("검색하고 싶은 내용검색/ 아무것도 안넣으면, 엄청돌아감",'마시고')
    df2 = df1[df1["내용"].str.contains(word)].copy()
    
    df2= df2.sample(frac=1)
    for k in df2['내용']:
        st.write(k)  
    

##################################################################################
def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)


def get_chromedriver_path():
    results = glob.glob('/**/chromedriver', recursive=True)  # workaround on streamlit sharing
    which = results[0]
    return which





def run_selenium():
    name = str()
    with webdriver.Chrome(options=options, service_log_path='selenium.log') as driver:
            query = st.text_input('검색어를 넣어주세요. ex)검색어 ','')

            url="https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={}".format(query)
            driver.get(url)

            time.sleep(1)


            df = pd.DataFrame(columns=['작성자', '제목', 'year',"month","day",
                                       '내용','링크'])

            #######################10번누르기###################################
            for i in range(2,11,1):
                time.sleep(0.5)
                link='/html/body/ui-view/div/main/div/div/section/div[3]/span[{}]/a'.format(i)    
                element1 = driver.find_element_by_xpath(link)
                ActionChains(driver).move_to_element(element1).click(element1).perform()
                time.sleep(0.5)

                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                divdiv= soup.find_all('div','item multi_pic')

                for k in range(len(divdiv)):
                    div= soup.find_all('div','item multi_pic')[k]
                    title= div.find('span','title').text
                    name = div.find('em','name_author').text
                    sub = div.find('a','text').text
                    link = div.find("a").get('href') 
                    date = div.find('span','date').text
                    date1 = date.replace(" ","").split('.')
                    try:
                        year,month,day = date1[0],date1[1],date1[2]
                    except:
                        year,month,day = "","",date1

                    df=df.append({'작성자':name, '제목':title, 'year':year,"month":month,"day":day,
                                       '내용':sub,'링크':link}, ignore_index=True)

            ######################더보기누르기###################################
            st.write('10번 눌렀습니다. ')
            kms = '/html/body/ui-view/div/main/div/div/section/div[3]/a'
            element1 = driver.find_element_by_xpath(kms)
            ActionChains(driver).move_to_element(element1).click(element1).perform()
            time.sleep(1.5)
            #######################11번-20번 누르기###################################

            for i in range(2,11,1):

                time.sleep(0.5)
                link='/html/body/ui-view/div/main/div/div/section/div[3]/span[{}]/a'.format(i)    
                element1 = driver.find_element_by_xpath(link)
                ActionChains(driver).move_to_element(element1).click(element1).perform()
                time.sleep(0.5)

                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                divdiv= soup.find_all('div','item multi_pic')

                for k in range(len(divdiv)):
                    div= soup.find_all('div','item multi_pic')[k]
                    title= div.find('span','title').text
                    name = div.find('em','name_author').text
                    sub = div.find('a','text').text
                    link = div.find("a").get('href') 
                    date = div.find('span','date').text
                    date1 = date.replace(" ","").split('.')
                    try:
                        year,month,day = date1[0],date1[1],date1[2]
                    except:
                        year,month,day = "","",date1

                    df=df.append({'작성자':name, '제목':title, 'year':year,"month":month,"day":day,
                                       '내용':sub,'링크':link}, ignore_index=True)

            #######################더보기 누르기와 30번 이후 5번###################################
            for kk in range(5):
                st.write('10번 눌렀습니다. ')
                kms = '/html/body/ui-view/div/main/div/div/section/div[3]/a[2]'    
                element1 = driver.find_element_by_xpath(kms)
                ActionChains(driver).move_to_element(element1).click(element1).perform()
                time.sleep(3)

                for i in range(2,11,1):
                    time.sleep(0.5)
                    link='/html/body/ui-view/div/main/div/div/section/div[3]/span[{}]/a'.format(i)    
                    element1 = driver.find_element_by_xpath(link)
                    ActionChains(driver).move_to_element(element1).click(element1).perform()
                    time.sleep(0.5)

                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    divdiv= soup.find_all('div','item multi_pic')

                    for k in range(len(divdiv)):
                        div= soup.find_all('div','item multi_pic')[k]
                        title= div.find('span','title').text
                        name = div.find('em','name_author').text
                        sub = div.find('a','text').text
                        link = div.find("a").get('href') 
                        date = div.find('span','date').text
                        date1 = date.replace(" ","").split('.')
                        try:
                            year,month,day = date1[0],date1[1],date1[2]
                        except:
                            year,month,day = "","",date1

                        df=df.append({'작성자':name, '제목':title, 'year':year,"month":month,"day":day,
                                           '내용':sub,'링크':link}, ignore_index=True)
            #######################10번누르기###################################            
            st.write('완료 하였습니다.')            
    return df,query


def blog_main():
    delete_selenium_log()    
    st.title('셀레니움')       
    executable_path = "notset"
    
    st.balloons()
    result,query = run_selenium()

    
    towrite = io.BytesIO()
    downloaded_file = result.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  
    b64 = base64.b64encode(towrite.read()).decode()    
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="[블로그]{query}.xlsx">내가 검색한 자료 다운받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    
    st.info('Successful finished. Selenium log file is shown below...')

##################################################################################
    
    
    


if __name__ == '__main__':
    get_dataset(dataset_name)
