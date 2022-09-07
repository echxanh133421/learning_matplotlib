import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#tạo mảng dữ liệu của x : 0-2pi step= 0.05
x= np.arange(0,2*math.pi,0.05)
print(x)
#tạo mảng y= sin(x)
y=np.sin(x)
#vẽ
plt.plot(x,y,'o',c='g')

# #vẽ hình thứ 2:
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);

plt.xlabel('x')
plt.ylabel('y')
plt.title('do thi sin(x)')

x=[1,2,3,4]
y=[3,2,6,6]
#marker để đánh dấu điểm
plt.plot(x,y,marker='o',linestyle='dotted',color='r')

#display
plt.show()