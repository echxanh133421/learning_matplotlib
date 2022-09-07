#cho phép hiển thị nhiều ô trong 1 hình
'''
dùng hàm : subplot
-nhận 3 dối số:số hàng ,số cột: là 2 dối số đầu tiên
đối số thứ 3 : là đồ thị thứ.... ví dụ : 2<> đồ thì thứ 2
'''

'''
-hàm suptitle():
plt.suptitle('sdjfhjhdfk'):
tiêu dề lướn của tất cả
'''

#ví dụ vẽ 2 ô

import math
import numpy as np
import matplotlib.pyplot as plt

#đồ thị 1 trái trên
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title('đồ thị 1')


#đồ thị 2 : phải trên
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,2,2)
plt.plot(x,y)
plt.title('đồ thị 2')



#đồ thị 3: trái dưới
x=np.arange(1,10,0.05)
y=x*x
plt.subplot(2,2,3)
plt.plot(x,y)
plt.title('đồ thị 3')


plt.suptitle('tổng hợp đồ thị')

plt.show()