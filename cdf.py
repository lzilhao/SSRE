import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('latency2.txt')
sorted_data = np.sort(data)

yvals = np.arange(len(sorted_data))/float(len(sorted_data)-1)

plt.plot(sorted_data, yvals)

data = np.loadtxt('latency.txt')
sorted_data = np.sort(data)

yvals = np.arange(len(sorted_data))/float(len(sorted_data)-1)
plt.plot(sorted_data, yvals)


plt.show()
