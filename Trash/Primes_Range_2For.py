primes = []

for number in range(10, 91):

    prime = True

    for divisor in range(2, 10):

        if number % divisor == 0 and number != divisor:
            prime = False

    if prime is True:
        primes.append(number)

print("Del rango entre 10 y 90, los siguentes numeros son primos:\n\n", primes)
