def fib(max):
    a, b = 1, 1
    while a < max:
        yield(a)
        a, b = b, a+ b
    return 'done'
