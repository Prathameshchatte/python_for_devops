num1 = float(input("enter num 1"))
num2 = float(input("enter num 2"))

opr = input("enter operator")
result = None #if user inputs different operator, and we don't want to get error
if opr == "+" :
    result=num1+num2
elif opr == "-":
    result=num1-num2
elif opr == "*":
    result = num1*num2

print("your calculation is =",result)


