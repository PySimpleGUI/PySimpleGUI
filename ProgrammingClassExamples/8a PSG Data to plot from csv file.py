#Matplotlib, pyplt and csv
#Tony Crewe
#Sep 2017 - updated Sep 2018

import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import MaxNLocator


x=[]
y=[]

with open('weight 20182.csv', 'r', encoding = 'utf-8-sig') as csvfile:
    plots = csv.reader(csvfile)
    for data in plots:
        var1 = (data[0])    #get heading for x and y axes
        var2 = (data[1])
        break
    for data in plots:      #get values - add to x list and y list
        x.append(data[0])   
        y.append(float(data[1]))


ax = plt.subplot(1,1,1)
ax.set_ylim([82, 96])
ax.xaxis.set_major_locator(MaxNLocator(10))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.plot(x,y, label = 'data loaded\nfrom csv file')
plt.axhline(y  = 85.5, color = 'orange', linestyle = '--', label = 'target')
plt.xlabel(var1)
plt.ylabel(var2)
plt.title('weight loss from\n first quarter 2018')


plt.legend()
plt.show()
