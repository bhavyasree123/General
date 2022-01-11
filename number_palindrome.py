number = int(input("Enter your palindrome Number: "))
if str(number) == str(number)[::-1]:
    print("Its a Palindrome")
else:
    print("No,Its not a palindrome")