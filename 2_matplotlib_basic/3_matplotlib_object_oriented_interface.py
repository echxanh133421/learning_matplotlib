#giao diện hướng đối tượng

'''
Mặc dù có thể dễ dàng tạo nhanh các ô bằng mô-đun matplotlib.pyplot ,
nhưng việc sử dụng phương pháp hướng đối tượng được khuyến nghị vì
nó mang lại nhiều quyền kiểm soát và tùy chỉnh hơn các ô của bạn.
Hầu hết các chức năng cũng có sẵn trong lớp matplotlib.axes.Axes .
'''

from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()