"""what is palindrome: a word/ number is similar when read from both left and right side.
   ex=141, nitin 
"""
usr_in = str(input("Enter anything you want : "))

print(usr_in)
b= usr_in[::-1] #::-1 is used to assign string from last index to first index
print(b)

if usr_in == b:
    print(f"{usr_in} is palindrome")
else:
    print(f"{usr_in} is not a palindrome")


