import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                   'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
                
#데이타를 가져오는것

@st.cache
def load_data(nrows):
  data = pd.read_csv(DATA_URL, nrows=nrows)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  return data





data_load_state = st.text('Loading data...로딩중이니까 기대리라')
data = load_data(10000)
# 로드데이터에 몇개의 데이터를 넣을래

data_load_state.text("Done 다했다! (using st.cache)")



if st.checkbox('Show raw data'):
    # 체크박스를 넣어줌
    st.subheader('Raw data')
    st.write(data)



# 이 아래것이다. 
# Some number in the range 0-23

hour_to_filter1 = st.slider('Select a range of values', 0, 23, (2, 17))
st.write('Values:', hour_to_filter1)


# hour_to_filter1 = st.slider('hour 시간바꿔줌', 0, 23, 15)
filtered_data1 = data[data[DATE_COLUMN].dt.hour == hour_to_filter1]
# 시간으로 변경해주는 명령 여러시간에 걸치지 않음
# 요거슨 필터





st.subheader('이름을 바꿔줌111 맨위에 히스토그램 %s 시에' % hour_to_filter1)
# 제목
hist_values = np.histogram(data[DATE_COLUMN].dt.hour == hour_to_filter1,bins=24, range=(0,24))[0]
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour , bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
# 히스토 그램 넣는 방법



# 이 아래것이다. 
# Some number in the range 0-23
hour_to_filter = st.slider('hour 시간바꿔줌', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# 요거슨 필터

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)








# 아래에다가 막 붙여봄







st.subheader('이름을 바꿔줌111 맨위에 히스토그램')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
# 히스토 그램 넣는 방법


st.subheader('이름을 바꿔줌111 맨위에 히스토그램')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
# 히스토 그램 넣는 방법


st.subheader('이름을 바꿔줌111 맨위에 히스토그램')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
# 히스토 그램 넣는 방법


st.subheader('이름을 바꿔줌111 맨위에 히스토그램')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
# 히스토 그램 넣는 방법


st.subheader('이름을 바꿔줌111 맨위에 히스토그램')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
# 히스토 그램 넣는 방법



st.subheader('이름을 바꿔줌111 맨위에 히스토그램')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
# 히스토 그램 넣는 방법
