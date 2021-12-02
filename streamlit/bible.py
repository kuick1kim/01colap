
import pandas as pd
import streamlit as st
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)

st.markdown("""
[AWS로 돌아가기](http://18.118.243.103:8080/)
""")

DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/bible.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()



word = st.text_input("검색하고 싶은 말씀을 넣어주세요",'엘리사')
df1 = df[df["말씀"].str.contains(word)].copy()

bible = st.text_input("성경을 넣어주세요/(백스페이스 아래 '|' 마크를 넣으시면 중복 검색됩니다. ) ",'열왕기')
df2 = df1[df1["성경"].str.contains(bible)].copy()

bible1 = st.text_input("장수를 넣어주세요")
df3 = df2[df2["장"]=='bible1'].copy()
st.write(df1) 
st.write(df2) 
st.write(df3) 

for kk , ll ,pp,oo in zip(df3['말씀'], df3['성경'], df3['장'], df3['절']):
    aa= str(ll) +" "+str(pp)+'-'+str(oo)
    st.write(aa)
    st.write(kk)
    
    

