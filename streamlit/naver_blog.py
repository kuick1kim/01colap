












import glob
import os

import streamlit as st
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
        url = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
        driver.get(url)
        xpath = '//*[@class="ui-mainview-block eventpath-wrapper"]'
        # Wait for the element to be rendered:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_xpath(xpath))
        # element = driver.find_elements_by_xpath(xpath)
        name = element[0].get_property('attributes')[0]['name']
        # print(name)
    return name


if __name__ == "__main__":
    delete_selenium_log()
    st.set_page_config(page_title="Selenium Test", page_icon='✅',
        initial_sidebar_state='collapsed')
    st.title('🔨 Selenium Test for Streamlit Sharing')
    st.markdown("""
        This app is only a very simple test for **Selenium** running on **Streamlit Sharing** runtime. <br>
        The suggestion for this demo app came from a post on the Streamlit Community Forum.  <br>
        <https://discuss.streamlit.io/t/issue-with-selenium-on-a-streamlit-app/11563>  <br>
        Unfortunately this app has deployment issues on Streamlit Sharing, sometimes deployment fails, sometimes not... 😞
        This is just a very very simple example and more a proof of concept.
        A link is called and waited for the existence of a specific class and read it. If there is no error message, the action was successful.
        Afterwards the log file of chromium is read and displayed.
        ---
        """, unsafe_allow_html=True)
    # executable_path = get_chromedriver_path()
    executable_path = "notset"
    # st.info(f'Chromedriver Path: {str(executable_path)}')
    st.balloons()
    if st.button('Start Selenium run'):
        st.info('Selenium is running, please wait...')
        result = run_selenium()
        st.info(f'Result -> {result}')
        st.info('Successful finished. Selenium log file is shown below...')
        show_selenium_log()
















# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import streamlit as st

# import streamlit as st
# import requests
# import re
# from selenium import webdriver
# import time

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("lang=ko_KR")



# query = st.text_input('검색어를 넣어주세요. ex)검색어 ','')


# # path='https://raw.githubusercontent.com/kuick1kim/01colap/main/streamlit/chromedriver.exe'

# path = "/chromedriver.exe" 
# driver = webdriver.Chrome(path, options=options)


# url = 'https://search.naver.com/search.naver?where=influencer&sm=tab_jum&query={}'.format(query)


# df = pd.DataFrame(columns=['날짜','블로거','분야1','분야2', 
#                                        '제목', '내용','링크','이미지'])
# driver.get(url)
# time.sleep(0.5)

# for i in range(22):
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     time.sleep(1)
#     if i%3==0:
#         st.write(i,"  21번까지")

# st.header("여기서 부터 2분정도 걸려요")

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')  



# lili = soup.find_all('li', 'keyword_bx')
# leee= len(lili)
# leee5=leee/5
# kkk=1
# for i in range(len(lili)):
#     if i%leee5 == 0:
#         st.write(kkk*20,"% 끝냈어요 / 전체는",leee)
#         kkk=kkk+1
#     li = soup.find_all('li', 'keyword_bx')[i]
#     date = li.find('span','date').text    
#     name = li.find('span','txt').text    
#     cate1 = li.find('span','etc highlight').text
#     cate2 = li.find('span','etc').text
#     title1 = li.find('div','dsc_area')
#     title = title1.find('a','name_link').text
    
#     story = title1.find('p','dsc').text
#     link = title1.find('a').get('href')
#     img1 = li.find('div','thumb_area type_solo')
#     try:
#         img = img1.find('img').get('src')
#     except: 
#         img ='이미지 없어요'

#     df=df.append({'날짜':date,'블로거':name,'분야1':cate1,'분야2':cate2, 
#                                        '제목':title, '내용':story,'링크':link,'이미지':img}, ignore_index=True)
# driver.quit()
    
# df
