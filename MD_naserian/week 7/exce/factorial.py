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
        
if __name__ == "__main__":
    print(factorial(10))
    
  
    for i in factor(10):
        print(i)
    print(list(factor(10)))