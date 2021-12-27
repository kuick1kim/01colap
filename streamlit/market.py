import streamlit as st
import pandas as pd
import base64
import io




df = pd.read_csv('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/uboyul.csv')#, engine='openpyxl')




cate1 = st.sidebar.text_input("업종1을 검색하세요",'')    
df1 = df[df["업종1"].str.contains(cate1)].copy()

df2=df1


if st.sidebar.button('2020 매출액 높은순'):
    df2=df1.sort_values(by="매출2020", ascending=False )

if st.sidebar.button('2016대비성장 높은순'):
    df2=df1.sort_values(by="4년전대비", ascending=False )

if st.sidebar.button('2018대비성장 높은순'):
    df2=df1.sort_values(by="2년전대비", ascending=False )


if st.sidebar.button('per 높은순'):
    df2=df1.sort_values(by="per", ascending=False )

if st.sidebar.button('유보율 높은순'):
    df2=df1.sort_values(by="유보율20", ascending=False )

if st.sidebar.button('연매출/시가총액'):
    df2=df1.sort_values(by="매출시총", ascending=False )

lll = len(df2)
ki = st.sidebar.slider( '몇개 회사만 보기', 0, lll, (0, lll))    
df3 = df2.iloc[ki[0]:ki[1], :]
lll1 = len(df3)

towrite = io.BytesIO()
downloaded_file = df3.to_excel(towrite, encoding='utf-8', index=True, header=True)
towrite.seek(0)  # reset pointer
b64 = base64.b64encode(towrite.read()).decode()

linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="market.xlsx">내가 검색한 자료 다운받기</a>'
st.markdown(linko, unsafe_allow_html=True)





df3

st.write(lll1,' 개의 기업 입니다. ',)


