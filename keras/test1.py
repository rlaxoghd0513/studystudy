import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 데이터
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([1,2,3,4,5,6,7,8,9,10])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, train_size=0.7, random_state=123, shuffle=True)

#모델구성
model=Sequential()
model.add(Dense(4, input_dim=1))
model.add(Dense(5))
model.add(Dense(6))
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(2))
model.add(Dense(1))

#컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=200, batch_size=5)

#평가, 예측
loss=model.evaluate(x_test, y_test)
print('loss=', loss)

result=model.predict([11])
print('[11]의 결과값=', result)

# 결과값 [[10.996764]] mse epochs 1500 batch 10 45643221 random 123 
    #   [[11.00005]]  mse epochs 200 batch 5  45643221 random 123