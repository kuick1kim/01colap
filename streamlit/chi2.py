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



#############################################################
freq = df.groupby(['time']).count()
freq = freq.reset_index(inplace=False)
freq = freq[['time','지역']].sort_values(by='time',ascending=1)
st.write(alt.Chart(freq).mark_bar().encode(
    x=alt.X('time', sort='-x'),
    y='지역'
))
##############################################################
df







df['주문내용']=df['주문내용'].fillna('주문내용없음')
##############잘됨####################
if st.checkbox('여기를 누르면 로딩된 데이터를 볼 수 있습니다. '):
    # 체크박스를 넣어줌
    
    df


def get_pos(x):  
    r1 = x.split(',')    
    pos = ['{}'.format(jumun) for jumun in r1 ]    
    return r1

from sklearn.feature_extraction.text import CountVectorizer
##################################################################################
# 형태소를 벡터 형태의 학습 데이터셋(X 데이터)으로 변환합니다.
index_vectorizer = CountVectorizer(tokenizer = lambda x: get_pos(x))
X = index_vectorizer.fit_transform(df['주문내용'].tolist())
box=index_vectorizer.get_feature_names()
dist = np.sum(X, axis=0)
df_freq = pd.DataFrame(dist, columns=box)
df_freq_T = df_freq.T.reset_index()
df_freq_T.columns = ["menu", "frequency"]

df_freq_T["c_menu"] = df_freq_T["menu"].str.replace("/1", "")

dft=df_freq_T.sort_values(["frequency"], ascending=False)
dft= dft[['c_menu','frequency']].reset_index(drop=True)
dft1= dft.iloc[0:15,:]


# ======
st.title(f" 위의 조건으로 {dataset_name} 에서 시킨 메뉴 보기")
st.write(alt.Chart(dft1).mark_bar().encode(
#     x=alt.X('frequency', sort=None),
#     y='c_menu',
    y=alt.X('c_menu', sort=None),
    x='frequency',
))
# ========
if st.checkbox('맨뒤에 데이터까지 보시려면 여기를 눌러주세요 '):
    # 체크박스를 넣어줌  
    dft

##################################################################################






def get_pos(x):  
    r1 = x.split(',')    
    pos = ['{}'.format(jumun) for jumun in r1 ]    
    return r1
index_vectorizer = CountVectorizer(tokenizer = lambda x: get_pos(x))
XN = index_vectorizer.fit_transform(df['Noun'].tolist())
box=index_vectorizer.get_feature_names()
dist = np.sum(XN, axis=0)
df_freq = pd.DataFrame(dist, columns=box)
df_freq_T = df_freq.T.reset_index()
df_freq_T.columns =["명사1", "갯수"]
df_freq_T["명사"] = df_freq_T["명사1"].str.replace("]", "").str.replace("[", "").str.replace("'", "")
dftn=df_freq_T.sort_values(["갯수"], ascending=False)
dftn= dftn[['명사','갯수']].reset_index(drop=True)
dftn1= dftn.iloc[0:15,:]


# ==============
st.title(f" 위의 조건으로 제일 많이 나온 형태소 빈도")

st.write(alt.Chart(dftn1).mark_bar().encode(
#     x=alt.X('갯수', sort=None),
#     y='c_menu',
    y=alt.X('명사', sort=None),
    x='갯수',
))

#######################동사/ 형용사############################
a=[]
df2=df['Verb'].fillna("")
for k in df2:
    try:
        k=k.astype(str)
    except:
        pass
    b=k.split(',')    
    for c in b:
        if c != '':
            a.append(c)
a  = pd.DataFrame(a)
XN = index_vectorizer.fit_transform(a[0].tolist())
box=index_vectorizer.get_feature_names()
dist = np.sum(XN, axis=0)
df_freq = pd.DataFrame(dist, columns=box)
df_freq_T = df_freq.T.reset_index()
df_freq_T.columns = ["동사1", "갯수"]
df_freq_T["동사"] = df_freq_T["동사1"].str.replace("]", "").str.replace("[", "").str.replace("'", "")
dftv=df_freq_T.sort_values(["갯수"], ascending=False)
dftv= dftv[['동사','갯수']].reset_index(drop=True)
# dftv



#####################################################






################
if st.checkbox('추가 형태소 빈도 보기'):
    dftt= pd.concat([dftn,dftv], axis=1)
    dftt
# ==============



dfi= df.sort_values(by='사진주소',ascending=0)

dfi=dfi[:10]

st.title("고객이 올려준 이미지 확인하기")
count =1
for i,j in zip(dfi['사진주소'],dfi['댓글']):
    original_title = '<p style="color:#FF4000; font-size: 14px;">손님이 올려준 {c}번째 사진 // {j}</p>'.format(c=count,j=j)        
    st.markdown(original_title, unsafe_allow_html=True)
    count +=1
    try:
        st.image(i, width=500)
    except:
        pass
        
#################################################################





