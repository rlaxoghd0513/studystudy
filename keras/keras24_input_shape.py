#input_dim 행과 열만 있는 2차원 데이터셋만 했음
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np
from sklearn.preprocessing import MinMaxScaler #값을 0에서 1사이로 바꾸지만 standardScaler는 평균점을 중심으로 모아준다
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import MaxAbsScaler  #
from sklearn.preprocessing import RobustScaler  #
 
#1 데이터
datasets = load_boston()
x= datasets.data    
y= datasets.target

print(type(x)) #<class 'numpy.ndarray'>
print(x)

#numpy가 부동소숫점 연산에 최적화되어있다
#데이터가 커지면 연산이 터질수도 있으니까 0~1 로 맞춰준다 = 정규화
#정규화 normalization
#모든데이터를 0~1사이로 압축시킨다 하지만 y데이터는 아니고 x에만 해당
# 성능좋아질수도 있다 속도 빨라짐 등등의 장점이 존재
# 단점은 성능이 안좋을 수도 있음
# 최대값으로 나눠버린다 x/max  최소값이 0이 아닐때  x-min/max-min

# print(np.min(x), np.max(x))  #0.0 711.0
# scaler = MinMaxScaler()
# scaler.fit(x)  #이 비율로 변환할 준비를 해라
# x = scaler.transform(x) # 실제로 변환해라  fit과 transform 둘다 실행해야한다 #0.0 1.0
# print(np.min(x), np.max(x)) 

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, random_state=300)
#x_predict 가 x.max를 벗어날 수 있다 그래서 훈련데이터만 정규화한다
#전체를 정규화하지 않는 가장 큰 이유는 과적합이 생길수가 있다 
#과적합 막는 방법 내가 예측할 구간도 정규화해준다
# x_train의 비율에 맞춰서 test나 predict도 qusghks한다 비율이 1을 넘는 것도 있을텐데 괜찮다 더 좋다 다 안에 들어가도 상관없다
# 그래서 train과 test분리한후 정규화 한다

scaler = MinMaxScaler()  #scaler = StandardScaler()    뭐쓸지만 정하면 됨
scaler.fit(x_train)
x_train = scaler.transform(x_train)
# x_test는 x_train의 변한 범위에 맞춰서 하기 때문에 fit 할 필요가 없다 scaler.fit(x_train)그대로 써야됨
x_test = scaler.transform(x_test)
print(np.min(x_test), np.max(x_test)) 



#2 모델구성
model=Sequential()
# model.add(Dense(1, input_dim=13))
model.add(Dense(1, input_shape=(13, ))) #열,

#데이터가 3차원이면(통상 시계열데이터)
#(1000,100,1) =>>> input_shape = (100,1)  맨앞에 있는게 데이터의 갯수(행) 3차원에선 면 #굳이 안따져도 됨

#데이터가 4차원이면(통상 이미지 데이터)
#(60000, 32, 32, 3) =>>> input_shape=(32,32,3)  맨앞에 있는게 데이터 갯수(행) 4차원에선 공간 #굳이 안따져도 됨


#컴파일 훈련
model.compile(loss='mse', optimizer= 'adam')
model.fit(x_train, y_train, epochs=100, batch_size=32)

#평가 예측
loss = model.evaluate(x_test, y_test)
print('loss:', loss)

# y값이 수치로 나와야한다 선형회귀
# y가 개냐 소냐 다중분류 (이진분류)
# Sequential 위에서 아래로만 내려간다
# 모델들 여러개를 만들어 합친다 Sequential로 가능은 한데 복잡해진다
# 함수형 모델
