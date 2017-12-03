import pandas as pd
import matplotlib.pyplot as plt

'''latency=pd.read_table("results.txt", sep="\t")
n_requests = latency.num_requests
interval_conf = latency.interval
plt.plot(n_requests, interval_conf)
plt.xlabel("Number of requests")
plt.ylabel("Confidence Interval")
plt.show()
'''

latency = []
f1 = open("latency.txt", 'r')
for line in f1:
    latency.append(line)
plt.figure(1)
plt.title("Latency")
plt.xlabel("Time elapsed in s/10")
plt.ylabel("Roundtrip time (s)")
plt.plot(latency, 'ro')

'''throughput = []
f1 = open("throughput.txt", 'r')
for line in f1:
    throughput.append(line)
plt.figure(2)
plt.title("Throughput")
plt.xlabel("Time elapsed in s/10")
plt.ylabel("Throughput MB/s")
plt.plot(throughput)'''

plt.show()
