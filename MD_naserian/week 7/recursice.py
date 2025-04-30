def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

# Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

# Sum of First n Natural Numbers
def sum_natural(n):
    if n <= 1:
        return n
    else:
        return n + sum_natural(n - 1)

# Power Function (Exponentiation)
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
    
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    
if __name__ == "__main__":
    print(factorial(5))
    print(sum_natural(5))
    print(fibonacci(6))
    print(power(2, 3))
    print(reverse_string("hello"))
