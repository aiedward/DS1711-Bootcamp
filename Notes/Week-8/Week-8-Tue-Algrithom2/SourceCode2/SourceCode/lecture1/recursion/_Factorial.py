def factorial(n):
    assert(n>=0)
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial2(n):
    assert(n>=0)
    if (n <= 1): 
        return 1
    return factorial2(n-1) * n

def main():
    n = 1000
    for i in range(n+1):
        print(i, ": ", factorial(i), ", ", factorial2(i))
    
main()



