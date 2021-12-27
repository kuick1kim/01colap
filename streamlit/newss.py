
import streamlit as st
import pandas as pd


st.sidebar.markdown("""
[자료 다운받기 사이트로 이동하기](https://share.streamlit.io/kuick1kim/01colap/main/streamlit/naver_news.py/)
""")


########################여기는 추가넣는부분##############



uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine='openpyxl')
#     st.dataframe(df)
else:
    df=''
    st.write('파일을 넣어주세요')


#########################성공###########################

llll = len(df)


many = st.slider('기간',  0, llll, (0, llll))
df1 = df.iloc[many[0]:many[1],:]



# cate = st.text_input("검색하고 싶은 언론사를 넣어주세요",'')    
# df3 = df1[df1["category"].str.contains(cate)].copy()

df1
# kiki = st.sidebar.text_input("검색하고 싶은 기사단어를 넣어주세요",'')    
# df2 = df3[df3['기사'].str.contains(kiki)].copy()



# for h, i,j,k,kk in zip(df3["날짜"], df3['category'],df3['제목'],df3['링크'],df3['내용']):
#             st.write(i," = = ",h)
#             st.write(j)
#             st.write(k)
#             st.write(kk)



