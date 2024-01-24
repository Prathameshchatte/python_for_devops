"""
bubble sort
"""


num_list = [2, -6, 5 , 89, 1,3,9,78]

for i in range(len(num_list)):
    for j in range(len(num_list)):
        if num_list[i] < num_list[j]:
            temp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temp
        
print(num_list)