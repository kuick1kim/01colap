import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import re
import base64
import io



def gather1():
    st.header('검색된 뉴스서비스')
    query = st.text_input('검색어를 넣어주세요. ex)검색어 ','')
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    df = pd.DataFrame(columns=["날짜","언론사","제목","내용","네이버링크","기사링크","사진링크"])
    try:
    for num in range(0,51,1):
        
        num1=num*10+1

        news_url = 'https://search.naver.com/search.naver?where=news&query={}&sm=tab_opt&sort=0&start={}'.format(query,num1)
        if num%10 ==0:
            st.write(num)
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
            df = df.append({"날짜":time,"언론사":unlonsa,"제목":title,"내용":gisa1,
                            "네이버링크":potallink,"기사링크":link,"사진링크":img}, ignore_index=True)    
    except:
        st.header("검색어를 넣어주세요")   
    df
    towrite = io.BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    qu=query  # some strings
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="[검색어]{qu}.xlsx">내가 검색한 자료 다운받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    return df,query




if __name__ == '__main__':
    gather1()




























# def main():
#     st.header('언론사별 주요뉴스 ')
#     query = st.text_input('날짜를 넣어주세요.. 자료가 없을수도 있어요. ex)검색어 ')

#     news_url = 'https://search.naver.com/search.naver?where=news&query={}&sm=tab_opt&sort=0&start=1'.format(query)

#     headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
#     req = requests.get(news_url, headers = headers)

#     soup = BeautifulSoup(req.text, 'html.parser')

#     df = pd.DataFrame(columns=['언론사','기사','날짜','링크'])

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
#             df=df.append({'언론사':h112,'날짜': aa,'기사':bb1,'링크':cc}, ignore_index=True)

#     st.write(num)  

#     ki = st.sidebar.slider( '기사', 0, num, (0, num))    
#     df1 = df.loc[ki[0]:ki[1], :]

#     sorted_unique_team = sorted(df1.언론사.unique())
#     selected = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
        
#     df2 = df1[df1.언론사.isin(selected)]

#     st.write(df2) 

#     for h, i,j,k in zip(df2['언론사'], df2['날짜'],df2['기사'],df2['링크']):
#         st.write(h," = = ",i,"=====",j,"<br>",k)
        

# if __name__ == '__main__':
#     main()
