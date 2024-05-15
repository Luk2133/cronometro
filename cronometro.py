import time

a = int()

segundos = int(input("Digite os segundos para iniciar o cronometro: "))

for a in range(0, segundos+1):
    time.sleep(1)
    print(a)
print("fim")