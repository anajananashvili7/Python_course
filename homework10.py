#1

def zip_lists(list1, list2):
    return [f"({x}, '{y}')" for x, y in zip(list1, list2)]


params = [1, 2, 3], ['a', 'b', 'c']
outputs = zip_lists(*params)

print(outputs)  

#2
from functools import reduce

def product_of_list(numbers):
  
    if not isinstance(numbers, list):
        raise TypeError("პარამეტრი უნდა იყოს სიაში")

 
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("სია უნდა შეიცავდეს მხოლოდ რიცხვებს")

   
    return reduce(lambda x, y: x * y, numbers)


params = [1, 2, 3, 4, 5]
output = product_of_list(params)

print(output) 


#3
params = [1, 2, 3, 4, 5, 6, 7]

odd_elements = list(filter(lambda x: x % 2 != 0, params))

print(odd_elements)  


#4
def filter_by_ending(strings, ending):
    if not isinstance(strings, list):
        raise TypeError("პირველი პარამეტრი უნდა იყოს სიაში")
    
    
    if not isinstance(ending, str):
        raise TypeError("მეორე პარამეტრი უნდა იყოს სტრიქონი")

    try:
        
        return list(filter(lambda s: s.endswith(ending), strings))
    except Exception as e:
        raise Exception(f"შეცდომა: {e}")


params = ['hello', 'world', 'coding', 'nod']
ending = 'ing'
outputs = filter_by_ending(params, ending)

print(outputs)  



