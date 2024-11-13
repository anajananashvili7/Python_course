#1
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)

    return sequence


n = 10
print(fibonacci_sequence(n))


#2
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2)) 


#3
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


n = 5
print(factorial(n))  


#4
def count_character(string, char):
    if len(char) != 1:
        raise ValueError("The second parameter must be a single character.")
    
    count = string.count(char)
    return count

my_string = "Hello, world!"
my_char = "o"
print(count_character(my_string, my_char))  

