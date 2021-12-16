
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
many = st.sidebar.slider('회사',  0, akiml, 0)

many=int(many)

st.write(many) 

df1= df.iloc[many, :]


st.write(df1) 

st.write(df1['client']) 

df2= df1['경험담k.1']
df2= df2.split("#####")
for a in df2:
  st.write(a)
  st.write()
  
  
  
df3= df1['story_k.1']
df3= df3.split("#####")
for b in df3:
  st.write(b)
  st.write()
  st.write()

