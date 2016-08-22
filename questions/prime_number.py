def _odd_iter():
    n = 3
    while True:
        yield n
        n += 2

def _divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        # it = filter(_divisible(n), it)
        it = filter(_divisible(n), it)

for i in primes():
    if i < 1000:
        print (i)
    else:
        break

