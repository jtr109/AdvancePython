import random


def get_rand(min_num=1, max_num=100, numbers=10):
    rands = []
    for i in range(numbers):
        rands.append(random.randint(min_num, max_num))
    return rands

if __name__ == '__main__':
    print(get_rand(1, 30, 5))

