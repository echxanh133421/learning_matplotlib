
from pylab import *

x = np.linspace(-3, 3, 30)

plot(x, sin(x))
plot(x,cos(x),'-.r')
plot(x,-sin(x),'g--')
plot(x,sin(2*x),'b2')

show()