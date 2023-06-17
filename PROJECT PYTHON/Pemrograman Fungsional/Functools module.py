"""Deret Fibonacci"""
def fibonacci(n):
    if n == 1 :
        return 1
    elif n == 2:
        return 1
    elif n > 2 :
        return fibonacci(n-1)+ fibonacci(n-2)
#testing 1
for n in range (1,11):
#testing 2
#for n in range (1,101):
#testing 3
#for n in range (1,501):

    print (n, ":", fibonacci (n))

"""Memoization"""
fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value

for n in range(1, 101):
    print(n, ":", fibonacci(n))

"""LRU Cache = Least Recently Used"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 501):
    print(n, ":", fibonacci(n))


from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n harus bilangan integer positif")
    if n < 1:
        raise ValueError("n harus bilangan integer positif")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
for n in range (1, 101):
    print (fibonacci(n+1)/fibonacci (n))

"""Fungsi partial()"""
from functools import partial

def func_multiply(x, y):
    return x * y

print(func_multiply(3, 4))  # 12

# membuat fungsi partial
partial_multiply = partial(func_multiply, 4)

print(partial_multiply(4))  # 16
print(partial_multiply(3))  # 12

"""Fungsi reduce()"""
from functools import reduce

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x * y
result = reduce(multiplier, data)
print(result)  # 6469693230

product = 1
for x in data:
    product = product * x
print(product)  # 6469693230

numbers = [99, 47, 11, 6, 42, 102, 13, 9]
f = lambda a, b: a if a > b else b
max_value = reduce(f, numbers)
print(max_value)  # 102

    