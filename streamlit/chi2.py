import streamlit as st
import pandas as pd
import base64
import io
import numpy as np
import altair as alt
from PIL import Image


# 여기는 단순하게 이름이다
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('BBQ', '처가집','후라이드참잘하는집', '네네치킨','교촌', '코리엔탈치킨')
)

st.write(f"## {dataset_name} Dataset")



@st.cache
def load_data(name):
    data = None
    if name == 'BBQ':
        DATA_URL =  'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/bbq.csv'
    elif name == '처가집':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/cheogajip.csv'
    elif name == '후라이드참잘하는집':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/friedgood.csv'
    elif name == '네네치킨':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/nene.csv'
    elif name == '교촌':
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/kyochon.csv'       
    else:
        DATA_URL = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/korental.csv'


    data = pd.read_csv(DATA_URL)    
    return data





df = load_data(dataset_name)



mat = st.sidebar.slider(    '맛',    0, 5, (0, 5))
yang = st.sidebar.slider(    '양',    0, 5, (0, 5))
bae = st.sidebar.slider(    '배달',    0, 5, (0, 5))

mask1 = (df['맛'] >= mat[0]) & (df['맛'] <= mat[1])
df1 = df.loc[mask1, :]

mask2 = (df1['양'] >= yang[0]) & (df1['양'] <= yang[1])
df2 = df1.loc[mask2, :]

mask3 = (df2['배달'] >= bae[0]) & (df2['배달'] <= bae[1])
df3 = df2.loc[mask3, :]

df=df3
df

dfk=df.sort_values(by='time', ascending=0)
dfk['time']
# st.bar_chart(dfk['time'])









# df['주문내용']=df['주문내용'].fillna('주문내용없음')
# ##############잘됨####################
# if st.checkbox('여기를 누르면 로딩된 데이터를 볼 수 있습니다. '):
#     # 체크박스를 넣어줌
    
#     df


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
# dft1= dft.iloc[0:30,:]




# st.title(f" 위의 조건으로 {dataset_name} 에서 시킨 메뉴 보기")

# st.write(alt.Chart(dft1).mark_bar().encode(
# #     x=alt.X('frequency', sort=None),
# #     y='c_menu',
#     y=alt.X('c_menu', sort=None),
#     x='frequency',
# ))


# if st.checkbox('맨뒤에 데이터까지 보시려면 여기를 눌러주세요 '):
#     # 체크박스를 넣어줌  
#     dft

# df1= df.sort_values(by='사진주소',ascending=1)
# df1
# df1=df1[:10]
# # df2=df1['댓글'][:10]
# st.title("고객이 올려준 이미지 확인하기")
# count =1
# for i,j in zip(df1['사진주소'],df2['댓글']):
#     original_title = '<p style="color:#FF4000; font-size: 14px;">손님이 올려준 {c}번째 사진 // {j}</p>'.format(c=count,j=j)        
#     st.markdown(original_title, unsafe_allow_html=True)
#     count +=1
#     try:
#         st.image(i, width=600)
#     except:
#         pass
#         #st.image(i, width=600)
# #################################################################





