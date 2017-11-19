import requests
import time
import threading
import sys
import os

'''def measure_latency():
    f1 = open('latency.txt', 'w')
    for i in range(10):
        rq = requests.get("http://172.16.1.51")
        print(rq.content)
        print(rq.elapsed.total_seconds())
        f1.write(str(rq.elapsed.total_seconds()) + '\n')
        time.sleep(0.1)
    f1.close()'''


def measure_latency(index, destination):
    global latencies
    cookie = {'PHPSESSID':'q48gg5v226r1r5gi3b7culjgc7'}
    # rq = requests.get("http://"+destination, cookies=cookie)
    rq = requests.get("http://"+destination)
    latencies[index] = rq.elapsed.total_seconds()
    print(str(index) + " " + str(latencies[index]))


def measure_throughput(duration, destination):
    f2 = open('throughput.txt', 'w')
    elapsed_total = 0
    while(True):
        elapsed_single = 0
        start = time.time()
        #rq = requests.get("http://" + destination + "/5MB.zip")
        cookie = {'PHPSESSID':'q48gg5v226r1r5gi3b7culjgc7'}
        # rq = requests.get("http://" + destination, cookies=cookie)
        rq = requests.get("http://" + destination)
        elapsed_single = time.time() - start
        print("elapsed_total: " + str(elapsed_total))
        print("throughput: " + str(len(rq.content)/(elapsed_single*1000000)) + "   MB/s")
        f2.write(str(len(rq.content)/(elapsed_single*1000000)) + "\n")
        elapsed_total += elapsed_single
        if elapsed_total > duration:
            f2.close()
            break
        # os.system("rm 5MB.zip")


if len(sys.argv) < 3:
    print("Usage: measure.py <time in seconds> <ip>")
    sys.exit()

destination = sys.argv[2]
duration = 10*int(sys.argv[1])  # in tenths of seconds
latencies = [None]*duration
f1 = open('latency.txt', 'w')

t1 = threading.Thread(target=measure_throughput, args=(duration/10, destination))
t1.daemon = True
t1.start()

thread_list = []
for i in range(duration):
    t = threading.Thread(target=measure_latency, args=(i, destination))
    t.daemon = True
    t.start()
    thread_list.append(t)
    time.sleep(0.1)

for i in range(0, len(thread_list)):
    thread_list[i].join()

t1.join()

for item in latencies:
    f1.write(str(item) + '\n')

f1.close()
