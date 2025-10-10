# Imprimir los primeros 50 números primos
def get_first_n_primes(n):
    """
    Generates a list containing the first n prime numbers.
    This implementation uses trial division against previously found primes.
    """
    n = 50
    if n <= 0:
        return []

    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            # Optimization: no need to check primes larger than the square root of num
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    num_primes_to_find = 50
    prime_numbers = get_first_n_primes(num_primes_to_find)
    print(f"Los primeros {num_primes_to_find} números primos son:")
    for prime in prime_numbers:
        print(prime)