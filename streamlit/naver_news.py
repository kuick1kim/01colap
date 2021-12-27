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
    ('news', 'blog', 'ranking')
)

def get_dataset(name):
    if name == 'news':
        gather1()    
    elif name == 'blog':
        blog_main()   
    else:
        ranking()


def gather1():
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
#     except:
#         st.write('검색어를 넣어야 검색이 되요')
        
    return 


######################################################################################################

def ranking():
    st.header('언론사별 주요뉴스 ')
    date = st.text_input('날짜를 넣어주세요.. 자료가 없을수도 있어요. ex)20210324')
    news_url = 'https://news.naver.com/main/ranking/popularDay.nhn?date={}'.format(date)

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    req = requests.get(news_url, headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    df = pd.DataFrame(columns=["category",'기사','날짜','링크'])
    h111 = soup.select('.rankingnews_box')
    num = 0
    
    for i in range(len(h111)):        
        h112=h111[i].find('strong').text
        lll= h111[i].find_all('div')
        kkk= h111[i].find_all('li')       
        
        for j in range(len(lll)):
            aa = lll[j].find('span').text
            bb1 = lll[j].find('a').text
            cc = lll[j].find('a').get('href')
            num=num+1
            df=df.append({"category":h112,'날짜': aa,'기사':bb1,'링크':cc}, ignore_index=True)

    st.write(num)  

    ki = st.sidebar.slider( '기사', 0, num, (0, num))    
    df1 = df.loc[ki[0]:ki[1], :]
    
    unlonsa = st.sidebar.text_input("검색하고 싶은 언론사를 넣어주세요",'')    
    df3 = df1[df1["category"].str.contains(unlonsa)].copy()
    
    kiki = st.sidebar.text_input("검색하고 싶은 기사단어를 넣어주세요",'')    
    df2 = df3[df3['기사'].str.contains(kiki)].copy()
    


    st.write(df2) 
    
             
    towrite = io.BytesIO()
    downloaded_file = df2.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()  # some strings
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="뉴스다운.xlsx">선택하신 자료 다운받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    #===============================인코딩이 안되서 csv를 안씀================================
    
    
    st.write('================================================================')
    st.write('　')

    for h, i,j,k in zip(df2["category"], df2['날짜'],df2['기사'],df2['링크']):
        st.write(h," = = ",i,"=====",j,"<br>",k)
        


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

            url = 'https://search.naver.com/search.naver?where=influencer&sm=tab_jum&query={}'.format(query)

            df = pd.DataFrame(columns=['날짜','블로거','분야1','분야2', '제목', '내용','링크','이미지'])
            driver.get(url)
            time.sleep(1)

            for i in range(21):
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(1.5)
                if i%2==0:
                    st.write(i,"  10번까지", query)

            st.header("여기서 부터 2분정도 걸려요")

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser') 

            lili = soup.find_all('li', 'keyword_bx')
            leee= len(lili)
            leee5=leee/5
            kkk=1
            st.write(leee)
            driver.quit()

            for i in range(len(lili)):

                if i%leee5 == 0:
                    st.write(kkk*20,"% 끝냈어요 / 전체는",leee,query)
                    kkk=kkk+1
                try:
                    li = soup.find_all('li', 'keyword_bx')[i]
                    date = li.find('span','date').text    
                    name = li.find('span','txt').text    
                    cate1 = li.find('span','etc highlight').text
                    cate2 = li.find('span','etc').text
                    title1 = li.find('div','dsc_area')
                    title = title1.find('a','name_link').text

                    story = title1.find('p','dsc').text
                    link = title1.find('a').get('href')
                    img1 = li.find('div','thumb_area type_solo')
                    try:
                        img = img1.find('img').get('src')
                    except: 
                        img ='이미지 없어요'

                    df=df.append({'날짜':date,'블로거':name,'분야1':cate1,'분야2':cate2, 
                                                           '제목':title, '내용':story,'링크':link,'이미지':img}, ignore_index=True)

                except:
                    pass
        
                
    
    return df,query


def blog_main():
    delete_selenium_log()    
    st.title('셀레니움')       
    executable_path = "notset"
    
    st.balloons()
    result,query = run_selenium()

    
    towrite = io.BytesIO()
    downloaded_file = result.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="[블로그]{query}.xlsx">내가 검색한 자료 다운받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    
    st.info('Successful finished. Selenium log file is shown below...')
















if __name__ == '__main__':
    get_dataset(dataset_name)
