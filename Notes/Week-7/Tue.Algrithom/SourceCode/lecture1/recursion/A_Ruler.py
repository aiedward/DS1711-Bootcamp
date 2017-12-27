def ruler(prefix, n):
    assert(n>=0)
    if (n==1):
        return "1"
    t = ruler(prefix, n-1)
    return t + " " + str(n) + " " + t

def ruler2(n):
    result = ""
    for i in range(1, n+1):
        result = result + str(i) + " " + result
    return result
    

def main():
    n = 4
    result = ruler("", n)
    print(result)
    result = ruler2(n)
    print(result)
    
main()