""" list = collection of dissimilar data types
Stores values.

syntax : 
    list_of_names = ["abhay", "manik", "rutuja"]
"""

list_of_csp = list(["aws", "azure", "gcp"])
list_of_env = ["dev", "stg","prd"]

#to see the operations can be performed
"""print(dir(list_of_csp))"""

#to add/append the element in last
list_of_csp.append("IBM")

#to insert the element at specific index
list_of_env.insert(3,"test")

print(list_of_csp)
print(list_of_env)


# for i in list_of_csp:
#     print(i)

#for help or manual
#print(dir(list_of_env))
#work with append, insert, delete
