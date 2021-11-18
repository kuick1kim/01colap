

import streamlit as st 
import numpy as np 

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score







st.title('머신러닝 할수 있는 모형 만들기')

st.write("""
# Explore different classifier and datasets
Which one is the best?
다른 학습을 하려고하면 어떤 것이 베스트 모델인가
""")


# 여기는 단순하게 이름이다
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Iris', 'Breast Cancer', 'Wine')
)




st.write(f"## {dataset_name} Dataset")

classifier_name = st.sidebar.selectbox(
    'Select classifier',
    ('KNN', 'SVM', 'Random Forest')
)



#데이터는 여기에서 연결된다. 
def get_dataset(name):
    data = None
    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    X = data.data
    y = data.target
    return X, y



X, y = get_dataset(dataset_name)
st.write('Shape of dataset(데이터 크기):', X.shape) 
st.write('number of classes(클래스의 넘버):', len(np.unique(y)))







def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'SVM':

        C = st.sidebar.slider('C', 0.01, 10.0) #범위를 만든다
        params['C'] = C
    elif clf_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15) #범위를 만든다
        params['K'] = K
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)# 최대깊이를 선택함
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)#파라메터 선택
        params['n_estimators'] = n_estimators
    return params

params = add_parameter_ui(classifier_name)





# 이거는 이거다 공부시키는 여러가지 방법
# 몇개더 추가할수도 있음

def get_classifier(clf_name, params):
    clf = None
    if clf_name == 'SVM':
        clf = SVC(C=params['C'])
    elif clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'], 
            max_depth=params['max_depth'], random_state=1234)
    return clf








clf = get_classifier(classifier_name, params)
#### CLASSIFICATION ####

# 이것이 clf가 되는 것이다 .



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)







clf.fit(X_train, y_train)



y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)

st.write(f'## Classifier(모델명) = {classifier_name}')#여기다가 
st.write(f'## Accuracy(정확도) =', acc)




# 여기까지 끝나버림 
# 이후부터는 그래프를 보는것



#### PLOT DATASET ####
# Project the data onto the 2 primary principal components


pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2,
        c=y, alpha=0.5,
        cmap='viridis')

plt.xlabel('Principal Component(중요요소) 1')
plt.ylabel('Principal Component(중요요소) 2')
plt.colorbar()

#plt.show()
st.pyplot(fig)