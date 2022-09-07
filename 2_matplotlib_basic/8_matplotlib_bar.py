#tạo thanh

'''
hàm plt.bar():tạo thanh dọc
hàm plt.barh(): tạo thanh ngang
- có tham số màu: color='red'
-có tham số chiều rộng thanh: width=0.1
-có tham số chiều cao thanh đối với thanh ngang: height=0.1 giống với width của thanh dọc

'''
import matplotlib.pyplot as plt
import numpy as np

#vẽ dọc
x=np.random.randint(10,size=(10))
y=np.random.randint(10,size=(10))
plt.subplot(2,1,1)
plt.bar(x,y,color='r',width=0.2)

#vẽ ngang
x=np.random.randint(10,size=(10))
y=np.random.randint(10,size=(10))
plt.subplot(2,1,2)
plt.barh(x,y,color='g',height=0.4)

plt.show()