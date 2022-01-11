# function which return reverse of a string
def pal(s):
    return s == s[::-1]
s = input("Enter your String: ")
ans = pal(s)
if ans:
    print("YES!, It is a palindrome")
else:
    print("No :< its not a palindrome") 