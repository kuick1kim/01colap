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


# Assign plotting style 
# mpl.style.use('seaborn-pastel')
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.size'] = 10.
# plt.rcParams['xtick.labelsize'] = 9.
# plt.rcParams['ytick.labelsize'] = 9.
# plt.rcParams['axes.labelsize'] = 12.
# mpl.rcParams['figure.dpi'] = 300.
#plt.gcf().canvas.renderer.dpi = 300.
# Font loading 
fm.get_fontconfig_fonts()
# font_location = "NGULIM.TTF"
# font_name = fm.FontProperties(fname=font_location).get_name()
# matplotlib.rc('font', family=font_name)





pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)


st.title('Dash Board')

st.markdown("""
이 앱은 통계청 외식산업 경기전망지수 입니다. !!

[통계청 외식산업 경기전망지수 바로가기](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_KRBI_2016_1&conn_path=I2).
""")

st.markdown("""
col	외식업종별 ,0.all	전체소계 ,1.han_all	한식소계 ,1.1han_il	한식 일반 음식점업 ,
1.2han_noo	한식 면요리 전문점 ,1.3han_meat	한식 육류요리 전문점 ,
1.4han_sea	한식 해산물요리 전문점 ,2.for	외국 전체 소계 ,2.1chn	중식 음식점업 ,
2.2jpn	일식 음식점업 ,2.3fff	서양식 음식점업 ,2.4odr	기타 외국식 음식점업 ,
3.gu	구내식당업 소계 ,4.chul	출장음식 소계 ,5.gan_all	간이음식점 소계 ,
5.1brd	제과점업 ,5.2pzz	피자 햄버거 샌드위치 및 유사 음식점업 ,5.3chi	치킨 전문점 
5.4kimb	김밥 및 기타 간이 음식점업 ,5.5dlv	간이 음식 포장 판매 전문점 ,6.alc_all	주점 소계 ,
6.1alc_il	일반 유흥 주점업 ,6.2alc_dn	무도 유흥 주점업 ,6.3alc_bee	생맥주 전문점 ,
6.4alc_ord	기타 주점업 ,7.noal_all	비알콜 음료소계 ,7.1coffee	커피 전문점 ,
7.2noncof	기타 비알콜 음료점업 
""")






st.sidebar.header('외식산업 경기전망지수')


##############잘됨####################
DATA_URL = ('https://github.com/kuick1kim/01colap/main/streamlit/eeee.csv')

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)    
    return data
df = load_data()

##############잘됨####################

##########################성공#여기는 추가넣는부분################################
# spectra = st.file_uploader("ex.csv", type={"csv", "txt", "xlsx"})

# if spectra is not None:
#     df = pd.read_csv(spectra)
# st.write(df)
#########################성공#########################################


df=df.set_index('col')
df=df.transpose()




# Sidebar - Sector selection
sorted_sector_unique = list(df.columns)



selected_sector = st.sidebar.multiselect('선택', sorted_sector_unique, sorted_sector_unique)


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
    csv = dfs2.to_csv(encoding='cp949', index=True, header=True)
    b64 = base64.b64encode(csv.encode()).decode()
    #st.markdown('### **⬇️ Download output CSV File **')
    href = f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">csv 파일 다운로드</a>'    
    st.markdown(href, unsafe_allow_html=True)


        



# #################################################################################
# st.title('')
# st.title('')
# st.title('')
# st.title('')
# st.title('임대비율')
# st.markdown("""
# 이번 앱은 통계청 임차현황에 대한 비율을 알아보는 앱입니다. .  !!

# [통계청 사업장 임차현황 바로가기](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114054_008&vw_cd=MT_ZTITLE&list_id=K2_003_001&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE).
# """)

# st.sidebar.header('임차현황입니다.')

# df = pd.read_excel('./ex1.xlsx', sheet_name='a')

# df = df.astype(str)

# dff1 = df.iloc[2:19,[1,3,5,7]]
# dff1=dff1.set_index('특성별(3)')
# dff1=dff1.transpose()
# # st.dataframe(dff1)
# #선택하기....
# sorted_sector_unique1 = list(dff1.columns)
# selected_sector1 = st.sidebar.multiselect('선택', sorted_sector_unique1, sorted_sector_unique1)







# dffs1 = dff1.loc[:,selected_sector1]
# a1 = len(selected_sector1)


# st.header('선택하신 업종입니다.')

# st.write('왼쪽에서 선택하신 업종의 갯수는 :', a1," 개 입니다. ")
# st.write(str(selected_sector1))



# dffs2= dffs1.astype(float)


# def plot(selected_sector1):
        
#     # plt.legend(selected_sector,loc='center left', bbox_to_anchor=(1, 0.5))
#     for i in selected_sector1:        
#         plt.plot(dffs2.index, dffs2.loc[:,i], label=i,alpha=0.8)   
#         plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))       
#     plt.xticks(rotation=50)
    
#     return st.pyplot()

# plot(selected_sector1)


# if st.checkbox('여기를 누르면 데이터를 볼 수 있습니다.1 '):
#     # 체크박스를 넣어줌
#     st.subheader('짜잔..... 당신이 선택한 데이터입니다. ') #글씨 쓰는데
#     dfs2=pd.DataFrame(dffs2)    
#     st.table(dffs2) #실제데이터

#     towrite = io.BytesIO()
#     downloaded_file = dffs2.to_excel(towrite, encoding='utf-8', index=True, header=True)
#     towrite.seek(0)  # reset pointer
#     b64 = base64.b64encode(towrite.read()).decode()  # some strings
#     linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="2021외식업 임대비율.xlsx">위에 보이는 데이터를 엑셀로 다운로드 받아봅니다. </a>'
#     st.markdown(linko, unsafe_allow_html=True)

