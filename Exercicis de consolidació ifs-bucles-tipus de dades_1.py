numeros = []

con = 1

while con <=10:
    numeros.append(int(input("Introduzca un número: ")))
    con += 1

pares = []
impares = []

for num in numeros:
    if(num % 2 == 0):
        pares.append(num)
    else:
        impares.append(num)

print(pares)
print(impares)