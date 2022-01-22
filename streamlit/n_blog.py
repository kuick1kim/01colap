import streamlit as st
import pandas as pd


dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('BBQ', '처가집','후라이드참잘하는집', 'BHC','교촌', '코리엔탈치킨')
)

@st.cache
def load_data(name):
    data = None
    if name == 'BBQ':
        DATA_URL =  'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/bbq.csv'
    elif name == '처가집':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/cheogajip.csv'
    elif name == '후라이드참잘하는집':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/friedgood.csv'
    elif name == 'BHC':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/nene.csv'
    elif name == '교촌':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/kyochon.csv'       
    else:
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/korental.csv'

    data = pd.read_csv(DATA_URL)    
    return data
df = load_data(dataset_name)

df
        
        
        
        
        
        
        




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
    
