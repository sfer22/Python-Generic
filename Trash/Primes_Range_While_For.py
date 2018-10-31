primes = []
numero = 9

while numero <= 90:

    numero += 1
    prime = True

    for divisor in range(2, 10):

        if numero % divisor == 0 and numero != divisor:
            prime = False

    if prime == True:
        primes.append(numero)


print("Del rango entre 10 y 90, los siguentes numeros son primos:\n\n", primes)