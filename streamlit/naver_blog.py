from bs4 import BeautifulSoup
import pandas as pd
import time

import glob
import os

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

import base64
import io


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")


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

            for i in range(3):
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
#                     st.write(title)
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
        
                
#     df        
    return df


if __name__ == "__main__":
    delete_selenium_log()    
    st.title('셀레니움')       
    executable_path = "notset"
    
    st.balloons()
#     st.info('Selenium is running, please wait...')
    result = run_selenium()
    
    st.info(f'Result -> {result}')
    result1 = pd.DataFrame(result)
    time.sleep(1)
    
    towrite = io.BytesIO()
    downloaded_file = result.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="[검색어]2.xlsx">내가 검색한 자료 다운받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    
    
    towrite = io.BytesIO()
    downloaded_file = result1.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="[검색어]1.xlsx">내가 검색한 자료 다운받기111</a>'
    st.markdown(linko, unsafe_allow_html=True)
    
    
    
    st.info('Successful finished. Selenium log file is shown below...')
    show_selenium_log()
#     if st.button('Start Selenium run'):
#         st.info('Selenium is running, please wait...')
#         result = run_selenium()
#         st.write(result)
#         st.info(f'Result -> {result}')
#         st.info('Successful finished. Selenium log file is shown below...')
#         show_selenium_log()
