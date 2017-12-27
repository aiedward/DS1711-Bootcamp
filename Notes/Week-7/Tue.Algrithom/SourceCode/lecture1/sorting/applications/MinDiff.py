import sys

def printClosest(ar1, ar2):
    m = len(ar1)
    n = len(ar2)

    diff = sys.maxsize
    
    p1 = 0
    p2 = 0
    
    while (p1 < m and p2 < n):
        if abs(ar1[p1] - ar2[p2]) < diff:
            diff = abs(ar1[p1] - ar2[p2])
        
        if (ar1[p1] > ar2[p2]):
            p2 += 1
        else:
            p1 += 1

    return diff


def main():

    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    diff = printClosest(ar1, ar2)
    print (diff)
    
    ar3 = [3, 27, 45, 68, 70, 81, 89];
    ar4 = [9, 16, 25, 35, 70, 84];
    diff = printClosest(ar3, ar4)
    print (diff)  
      
if __name__ == "__main__":
    main()