def isPalindrome(s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True

def isPalindrome2(s):
    newS= [i.lower() for i in s if i.isalnum()]
    return newS == newS[::-1]

def main():

    str1 = "A man, a plan, a canal: Panama"
    result = isPalindrome(str1)
    print (result)
    result = isPalindrome2(str1)
    print (result)
    
    str2 = "race a car"
    result = isPalindrome(str2)
    print (result)
    result = isPalindrome2(str2)
    print (result)
    
      
if __name__ == "__main__":
    main()