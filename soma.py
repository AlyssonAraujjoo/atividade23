import time

soma = 0

for numero in range(1, 501):
    if numero % 3 == 0:
        soma += numero
        print("a soma dos números é:", soma)
        time.sleep(1)