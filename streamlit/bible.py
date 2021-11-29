
import pandas as pd
import streamlit as st
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)



DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/bible.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()



word = st.text_input("검색하고 싶은 말씀을 넣어주세요",'엘리사')
df5 = df[df["말씀"].str.contains(word)].copy()

bible = st.text_input("성경을 넣어주세요/(백스페이스 아래 '|' 마크를 넣으시면 중복 검색됩니다. ) ",'열왕기')
df4 = df5[df5["성경"].str.contains(bible)].copy()

st.write(df4) 

for kk , ll ,pp,oo in zip(df4['말씀'], df4['성경'], df4['장'], df4['절']):
    aa= str(ll) +" "+str(pp)+'-'+str(oo)
    st.write(aa)
    st.write(kk)
    
    
st.sidebar.title('')
st.sidebar.title('')
st.sidebar.markdown("""
[AWS로 돌아가기](http://18.118.243.103:8080/)
""")
