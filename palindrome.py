#part 1
def palindrome(s): 
    print(s)
    a=s[::-1]
    print(a)
    if s[0]==a[0] or s[1]==a[1] or s[2]==a[2] or s[3]==a[3] or s[4]==a[4] :
        print("is palindrome")
    else:
        print("not palindrome")
palindrome("wordpad")

#part 2
def palindrome(n):
    
    if n==n[::-1]:
        print("this is palindrome")
        # return n
    else:
        print("this is not palindrome!")
        # return n
palindrome("malayalam")
