
import pandas as pd
import streamlit as st


DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/up.csv')
             
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()

# st.title("주 예수를 믿으라 그리하면 너와 네 집이 구원을 받으리라.") 
st.title("Uipath 성공사례.")
st.write('Uipath 성공사례를 website에서 번역하여 수집하였습니다. ') 
st.write(df) 

n= len(df)



num = st.slider('몇번째 회사를 볼까요?', 0, n-1, 2)






dfa= df.iloc[num,:]


st.write(dfa) 

d= dfa['client']
st.header(d)

st.write('{aa}'.format(aa=dfa['Headline']))
st.header('Success story')

a=dfa['경험담k.1']
a= a.split("#####")
for b in a:
  c= b.replace("@@",'\n-----').replace("/////",'-----')
  st.write(c)
  st.write('')
  
  
  
st.header('Full story')
  
a1=dfa['story_k.1']
a1= a1.split("#####")
for b1 in a1:
  st.write(b1)
  st.write('')


# ['client', '지역', '산업', 'Headline', 'Client Overview', 'process type',
#        'key Benefits', '경험담', 'story', '경험담k', 'story_k', 'img', '경험담k.1',
#        'story_k.1']


##################################################################################

# DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/bible.csv')
# @st.cache
# def load_data():
#     data = pd.read_csv(DATA_URL)    
#     return data
# df = load_data()



# word = st.text_input("검색하고 싶은 성경 말씀을 넣어주세요",'주 예수를 믿으라 그리하면 너와 네 집이 구원을 받으리라 ')
# df1 = df[df["말씀"].str.contains(word)].copy()

# bible = st.text_input("성경을 넣어주세요/(백스페이스 아래 '|' 마크를 넣으시면 중복 검색됩니다. ) ",'')
# df2 = df1[df1["성경"].str.contains(bible)].copy()

# bible1 = st.text_input("장수를 넣어주세요")

# if bible1 != "":    
#     bible1 = int(bible1)
#     df2 = df2[df2["장"]==bible1].copy()

    
# st.write(df2) 

# for kk , ll ,pp,oo in zip(df2['말씀'], df2['성경'], df2['장'], df2['절']):
#     aa= str(ll) +" "+str(pp)+'-'+str(oo)
#     st.write(aa)
#     st.write(kk)
    
    
