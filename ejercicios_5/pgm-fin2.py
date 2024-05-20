numeros = []

while True:
    entrada = input("Introduce un número #️⃣ o escribe 'fin' para terminar: ⏸️ ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Error 🚫: Por favor, introduce un número válido.")
        continue

if numeros:
    maximo = max(numeros)
    minimo = min(numeros)
    print("Máximo 🟰 ", maximo)
    print("Mínimo 🟰 ", minimo)
else:
    print("No se introdujeron números‼️")
