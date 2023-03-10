from sklearn.datasets import fetch_covtype
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from tensorflow.keras.utils import to_categorical
from tensorflow.python.keras.callbacks import EarlyStopping

datasets = fetch_covtype()

x = datasets.data
y = datasets.target
print(x.shape, y.shape) #(581012, 54) (581012,)
print('y의 라벨값:',np.unique(y)) #[1 2 3 4 5 6 7]
print(y)

#keras 카테고리컬
y = to_categorical(y)
print(y.shape)       #(581012, 8)  #카테고리컬로 하면 0부터 시작해서 0라벨이 생겨서 8개가 된다  
y = np.delete(y,0,axis=1)   #y의 열에서 0번째 행을 뺀다
print(y)   

#2. sklearn
# from sklearn.preprocessing import OneHotEncoder
# ohe = OneHotEncoder()
# y = y.reshape(-1,1)
# y = ohe.fit_transform(y).toarray()
# print(y.shape) # (581012,7)
# print(type(y)) #<class 'numpy.ndarray'>

#3.pandas get_dummies
# import pandas as pd
# y=pd.get_dummies(y)
# print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x,y, random_state =123, 
                                             shuffle = True, train_size = 0.8)


#모델구성
model = Sequential()
model.add(Dense(60, input_dim=54))
model.add(Dense(60))
model.add(Dense(50))
model.add(Dense(40))
model.add(Dense(30))
model.add(Dense(20))
model.add(Dense(7, activation = 'softmax'))

#컴파일 훈련
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
es=EarlyStopping(monitor='acc', patience=10, mode='max',verbose=1, restore_best_weights=True)
model.fit(x_train, y_train, batch_size=100000, epochs=1, validation_split=0.2,verbose=1, callbacks=[es])


#평가 예측
results = model.evaluate(x_test, y_test)
print('results:', results)

y_predict = model.predict(x_test)
print(y_predict.shape)
y_test_acc = np.argmax(y_test, axis=1)
print(y_test_acc)
y_predict_acc = np.argmax(y_predict, axis=1)

acc = accuracy_score(y_test_acc, y_predict_acc)
print('acc:', acc)


