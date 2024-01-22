server_1 = {
    "env":"prd",
    "server":"aws linux2",
    "ram":8096,
    "cpu":4,
    "active": True
}

# if dict_of_items["active"] == True:
#     print("server details :", dict_of_items["server"])
#     print("environment : ", dict_of_items["env"])


server_2 = {
    "env": "prd",
    "server":"aws linux2",
    "ram" : 10000,
    "cpu":4,
    "active":False
}

#create a list of above two dictionaries
env_details = [server_1, server_2]

for env in env_details:
    for key,value in env.items():
        if key == "active" and value == True:
            #it takes bydefault value as a True so it's okay if you not write True
            print(env)
            print(env.values())#to print only values 

