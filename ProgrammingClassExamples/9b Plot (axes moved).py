#matplotlib, numpy, pyplot
#Tony Crewe
#Sep 2017 - updated Sep 2018import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


fig=plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(-np.pi*2, np.pi*2, 100)
y= np.sin(x)
ax.plot(x,y)

ax.set_title('sin(x)')
#centre bottom and keft axes to zero

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')


plt.show()




