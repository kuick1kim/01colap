
import pandas as pd
import streamlit as st


DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/up.csv')
             
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()
st.write(df) 
akiml= len(df)
many = st.sidebar.slider('몇번째 회사인지 선택해 주세요',  0, akiml, 0)

many=int(many)

st.write(many) 

df1= df.iloc[many, :]


st.write(df1) 

# try:
a= df1['img']
st.write(a)

# st.image(a)
   

st.title(df1['client']) 
st.write("지역",'　:　',df1['지역'],'　　　', '산업','　:　',df1['산업'])
st.header(df1['Headline'])


df2= df1['경험담k.1']
df2= df2.split("#####")
for a in df2:
  st.header(a)
  st.write()
  
st.write(df1['key Benefits']) 

df3= df1['story_k.1']
df3= df3.split("#####")
for b in df3:
  st.write(b)
  st.write()
  st.write()
  st.write()

