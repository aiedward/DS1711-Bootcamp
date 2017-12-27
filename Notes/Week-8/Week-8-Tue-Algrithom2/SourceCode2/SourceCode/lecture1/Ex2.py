import random
import time
'''
from openpyxl import load_workbook
start = time.time()

wb = load_workbook(filename = 'H-1B_Disclosure_Data_FY16.xlsx')
ws = wb['H-1B_FY2016']
'''

def reverse(S, start, stop):
    if (start<stop):
        S[start], S[stop] = S[stop], S[start]
        reverse(S, start+1, stop-1)
        
S = [3,2,5,4,1]
reverse(S, 0, len(S)-1)

print(S)

aset = set(random.sample(range(1,100000), 10000))
alist = random.sample(range(1, 100000), 10000)

start = time.time()
print(1 in aset)
end = time.time()
print(end - start)

start = time.time()
print(1 in alist)
end = time.time()
print(end - start)

s = "ABBA"
print(s[0])
print(s[1])
r = chr("a") ^ chr("b")
r = ord(s[0])
print(r)