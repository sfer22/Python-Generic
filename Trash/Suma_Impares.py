
impares = 0
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

while numero1 >= numero2:
    print("")
    print("ERROR!!! - El primer numero debe ser estrictamente menor que el segundo!!\n")
    numero1 = int(input("Digite el primer numero: "))
    numero2 = int(input("Digite el segundo numero: "))

for numero in range(numero1, numero2+1):

    if numero % 2 != 0:
        impares += numero

print("")
print("La suma de los numeros impares en el rango [" + str(numero1) + ", " + str(numero2) + "] es de:", impares)
