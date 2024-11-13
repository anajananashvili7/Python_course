#1

def encode_to_utf8(input_string):
    return input_string.encode('utf-8')


user_input = input("Enter a string to encode in UTF-8: ")

utf8_encoded = encode_to_utf8(user_input)

print("UTF-8 Encoded String:", utf8_encoded)



#2


def process_string(input_string):
    processed_string = input_string.strip().lower()
    processed_string = processed_string.replace("python", "Python")
    
    processed_string += " Python"
    return processed_string

user_input = input("Enter a string: ")


result = process_string(user_input)

print("Processed String:", result)


#3

def first_half(input_string):
    half_index = len(input_string) // 2  
    return input_string[:half_index]  


user_input = input("Enter a string: ")

result = first_half(user_input)


print("First half of the string:", result)


#4
import string

def is_valid_string(input_string):
    has_letter = any(c in string.ascii_letters for c in input_string)  
    has_digit = any(c.isdigit() for c in input_string)  
    has_invalid_char = any(c not in string.ascii_letters and not c.isdigit() for c in input_string) 

    return has_letter and has_digit and not has_invalid_char


user_input = input("Enter a string: ")


if is_valid_string(user_input):
    print("The string is valid.")
else:
    print("The string is invalid.")


#5

def convert_string_to_bytes_and_back(input_string):

    byte_value = input_string.encode('utf-8')
    print("Bytes:", byte_value)
    
    
    string_value = byte_value.decode('utf-8')
    print("String:", string_value)

user_input = input("Enter a string: ")


convert_string_to_bytes_and_back(user_input)

