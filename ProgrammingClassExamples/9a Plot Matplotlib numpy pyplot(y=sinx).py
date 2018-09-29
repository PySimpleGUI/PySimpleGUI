#matplotlib, numpy, pyplot
#Tony Crewe
#Sep 2017 - updated Sep 2018

import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(-np.pi*2, np.pi*2, 100)
y= np.sin(x)
ax.plot(x,y)

ax.set_title('sin(x)')


plt.show()




