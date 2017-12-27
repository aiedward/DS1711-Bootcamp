import time
from util.ArrayUtil import ArrayUtil

def linear_sum(S, n):
    if (n == 0):
        return 0
    return linear_sum(S, n-1) + S[n-1]

def binary_sum(S, start, stop):
    if (start >= stop):
        return 0
    elif (start==stop-1):
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
    


S = ArrayUtil.generateRandomArray(990)
start_time = time.time()
sum = linear_sum(S, len(S))
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
sum = binary_sum(S, 0, len(S))
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
