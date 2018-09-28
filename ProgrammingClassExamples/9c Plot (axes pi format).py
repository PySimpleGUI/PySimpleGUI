#Plt using matplylib, plotly and numpy
#Tony Crewe
#Sep 2017 updated Sep 2018

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

fig=plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(-np.pi*2, np.pi*2, 100)
y= np.sin(x)
ax.plot(x/np.pi,y)

ax.set_title('sin(x)')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

#Format axes - nicer eh!
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))

plt.show()




