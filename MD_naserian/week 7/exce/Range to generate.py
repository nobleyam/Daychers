import numpy as np
#Method 1--> with numpy:
def range_to_gen(n):
    start = 2.3
    for i in np.arange(start=start, stop=n, step=0.01):
        yield i

# method 2 --> using while and round:
def  my_range(n):
    num = 2.3
    while n > num:
        yield round(num, 2)
        num += 0.01


if __name__ == "__main__":
    # for i in  range_to_gen(3.75):
    #     print(i)
    for i in my_range(3.75):
        print(i)