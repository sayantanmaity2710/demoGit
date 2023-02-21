#string
# string = input("Enter string:")
# string = string.casefold()
# rev_string = reversed(string)
#
# if list(string) == list(rev_string):
#     print("is palindrome")
# else:
#     print('not palindrome')

# Number
Num = int(input("Enter a value:"))
temp = Num
rev = 0
while Num > 0:
    dig = Num % 10
    rev = rev * 10 + dig
    Num = Num // 10
if temp == rev:
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")
