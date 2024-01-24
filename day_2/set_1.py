# LEARN SET
"""
set is data structure which does not tolerate duplicates

"""
"""
set_1 = {1,5,6,8,22,1,6,9,7,4}
set_2 = {65,5,8,7,3,4,9}

print(set_1)
print(set_2)

print(set_1.intersection(set_2)) #commmon elements
print(set_1.union(set_2)) #merge sets 
"""
#use case when there are duplicates in files

list_of_env = ["dev", "stg", "prd" , "tst", "qa", "prd", "qa", "dev"]
list_of_env = list(set(list_of_env))
#list first converted as set and then again converted in list 
print(list_of_env)