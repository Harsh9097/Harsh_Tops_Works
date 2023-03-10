
 
def isPalindrome(str):
    return str == str[::-1]
 
str = "malayalam"
ans = isPalindrome(str)
 
if ans:
    print("pelindrom !")
else:
    print("not pelindrom !")
