
list_of_env = ["dev", "stg", "prd", "test"]

key = "test"

is_found = False
for env in list_of_env:
    if env == key:
        is_found = True
        # print("Found", key)
        # break
    
if is_found:
    print("Found")
else:
    print("not found")