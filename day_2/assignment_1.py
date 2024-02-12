"""
Input a list of Numbers from user i.e take integer inputs and append to list.

Find the smallest and Second Smallest Numbers from that list
"""
"""---------------------------------------------------------------"""

#if we don't want to use default sort function then we can go with sorting algorithm 
# for i in range(len(num_list)):
#     for j in range(len(num_list)):
#         if num_list[i] < num_list[j]:
#             temp = num_list[i]
#             num_list[i] = num_list[j]
#             num_list[j] = temp


"""----------------------using default function: sort()-----------------------------------------"""
num_list = [] #created a numbers list

# use of while loop for taking multiple input values from user
while True:
    usr_input = input("Enter a number or (q to quit): ")
    if usr_input.lower() == "q":
        break
    try:
        num = int(usr_input)
        num_list.append(num)#append input in the list
    except ValueError :
        print("Invalid input. Please enter an integer number.")

if not num_list:
    print("No numbers were entered.")
else :
    print("Input Number List : ", num_list)

    #to remove the duplicates, lsit is converted to set and again to list
    num_list = list(set(num_list))
    num_list.sort() #sort function for sorting numbers in assending order

smallest = num_list[0]
second_smallest = num_list[1] if len(num_list) > 1 else None

print("Smallest number = ", smallest)
print("Second smallest number = ", second_smallest)
    