# Imprimir los primeros 50 números primos
def print_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    print(f"Los primeros {n} números primos son:")
    for prime in primes:
        print(prime)

print_first_n_primes(50)