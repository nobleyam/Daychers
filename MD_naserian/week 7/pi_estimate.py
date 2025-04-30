


def create_odd_numbers():
    num= 1
    while True:
        yield num
        num +=2
def create_cosequetive_number():
     num= 1
     while True:
        yield num
        yield num +1
        yield num +2
        num +=2


def gregorey(n):
    odd = create_odd_numbers()

    pi_approximate = 0
    for _ in range(n):
        pi_approximate += 4 / next(odd)
        yield pi_approximate
        pi_approximate -= 4 / next(odd)
        yield pi_approximate 

def nilakantha(n):
    sequence = create_cosequetive_number()

    pi_approximate = 3
    for _ in range(n):
        pi_approximate += 4 / (next(sequence) * next(sequence) * next(sequence))
        yield pi_approximate
        pi_approximate -= 4 / (next(sequence) * next(sequence) * next(sequence))
        yield pi_approximate 


if __name__ == "__main__":

    for val in gregorey(5):
        print(val)
    print("--------------------")
    for val in nilakantha(5):
        print(val)