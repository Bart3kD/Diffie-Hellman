from random import randrange

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i==0:
            return False    

    return True

def rand_prime(size):
    prime = 1

    while not is_prime(prime):
        prime = randrange(size)

    return prime