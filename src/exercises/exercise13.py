
def prime_in_position(position:int) -> int:
    counter = 1
    isPrime: bool = True
    j:int = 0
    primes = [2]
    while len(primes) < position:
        counter += 2 #ímpares
        while (primes[j]*primes[j] <= counter):
            if counter % primes[j] == 0:
                isPrime = False
    if isPrime:
        primes.append(counter)
    return primes[position]

print(prime_in_position(6))