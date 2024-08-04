print("\n\n================================================")
print("\nLesson 5: Assignments | Python Functions\n")
print("================================================\n\n")

print("1. The Calculator App\n")
#Objective:
    #The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division. The

#Task 1:
    #Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation

#Task 2:
    #Implement user input to receive numbers and an operation choice, their response for operation should call the associated function
        
#Task 3:
    #Ensure your program can handle division by zero and other potential errors.


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero: Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn’t make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends."
    return num1 / num2


#Task 2: Implement user input and perform arithmetic operation

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

result = None

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    print("Invalid operation")

if result is not None:
    print(f"Result: {result}")





print("================================================")
#2. The Shopping List Maker Objective: The aim of this assignment is to create a program that helps users make a shopping list

    #Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list).

    #Task 2: Include a feature to remove items from the list.

    #Task 3: Add a function that prints out the entire list.




# Task 1: Write a function to add items to a list
def add_item(shopping_list):
    item = input("Enter an item to add to the list: ")
    shopping_list.append(item)
    print(f"Item '{item}' has been added to the list.")

# Task 2: Write a function to remove items from a list
def remove_item(shopping_list):
    item = input("Enter an item to remove from the list: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item '{item}' has been removed from the list.")
    else:
        print(f"Item '{item}' is not in the list.")

# Task 3: Write a function to print the entire list
def print_list(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print("- " + item)

# Main code
shopping_list = []

while True:
    print("Select an option:")
    print("1. Add item to the shopping list")
    print("2. Remove item from the shoping list")
    print("3. Print the entire shopping list")
    print("4. Quit")

    choice = input("Select your choice (1-4): ")

    if choice == "1":
        add_item(shopping_list)
    elif choice == "2":
        remove_item(shopping_list)
    elif choice == "3":
        print_list(shopping_list)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")