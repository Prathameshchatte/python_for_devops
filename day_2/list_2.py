"""Create a list of fruits and access elements using indexing"""


fruit_list = []

while True:
    usr_input = input("Enter a fruit or (q to quit): ")
    if usr_input.lower() == 'q':
        break
    try:
        fruit_list.append(usr_input)
    except ValueError:
        print("Enter a valid input.")

if not fruit_list :
    print("No fruits were enterred")


print(fruit_list)


