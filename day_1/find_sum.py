"""Given a list of integers, find the sum of all positive numbers, sum all odd numbers and compare it """

num_list = []

while True:
    user_input = input("Enter a number or (q to quit): ")
    if user_input.lower() == "q":
        break
    try:
        num = int(user_input)
        num_list.append(num)
    except ValueError:
        print("Invalid Input! Enter integer number")

even_num_list=[]
odd_num_list =[]
even_num_list_sum =0
odd_num_list_sum = 0

if not num_list:
    print("No numbers were entered.")
else :
    # print("Input Number List : ", num_list)
    for i in num_list:
        if i % 2 == 0:
            even_num = i
            even_num_list.append(even_num)
        else:
            odd_num = i
            odd_num_list.append(odd_num)

    print(even_num_list)
    print(odd_num_list)

    sum_even = 0
    sum_odd = 0

    for i in even_num_list:
        sum_even  += i     

    for i in odd_num_list:
        sum_odd  += i     

    if sum_even == sum_odd:
        print("both are equal")
    elif sum_odd > sum_even:
        print ("odd wins", sum_odd )
    else:
        print("sum wins", sum_even)

    odd_num_list_sum = sum_odd
    even_num_list_sum = sum_even

print("sum of even numbers = ",even_num_list_sum)
print("sum of odd numbers = ",odd_num_list_sum)