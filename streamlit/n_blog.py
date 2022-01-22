import streamlit as st
import pandas as pd


dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('블로그 검색1', '블로그 검색2')
)

@st.cache
def load_data(name):
    data = None
    if name == '블로그 검색1':
        DATA_URL= kms()        
    elif name == '블로그 검색2':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.csv'        
    else:
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/cheogajip.csv'

    data = pd.read_csv(DATA_URL)   
    return data
    
def kms():
    a =  'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.csv'       
    return a

df = load_data(dataset_name)

list = st.sidebar.slider( '선택하세요',0, len(df)-1, 5)
st.write(list)
df1 = df.iloc[list:list+1, :]

dfs = pd.DataFrame(columns=['내용'])

for i in df1['내용']:
    hh1=i.split('\t')
    a=1
    for nn in hh1:
        if nn is not None or nn != " " or nn != "" :
            nn1= nn+'//'+str(a)            
            a=a+1
            dfs=dfs.append({'내용':nn1}, ignore_index=True)

    
word = st.sidebar.text_input("검색하고 싶은 단어를 넣으세요",'')
dfs2 = dfs[dfs["내용"].str.contains(word)].copy()
dfs2
for i in dfs2:
    st.write(i)


        
        
        
        


