#!/usr/bin/env python3

import time
iterations = 100000000
start = time.time()
mylist = []
for i in range(iterations):
    mylist.append(i+1)
end = time.time()
print(end - start)

start = time.time()
mylist = [i+1 for i in range(iterations)]
end = time.time()
print(end - start)

start = time.time()
mylist = list(range(iterations))
end = time.time()
print(end - start)
