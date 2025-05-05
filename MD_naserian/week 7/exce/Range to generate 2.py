def range_jumper(c, x):
    number = c
    while x > number:
        yield number
        number += 2

if __name__ == "__main__":
    for i in range_jumper(3, 12):
        print(i)