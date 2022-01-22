import streamlit as st
import pandas as pd

DATA_URL = pd.read_csv('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.csv')

########################여기는 추가넣는부분##############
spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
if spectra is not None:
    DATA_URL = pd.read_csv(spectra)
    dataset_name='외부데이터' 
#########################성공###########################



dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('블로그 검색1','블로그 검색2')
)

def get_dataset(name):
    if name == '블로그 검색1':          
        df = load_data()
    elif name == '블로그 검색2':
        df = load_data()
    else:
        blog1()


DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/up.csv')
             
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data


st.write(df) 

        
        
        
        
        
        
        
        




# # df= pd.read_csv('c:/123kms/성경전체.csv')


# word = st.text_input("검색하고 싶은 말씀을 넣어주세요",'엘리사')
# df5 = df[df["말씀"].str.contains(word)].copy()



# bible = st.text_input("성경을 넣어주세요/(백스페이스 아래 '|' 마크를 넣으시면 중복 검색됩니다. ) ",'열왕기')
# df4 = df5[df5["성경"].str.contains(bible)].copy()

# # jang = st.text_input("특정 장수가 보고 싶으시면 넣어주세요")
# # df44 = df4[df4["장"].str.count(jang)].copy()
# # df44



# st.write(df4) 

# for kk , ll ,pp,oo in zip(df4['말씀'], df4['성경'], df4['장'], df4['절']):
#     aa= str(ll) +" "+str(pp)+'-'+str(oo)
#     st.write(aa)
#     st.write(kk)
    
