import streamlit as st
import pandas as pd
import base64
import io
import numpy as np








# 여기는 단순하게 이름이다
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('BBQ', '교촌','페리카나','컬투치킨', '코리엔탈치킨')
)

st.write(f"## {dataset_name} Dataset")



@st.cache
def load_data(name):
    data = None
    if name == 'BBQ':
        DATA_URL =  'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/bbq.csv'
    elif name == '교촌':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/kyochon.csv'
    elif name == '페리카나':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/pericana.csv'
    elif name == '컬투치킨':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/cultwu.csv'
    else:
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/korental.csv'


    data = pd.read_csv(DATA_URL)    
    return data
df = load_data(dataset_name)

##############잘됨####################
df


# def get_pos(x):  
#     r1 = x.split(',')    
#     pos = ['{}'.format(jumun) for jumun in r1 ]    
#     return r1

# from sklearn.feature_extraction.text import CountVectorizer

# # 형태소를 벡터 형태의 학습 데이터셋(X 데이터)으로 변환합니다.
# index_vectorizer = CountVectorizer(tokenizer = lambda x: get_pos(x))
# X = index_vectorizer.fit_transform(df['주문내용'].tolist())
# box=index_vectorizer.get_feature_names()
# dist = np.sum(X, axis=0)
# df_freq = pd.DataFrame(dist, columns=box)
# df_freq_T = df_freq.T.reset_index()
# df_freq_T.columns = ["menu", "frequency"]

# df_freq_T["c_menu"] = df_freq_T["menu"].str.replace("/1", "")

# dft=df_freq_T.sort_values(["frequency"], ascending=False)
# dft= dft[['c_menu','frequency']].reset_index(drop=True)
# dft


