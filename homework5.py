#1

def main():
    numbers = []  

    while True:
        action = input("Enter 'a' to add a number, 'r' to remove a number, or 'e' to exit: ").lower()

        if action == 'a':
            number = input("Enter a number to add: ")
            try:
                numbers.append(float(number))  
                print(f"Number {number} added. Current list: {numbers}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif action == 'r':
            number = input("Enter a number to remove: ")
            try:
                numbers.remove(float(number))  
                print(f"Number {number} removed. Current list: {numbers}")
            except ValueError:
                print("Invalid input. The number is not in the list.")
            except Exception as e:
                print(f"Error: {e}")

        elif action == 'e':
            print("Exiting the program.")
            print(f"Final list: {numbers}")
            break

        else:
            print("Invalid action. Please enter 'a', 'r', or 'e'.")

if __name__ == "__main__":
    main()



#2


my_list_1 = [43, '22', 12, 66, 210, ["hi"]]


index_of_210 = my_list_1.index(210)
print(f"Index of 210: {index_of_210}")


my_list_1[-1].append("hello")
print(f"List after adding 'hello': {my_list_1}")

del my_list_1[2]  
print(f"List after deleting element at index 2: {my_list_1}")


my_list_2 = my_list_1.copy()  
my_list_2.clear()  
print(f"my_list_1: {my_list_1}")
print(f"my_list_2 after clearing: {my_list_2}")


#3

import re

def validate_phone_number(phone_number):

    pattern = r'^\(\d{3}\) \d{3}-\d{3}$'
    
    if re.fullmatch(pattern, phone_number):
        return phone_number
    else:
        return "Invalid format"

# Get user input
user_input = input("Enter a phone number in the format (123) 456-789: ")
result = validate_phone_number(user_input)
print(result)

