import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline 表示だとアニメーションしない
# %matplotlib


fig, ax = plt.subplots(1, 1)
ax.set_ylim((-1.1, 1.1))
x = np.arange(0, 100, 1)
# y = [0]*200

while True:
 for i in np.arange(0.2, -0.2, -0.01):
  y = [i]*100
  line, = ax.plot(x, y, color='black')
  plt.pause(0.005)
  line.remove()