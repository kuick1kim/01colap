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
        DATA_URL='https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.xlsx'
        data = pd.read_csv(DATA_URL)  
    else:
        DATA_URL= kms()        
        data = pd.read_csv(DATA_URL)     
    return data
    
def kms():
    a = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/csv/blog2.csv'  
    df = pd.read_csv(a)  
    
#     spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
#     if spectra is not None:
#         df = pd.read_csv(spectra)
    list = st.sidebar.slider( '선택하세요',0, len(df)-1, 5)
    st.write(list)
    df1 = df.iloc[list:list+1, :]


    for i,j in zip(df1['내용'],df1['링크']):
        st.write(j)
        hh1=i.split('\t')
        a=1
        for nn in hh1:
            if nn is not None or nn != " " or nn != "" :                
                st.write(nn)
                a=a+1
    

# df = load_data(dataset_name)

# spectra = st.file_uploader(" ", type={"csv", "txt", "xlsx"})
# if spectra is not None:
#     df = pd.read_csv(spectra)
# #     dataset_name='외부데이터' 




# list = st.sidebar.slider( '선택하세요',0, len(df)-1, 5)
# st.write(list)
# df1 = df.iloc[list:list+1, :]


# for i,j in zip(df1['내용'],df1['링크']):
#     st.write(j)
#     hh1=i.split('\t')
#     a=1
#     for nn in hh1:
#         if nn is not None or nn != " " or nn != "" :                
#             st.write(nn)
#             a=a+1
         

    



        
        
        
        


