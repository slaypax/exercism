def prime(nth):
    if nth < 1:
        raise ValueError("not prime")
    primes = [2]
    number = 3
    while len(primes) != nth:
        if is_prime(number):
            primes.append(number)
        number += 2
    return primes[-1]

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
