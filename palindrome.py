def palindrome():
    s="wordpad"
    print(s)
    a=s[::-1]
    print(a)
    if s[0]==a[0] or s[1]==a[1] or s[2]==a[2] or s[3]==a[3] or s[4]==a[4] :
        print("is palindrome")
    else:
        print("not palindrome")
palindrome()