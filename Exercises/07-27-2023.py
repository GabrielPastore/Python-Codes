"""Exercise 1 - Define a function that requires two arguments and returns their sum"""

def soma(a, b):
    return a+b

#======##======##======##======#

"""Exercise 2 - Define a function that reads a list of integers and return the highest number in the list"""

def compare(*args):
    maior = args[0]
    for c in range(0, len(args)):
        if args[c] > maior:
            maior = args[c]
    return maior

#======##======##======##======#

"""Exercise 3 - Define a function that reads a list of strings and returns a list of the strings that have more than 5 characters"""

def words(*args):
    list1 = []
    characters_count = 0
    for words in args:
        if len(words) > 5:
            list1.append(words)
    return list1

#======##======##======##======#

"""Exercise 4 - Define a function that accepts a string as parameter and will return True or False wether or not the string is a palindrome"""

def palindrome(a: str):
    a = ''.join(filter(str.isalnum, a.lower()))
    list1 = []
    for c in a:
        list1.append(c)
    if list1 == list(reversed(list1)):
        return True
    else:
        return False
    
#======##======##======##======#

"""Exercise 5 - Define a function that reads a list and then return a dictionary where the strings from the list are the keys and the integers are its values"""

def dici(*args):
    resultado = {}
    for c in args:
        if isinstance(c, str):
            resultado[c] = None
        elif isinstance(c, int):
            key = next((key for key, value in resultado.items() if value is None), None)
            if key is not None:
                resultado[key] = c
    return resultado

#======##======##======##======#

"""Exercise 6 - Define a function where the parameter is a integer and the output of this function is the number in the Fibonacci sequence on the position of the input integer"""

def fibo(n):
    n1 = 1
    n2 = 0
    r = 0
    for c in range(1, n):
        r = n1 + n2
        n2 = n1
        n1 = r
    return r
