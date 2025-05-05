# Generatorsdef fibo(n):

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)
def factor(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i 
        yield sum
        
        

def fibo(n):
    previous, current = 0, 1
    for _ in range(n):
        print(current)
        previous, current = current, previous + current

# Generators
def fibonacci(n):
    previous, current = 0, 1
    for _ in range(n):
        # print(current)
        yield current
        # return current
        previous, current = current, previous + current


if __name__ == "__main__":
    print(factorial(10))
    # fibo(100)
    # print('-' * 40)
    # for number in fibonacci(50):
    #     print(number)
        # print(factorial(5))
    for i in factor(10):
        print(i)
