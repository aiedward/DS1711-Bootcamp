from time import time

def factorial(n):
    assert(n>=0)
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fibonacci(n):
    assert(n>=0)
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return a    


def factorial2(n):
    assert(n>=0)
    if (n <= 1): 
        return 1
    return factorial2(n-1) * n
    
def fibonacci2(n):
    assert(n>=0)
    if (n <= 2): 
        return 1
    return fibonacci2(n-1) + fibonacci2(n-2)

def fibonacci3(n):
    assert(n>=0)
    if (n <= 1): 
        return (n,0)
    (a, b) = fibonacci3(n-1)
    return (a+b, a)
    
def main():
    n = 40
    start1 = time()
    for i in range(1, n+1):
        print(i, ": ", fibonacci(i))
    end1 = time()
   
    start2 = time()
    for i in range(1, n+1):
        print(i, ": ", fibonacci2(i))
    end2 = time()
        
    start3 = time()
    for i in range(1, n+1):
        print(i, ": ", fibonacci3(i))
    end3 = time()

    print ("fibonacci time: ", str(end1 - start1))
    print ("fibonacci2 time: ", str(end2 - start2))
    print ("fibonacci3 time: ", str(end3 - start3))
    
main()