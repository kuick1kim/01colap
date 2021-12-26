import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


def main():
    st.header('언론사별 주요뉴스 ')
    date = st.text_input('날짜를 넣어주세요.. 자료가 없을수도 있어요. ex)20210324')
    news_url = 'https://news.naver.com/main/ranking/popularDay.nhn?date={}'.format(date)

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    req = requests.get(news_url, headers = headers)

    soup = BeautifulSoup(req.text, 'html.parser')

    df = pd.DataFrame(columns=['언론사','기사','날짜','링크'])

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
            df=df.append({'언론사':h112,'날짜': aa,'기사':bb1,'링크':cc}, ignore_index=True)

    st.write(num)  

    ki = st.sidebar.slider( '기사', 0, num, (0, num))    
    df1 = df.loc[ki[0]:ki[1], :]
    
    unlonsa = st.sidebar.text_input("검색하고 싶은 언론사를 넣어주세요",'조선')
    
    df2 = df1[df1['언론사'].str.contains(unlunsa)].copy()

#     sorted_unique_team = sorted(df1.언론사.unique())
#     selected = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
        
#     df2 = df1[df1.언론사.isin(selected)]

    st.write(df2) 

    for h, i,j,k in zip(df2['언론사'], df2['날짜'],df2['기사'],df2['링크']):
        st.write(h," = = ",i,"=====",j,"<br>",k)
        

if __name__ == '__main__':
    main()
