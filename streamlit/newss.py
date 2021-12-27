
import streamlit as st
import pandas as pd


st.sidebar.markdown("""
[자료 다운받기 사이트로 이동하기](https://share.streamlit.io/kuick1kim/01colap/main/streamlit/naver_news.py/)
""")


########################여기는 추가넣는부분##############

st.title('블로그 분석기')

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine='openpyxl')
#     st.dataframe(df)
else:
    df=''
    st.write('파일을 넣어주세요')


#########################성공###########################

llll = len(df)


many = st.sidebar.slider('기간',  0, llll, (0, llll))
df1 = df.iloc[many[0]:many[1],:]



cate1 = st.sidebar.text_input("분야1 넣어주세요",'')    
df3 = df1[df1["분야1"].str.contains(cate1)].copy()

cate2 = st.sidebar.text_input("검색내용 넣어주세요",'')    
df4 = df3[df3["내용"].str.contains(cate2)].copy()

df4


for h,i,j,k,kk,kkk in zip(df4["날짜"], df4['블로거'],df4['분야1'],df4['제목'],df4['링크'],df4['내용']):
            st.write(i," = = ",h," = = ",j)
            st.header(k)
            st.write(kk)
            st.write(kkk)



