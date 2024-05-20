def fibonacci(n):
    fib_series = [0, 1]  # Inicializamos la serie de Fibonacci con los dos primeros términos
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])  # Generamos el siguiente término sumando los dos últimos
    return fib_series

# Pedimos al usuario el número de términos que quiere generar en la serie
num_terminos = int(input("Introduce el número de términos de la serie de Fibonacci que deseas generar: "))

# Generamos la serie de Fibonacci
serie_fibonacci = fibonacci(num_terminos)

# Mostramos la serie de Fibonacci generada
print("Serie de Fibonacci con", num_terminos, "términos:", serie_fibonacci)
