#biểu đồ tròn
'''
hàm pie():
-vẽ ngược chiều kim đồng hồ và gioosgn đưuòng tròn luwojgn giác
-có tham số nhãn: label=['','','','']
-thay đổi vị trí bắt đầu bằng đối số: startangle=90
-dối số explode: kéo miếng rời khỏi tâm
-đối số màu: colors=...
'''

'''
thêm chú giải bằng hàm plt.legend():
-có dối số title='jsdhvgbvij'
'''

import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.subplot(3,2,1)
plt.pie(y,labels=mylabels)
plt.title('biểu đồ tròn 1')

y=np.array([35,25,25,15])
plt.subplot(3,2,2)
plt.pie(y,labels=mylabels,startangle=90)
plt.title('biểu đồ tròn 2')

y=np.array([35,25,25,15])
plt.subplot(3,2,3)
my_explode=[0.1,0,0,0]
plt.pie(y,labels=mylabels,explode=my_explode)
plt.title('biểu đồ tròn 3')

y=np.array([35,25,25,15])
plt.subplot(3,2,4)
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y,labels=mylabels,colors=mycolors)
plt.title('biểu đồ tròn 4')

y=np.array([35,25,25,15])
plt.subplot(3,2,5)
plt.pie(y,labels=mylabels)
#thêm chú giải
plt.legend(title = "Four Fruits:")
plt.title('biểu đồ tròn 5')

plt.show()