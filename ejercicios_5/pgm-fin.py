total = 0
cantidad_numeros = 0

while True:
    entrada = input("Introduce un número #️⃣ o escribe 'fin' para terminar ⏸️: ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        total += numero
        cantidad_numeros += 1
    except ValueError:
        print("Error 🚫: Por favor, introduce un número válido.")
        continue

if cantidad_numeros > 0:
    media = total / cantidad_numeros
    print("Total 🟰 ", total)
    print("Cantidad de números 🟰 ", cantidad_numeros)
    print("Media 🟰 ", media)
else:
    print("No se introdujeron números‼️")
