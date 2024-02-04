def palindrome(string):
    s=string[::-1]
    if s==string:
        print(True)
    else:
        print(False)
    


phrase=input()
palindrome(phrase)