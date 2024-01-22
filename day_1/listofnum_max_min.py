# #TAKES HELP OF BARD

# def find_max_min(numbers):
#"""Finds the maximum and minimum values in a list of numbers.

#   Args:
#     numbers: A list of numbers.

#   Returns:
#     A tuple containing the maximum value and the minimum value.
#   """
#   if not numbers:
#     raise ValueError("The list of numbers is empty.")

#   max_value = numbers[0]
#   min_value = numbers[0]

#   for number in numbers:
#     if number > max_value:
#       max_value = number
#     elif number < min_value:
#       min_value = number

#   return max_value, min_value

# # Example usage:
# numbers=[15, 45, 8, 6, 7, 9, 1, 3]
# max_value, min_value = find_max_min(numbers)
# print(numbers)
# print("Maximum value:", max_value)
# print("Minimum value:", min_value)



def min_max_number(number_list):
    if not number_list:
        raise ValueError("The List of numbers is empty")
    
    min_num= number_list[0]
    max_num= number_list[0]

    for number in number_list:
        if number > max_num:
          max_num = number
        elif number < min_num:
          min_num = number
    return max_num, min_num


numbers=[15,48,79,2,9,36,89]
max_num, min_num = min_max_number(numbers)
print(numbers)
print("Maximum value =", max_num)
print("Minimum value =", min_num)




