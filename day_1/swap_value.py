"""PROBLEM STATEMENT : Implement a program that swaps values of two variables """


def swap(val_1, val_2):
    temp = val_1
    val_1 = val_2
    val_2 = temp
    
    return{
        "first_value" : val_1,
        "second_value": val_2,
    }

val_1=(input("Enter first value : "))
val_2=(input("Enter second value : "))

print("First Value = ",val_1, "\nSecond Value = ", val_2)

swapped_value = swap(val_1, val_2)
print(f"swapped first value: {swapped_value['first_value']}")
print(f"swapped second value: {swapped_value['second_value']}")