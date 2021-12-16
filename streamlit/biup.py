
import pandas as pd
import streamlit as st



DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/up.csv')
             
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()


#st.markdown("![Foo](https://lh3.googleusercontent.com/proxy/arX8KAzc-yfz5Pw67IQ6o86FkebTfFh-PVALs2N9ZwYCYp0BHe3kowCRhtIz_VuxMtp9nBdwP5bk3U7gxIrVw7rMs1XOjk3_1LpDhwEmIIjoE8SXLDbpvHE)")


st.write(df) 
##########################################################################
towrite = io.BytesIO()
downloaded_file = df.to_excel(towrite, encoding='utf-8', index=True, header=True)
towrite.seek(0)  # reset pointer
b64 = base64.b64encode(towrite.read()).decode()  # some strings
linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="전체보기.xlsx">자료 다운받기</a>'
st.markdown(linko, unsafe_allow_html=True)
#===============================인코딩이 안되서 csv를 안씀================================




akiml= len(df)
many = st.slider('몇번째 회사인지 선택해 주세요',  0, akiml-1, 0)

many=int(many)

st.write(many) 

df1= df.iloc[many, :]

st.write(df1) 


   

st.title(df1['client']) 
st.write("지역",'　:　',df1['지역'],'　　　', '산업','　:　',df1['산업'])
st.header(df1['Headline'])


df2= df1['경험담k.1']
df2= df2.split("#####")
for a in df2:
  st.header(a)
  st.write()
  
st.write()
st.write()
st.header("효과")
st.write(df1['key Benefits']) 

df3= df1['story_k.1']
df3= df3.split("#####")
for b in df3:
  st.write(b)
  st.write()
  st.write()
  st.write()

