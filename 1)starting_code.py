# Let's see, how to plot live data in real-time using Matplotlib. 
# We will learn how to monitor a CSV file that is constantly being updated, and plot the values from that CSV file as they are coming in. 
# This can be extremely useful for plotting data coming from APIs or sensors or any other source that will have frequent updates. 


import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]

plt.plot(x_vals, y_vals)


# index = count()

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 5))


plt.tight_layout()
plt.show()


# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']
