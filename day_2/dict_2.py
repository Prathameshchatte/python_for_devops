"""create variables for storing person's name , age and average test score """

usr_name_list = []
usr_age_list = []
usr_score_list = []

while True:
    user_input = input ("Enter 'a' to provide Inforamtion or ('q' to quit) : ")
    if user_input.lower() == "q":
        break
    # try : 
    elif user_input.lower() == "a":
        user_name = input("Enter Your Name : ")
        usr_name_list.append(user_name)

        user_age = input("Enter Your Age : ")
        usr_age_list.append(user_age)

        user_score = input("Enter Your Test Score : ")
        usr_score_list.append(user_score)
    # except ValueError:
    else:
        print("Enter Valid Input Option. 'a' to provide Information or ( 'q' to quit) ")

Id = 0
Id = int(input("Enter a Employee Id , To see Information : "))
print("User Names = ", usr_name_list[Id])
print("User Age = ",usr_age_list[Id])
print("User Score = " ,usr_score_list[Id])


# user_dict = {
#     "name" : "Prathamesh",
#     "age" : "24",
#     "score" : "85"
# }

# print("Your Name : ", user_dict["name"])
# print("Your Age : ", user_dict["age"])
# print("Your Test Score : ", user_dict["score"])

