import streamlit as st
import pandas as pd



import pandas as pd
import streamlit as st
##########################성공#여기는 추가넣는부분################################
# spectra = st.file_uploader("ex.csv", type={"csv", "txt", "xlsx"})
# if spectra is not None:
#     df = pd.read_csv(spectra)
# st.write(df)
#########################성공#########################################








import base64

import io
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.style
import matplotlib as mpl


plt.rcParams['axes.unicode_minus'] = False

fm.get_fontconfig_fonts()

pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)


st.title('Dash Board')

st.markdown("""
이 앱은 통계청 외식산업 경기전망지수 입니다. !!

[통계청 외식산업 경기전망지수 바로가기](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_KRBI_2016_1&conn_path=I2).
""")







st.sidebar.header('외식산업 경기전망지수')


##############잘됨####################
DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/streamlit/ex.csv')

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()

##############잘됨####################




df=df.set_index('외식업종별')
df=df.transpose()




# Sidebar - Sector selection
sorted_sector_unique = list(df.columns)


llist=['전체소계',  '치킨 전문점']
selected_sector = st.sidebar.multiselect('선택', sorted_sector_unique, llist)


dfs = df.loc[:,selected_sector]
a = len(selected_sector)


st.header('선택하신 업종입니다.')

st.write('왼쪽에서 선택하신 업종의 갯수는 :', a," 개 입니다. ")
st.write(str(selected_sector))



dfs1=dfs[:]
#################새로운 그래프##########################
chart_data = pd.DataFrame(dfs1,columns=selected_sector)
st.line_chart(chart_data)

################### 과거에 사용한것 ##########################
# def plot(selected_sector):
    
#     dfs1['Date'] = dfs1.index
    
#     for i in selected_sector:      
        
#         plt.plot(dfs1.Date, dfs1.loc[:,i], label=i,alpha=0.8)   
#         plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))       
#     plt.xticks(rotation=50)
    
#     return st.pyplot()

#plot(selected_sector)
#############################################################



if st.checkbox('여기를 누르면 데이터를 볼 수 있습니다. '):
    # 체크박스를 넣어줌
    st.subheader('짜잔..... 당신이 선택한 데이터입니다. ') #글씨 쓰는데
    dfs2=pd.DataFrame(dfs)    
    st.table(dfs2) #실제데이터

    # Download S&P500 data
    # https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
    towrite = io.BytesIO()
    downloaded_file = dfs2.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()  # some strings
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="2021외식업.xlsx">위에 보이는 데이터를 엑셀로 다운로드받기</a>'
    st.markdown(linko, unsafe_allow_html=True)
    #===============================인코딩이 안되서 csv를 안씀================================
#     csv = dfs2.to_csv(encoding='cp949', index=True, header=True)
#     b64 = base64.b64encode(csv.encode()).decode()
#     #st.markdown('### **⬇️ Download output CSV File **')
#     href = f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">csv 파일 다운로드</a>'    
#     st.markdown(href, unsafe_allow_html=True)



# #################################################################################
# #################################################################################        
# #################################################################################







# #################################################################################
# #################################################################################
# #################################################################################
st.title('')
st.title('')
st.title('')
st.title('')
st.title('임대비율')
st.markdown("""
이번 앱은 통계청 임차현황에 대한 비율을 알아보는 앱입니다. .  !!

[통계청 사업장 임차현황 바로가기](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114054_008&vw_cd=MT_ZTITLE&list_id=K2_003_001&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE).
""")

st.sidebar.header('임차현황입니다.')

##############잘됨####################
DATA_URL = ('https://raw.githubusercontent.com/kuick1kim/01colap/main/streamlit/ex2.csv')

@st.cache
def load_data():
    try:
        data = pd.read_csv(DATA_URL)    
    except:
        data = pd.read_excel(DATA_URL)
    return data
df = load_data()

##############잘됨####################



df = df.astype(str)

dff1 = df.iloc[2:19,[1,3,5,7]]
dff1=dff1.set_index('특성별(3)')
dff1=dff1.transpose()
# st.dataframe(dff1)
#선택하기....
sorted_sector_unique1 = list(dff1.columns)

lllist = ['전체', '치킨전문점']
selected_sector1 = st.sidebar.multiselect('선택', sorted_sector_unique1, lllist)







dffs1 = dff1.loc[:,selected_sector1]
a1 = len(selected_sector1)


st.header('선택하신 업종입니다.')

st.write('왼쪽에서 선택하신 업종의 갯수는 :', a1," 개 입니다. ")
st.write(str(selected_sector1))



dffs2= dffs1.astype(float)


#################새로운 그래프##########################
chart_data = pd.DataFrame(dffs2,columns=selected_sector1)
st.line_chart(chart_data)

################### 과거에 사용한것 ##########################




################지워버림######################
# def plot(selected_sector1):
        
#     # plt.legend(selected_sector,loc='center left', bbox_to_anchor=(1, 0.5))
#     for i in selected_sector1:        
#         plt.plot(dffs2.index, dffs2.loc[:,i], label=i,alpha=0.8)   
#         plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))       
#     plt.xticks(rotation=50)
    
#     return st.pyplot()

# plot(selected_sector1)
#######################################

if st.checkbox('여기를 누르면 데이터를 볼 수 있어요 '):
    # 체크박스를 넣어줌
    st.subheader('짜잔..... 당신이 선택한 데이터입니다. ') #글씨 쓰는데
    dfs2=pd.DataFrame(dffs2)    
    st.table(dffs2) #실제데이터

    towrite = io.BytesIO()
    downloaded_file = dffs2.to_excel(towrite, encoding='utf-8', index=True, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()  # some strings
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="2021외식업 임대비율.xlsx">위에 보이는 데이터를 엑셀로 다운로드 받아봅니다. </a>'
    st.markdown(linko, unsafe_allow_html=True)


    
st.sidebar.header('')
st.sidebar.header('') 
st.sidebar.markdown("""

[요기요 데이터 가기](https://share.streamlit.io/kuick1kim/01colap/main/streamlit/chi2.py/).
""")

