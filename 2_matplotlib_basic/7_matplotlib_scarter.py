#vẽ ra các điểm phân tán:
'''
hàm scatter():
-vẽ 1 dấu chấm cho mỗi lần quan sát
-có thể có thêm đối số color vào hàm viết tắt bằng chữ c,
có thể dùng mã màu
vd:
plt.scatter(x,y,c='r')
-có thể tạo màu sắc cho từng chấm
-vẽ theo bảng màu sẵn có trong matplotlib: xem thêm

- có thể đặt kích cỡ cho các điểm: bằng thêm đối số:
-có đối số alpha: độ mờ 0-1
'''




import matplotlib.pyplot as plt
import numpy as np

#vẽ lần 1
x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.subplot(3,2,1)
plt.scatter(x,y)

#vẽ lần 2
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x,y,c='r')


#vẽ mỗi điểm 1 màu
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.subplot(3,2,2)
colors=np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x,y,c=colors)

#vẽ theo dải màu từ 0-100
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.subplot(3,2,3)
plt.scatter(x,y,c=colors,cmap='viridis')
#vẽ thêm bảng màu bên cạnh
plt.colorbar()


#các điểm với kích thước khác nhau
x=np.array([1,2,3,4,5,6,7,8])
y=np.array([3,7,3,8,0,3,4,6])
sizes=np.array([20,10,40,70,5,34,50,43])
plt.subplot(3,2,4)
plt.scatter(x,y,s=sizes,alpha=0.5)

plt.show()