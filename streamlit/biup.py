
import pandas as pd
import streamlit as st


DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/up.csv')
             
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()

akiml= len(df)
many = st.sidebar.slider('회사',  0, akiml, 0)

many=int(many)

st.write(many) 

df1= df.iloc[many, :]


st.write(df1) 





# jang = st.text_input("특정 성경을 넣어주세요/ 안넣으시면 전체 검색 입니다. ",'누가')


# df4 = df[df["성경"].str.contains(jang)].copy()

# word = st.text_input("검색하고 싶은 말씀을 넣어주세요",'사랑')
# df5 = df4[df4["말씀"].str.contains(word)].copy()
# st.write(df5) 

# for kk , ll ,pp,oo in zip(df5['말씀'], df5['성경'], df5['장'], df5['절']):
#     aa= str(ll) +" "+str(pp)+'-'+str(oo)
#     st.caption(aa)
#     st.caption(kk)
    
