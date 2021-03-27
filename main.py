#Latency challenge
from sys import stdin
import random
# classify terminal input
for line in stdin:
    if line == '': break
    print([round(random.random()) for x in line.split(',')])