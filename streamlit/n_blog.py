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
    elif name == '세부검색':
        ranking3() 
    elif name == '검색기S':
        blog_main()
    else:
        blog_main2()


######################################################################################################
def ranking():
    st.header('언론사별 주요뉴스 ')
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
#     df 
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
    st.header('언론사별 주요뉴스 ')
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
            query = st.text_input('검색어를 넣어주세요. ex)검색어 ','맛집')
            list1 = st.sidebar.slider( '몇개까지 검색할까요? 10개 단위로만 가능', 21, 100, 20)
            list2 = (int(list1)%10)
            url="https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={}".format(query)
            driver.get(url)

            time.sleep(1)


            df5 = pd.DataFrame(columns=['작성자', '제목', 'year',"month","day",
                                       '내용','링크'])

            #######################10번누르기###################################
            for i in range(2,11,1):
                time.sleep(0.8)
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

                    df5=df5.append({'작성자':name, '제목':title, 'year':year,"month":month,"day":day,
                                       '내용':sub,'링크':link}, ignore_index=True)

            ######################더보기누르기###################################
            st.write('10번 눌렀습니다./전체는', list2*10,'번입니다.')
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

                    df5=df5.append({'작성자':name, '제목':title, 'year':year,"month":month,"day":day,
                                       '내용':sub,'링크':link}, ignore_index=True)

            #######################더보기 누르기와 30번 이후 5번###################################
            for kk in range(list2-1):
                st.write('10번 눌렀습니다./전체는', list2*10,'번입니다.')
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

                        df5=df5.append({'작성자':name, '제목':title, 'year':year,"month":month,"day":day,
                                           '내용':sub,'링크':link}, ignore_index=True)
            #######################10번누르기###################################            
            st.write('완료 하였습니다.')            
    return df5,query


def blog_main():
    delete_selenium_log()    
    st.title('셀레니움')       
    executable_path = "notset"
    
    st.balloons()
    result,query = run_selenium()
    
    towrite = io.BytesIO()
    downloaded_file = result.to_excel(towrite, encoding='utf-8', index=False, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="[블로그]{query}.xlsx">내가 검색한 자료 다운받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    
    st.info('Successful finished. Selenium log file is shown below...')


######################################################################################################
def blog_main2():
    oo=1
    st.header('블로그 다운받은것을 여기다 넣으세요 기본으로 검색합니다. ')
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    spectra3 = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
    if spectra3 is not None:
        try:
            ddf = pd.read_csv(spectra3)
        except:
            ddf = pd.read_excel(spectra3)
        dataset_name='외부데이터' 
    if ddf != '':
        dff3 = pd.DataFrame(columns=['작성자','시간','제목','링크','내용','이미지모음'])
        dfs = pd.DataFrame(columns=['내용'])

        # query= input('내용을 쓰시요')
        for ll in ddf['링크']:
            if oo%10==0:
                st.write(oo,"/전체는 ",len(ddf),'입니다')
            oo=oo+1
            a=ll.split('?')[0]
            a=a.split("/")
            b,c=a[-2],a[-1]

            url= 'https://blog.naver.com/PostView.naver?blogId={}&logNo={}&redirect=Dlog&widgetTypeCall=true&directAccess=false'.format(b,c)

            html = session.get(url, headers=headers).content
            soup = BeautifulSoup(html, "html.parser")
            try:

                table = soup.find('table',id='printPost1')

                title1 = table.find('div','pcol1').text
                title= title1.replace('\n','') 

                date = table.find('span','se_publishDate pcol2').text
                name= table.find('span','nick').text

                imgimg = table.find_all('img','se-image-resource')
                imgb=''
                for a in range(len(imgimg)):
                    img = table.find_all('img','se-image-resource')[a].get('data-lazy-src')    
                    imgb=imgb+"@@@@@"+str(img)    

                storya= table.find_all('p',"se-text-paragraph")                            
                storyb=""
                for b in range(len(storya)):
                    story = table.find_all('p',"se-text-paragraph") [b].text
                    if story != "" :
                        dfs=dfs.append({'내용':storyb}, ignore_index=True)
                    storyb = storyb+'\t'+str(story)

                dff3=dff3.append({'작성자':name,'시간':date,'제목':title,'링크':ll,'내용':storyb,
                      '이미지모음':imgb}, ignore_index=True)

            except:
                pass

        towrite1 = io.BytesIO()
        downloaded_file = dff3.to_excel(towrite1, encoding='utf-8', index=False, header=True)
        towrite1.seek(0)  # reset pointer
        b64a = base64.b64encode(towrite1.read()).decode()    
        linko1= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64a}" download="[블로그]전체.xlsx">전체 자료 다운</a>'
        st.markdown(linko1, unsafe_allow_html=True)

        towrite2 = io.BytesIO()
        downloaded_file = dfs.to_excel(towrite2, encoding='utf-8', index=False, header=True)
        towrite2.seek(0)  # reset pointer
        b64b = base64.b64encode(towrite2.read()).decode()    
        linko2= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64b}" download="[블로그]내용만.xlsx">내용 자료 다운</a>'
        st.markdown(linko2, unsafe_allow_html=True)
    


if __name__ == '__main__':
    get_dataset(dataset_name)
