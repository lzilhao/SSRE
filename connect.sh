#!/bin/bash
ip="172.16.1.51"
port="80"
for i in {1..100} 
do
  # do nothing just connect and exit
  echo $i;
  echo "exit" | nc ${ip} ${port};
done
