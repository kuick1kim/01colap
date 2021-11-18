font = 'https://github.com/kuick1kim/01colap/raw/main/NanumBarunGothic.ttf'
import matplotlib.pyplot as plt
import pandas as pd

from konlpy.tag import Okt
from wordcloud import WordCloud
import nltk
import streamlit as st


st.title('김민상이 만든 Streamlit')


def main():
    
    

    # 여기는 단순하게 이름이다
    dataset_name = st.sidebar.selectbox(
        'Select Dataset',
        ('BBQ-수원매산세류점', '교촌치킨-매교점', '코리엔탈깻잎두마리치킨')
    )

    st.write(f"## {dataset_name} 워드클라우드 중요단어 보여주기")

    
    #데이터는 여기에서 연결된다. 
    def get_dataset(name):
        data = None
        if name == 'BBQ-수원매산세류점':
            data = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/%EC%9A%94%EA%B8%B0%EC%9A%94-%EA%B6%8C%EC%84%A0%EB%8F%99-BBQ-%EC%88%98%EC%9B%90%EB%A7%A4%EC%82%B0%EC%84%B8%EB%A5%98%EC%A0%90.csv'
        elif name == '교촌치킨-매교점':
            data = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/%EC%9A%94%EA%B8%B0%EC%9A%94-%EA%B6%8C%EC%84%A0%EB%8F%99-%EA%B5%90%EC%B4%8C%EC%B9%98%ED%82%A8-%EB%A7%A4%EA%B5%90%EC%A0%90.csv'
        else:
            data = 'https://raw.githubusercontent.com/kuick1kim/01colap/main/%EC%9A%94%EA%B8%B0%EC%9A%94-%EA%B6%8C%EC%84%A0%EB%8F%99-%EC%BD%94%EB%A6%AC%EC%97%94%ED%83%88%EA%B9%BB%EC%9E%8E%EB%91%90%EB%A7%88%EB%A6%AC%EC%B9%98%ED%82%A8-%EA%B6%8C%EC%84%A0%EC%A0%90.csv'
        X= pd.read_csv(data)        
        
   
        return X
        



    X = get_dataset(dataset_name)
    # st.write('Shape of dataset(데이터 크기):', X.shape) 
    


        
    
    crowled_title=X['댓글']
    

    



    title = "".join(crowled_title)
    filtered_title = title.replace('.', ' ').replace('"',' ').replace(',',' ').replace("'"," ").replace('·', ' ').replace('=',' ').replace('\n',' ')

    tw = Okt()
    tokens_ko = tw.nouns(filtered_title)

    ko = nltk.Text(tokens_ko, name='내 명사')

    new_ko=[]
    for word in ko:
        if len(word) > 1 and word != '단독' and  word != ' ':
            new_ko.append(word)

    ko = nltk.Text(new_ko, name = '기사 내 명사 두 번째')

    data = ko.vocab().most_common(150)

    data = dict(data)

    font = 'https://github.com/kuick1kim/01colap/raw/main/NanumBarunGothic.ttf' #이 친구는 코랩과는 다르다 ㅋㅋㅋㅋ
    wc = WordCloud(font_path=font,\
            background_color="white", \
            width=1000, \
            height=1000, \
            max_words=100, \
            max_font_size=300)
    wc = wc.generate_from_frequencies(data)



    fig = plt.figure()  # 스트림릿에서 plot그리기
    plt.title(f" {dataset_name}")
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot(fig)

    
    data1 = pd.DataFrame(data, index = [0])
    data1=data1.T[:40]
    data2= data1.sort_values(by=0, ascending= False)
    data2


    st.subheader('히스토그램')
    # hist_values = np.histogram(data1[0])#, bins=24, range=(0,24))
    st.bar_chart(data2)
    # 히스토 그램 넣는 방법


    if st.checkbox('여기를 누르면 데이터를 볼수 있어요'):
    # 체크박스를 넣어줌
        st.subheader('짜잔..... 실제데이터 입니다') #글씨 쓰는데
        st.write(X) #실제데이터





if __name__ == '__main__':
    main()
