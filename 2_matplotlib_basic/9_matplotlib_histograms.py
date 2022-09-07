#biểu đồ

'''
hist() method:
'''
#vd:

'''
Để đơn giản hơn, chúng tôi sử dụng NumPy để tạo ngẫu nhiên một mảng có 250 giá trị, trong đó các giá trị sẽ tập trung vào khoảng 170 và độ lệch chuẩn là 10. Tìm hiểu thêm về Phân phối Dữ liệu Bình thường trong Hướng dẫn Học máy của chúng tôi .

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()