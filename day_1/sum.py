num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
#if you don't write int while taking input from user compiler will bydefault take it as "string"
sum = int(num_1 + num_2)

# print(type(sum))
#if you want shoe input variable value while printing then you have to use print(f "") 
#and write the variable name in {} curly brackets 
print(f"sum of {num_1} and {num_2} is {sum}")