import random

limite = 0
while limite < 1: 
    limite = int(input('Digite a quantidade de números aleatórios: '))

contador = 1

for i in range(limite):
    print(f'{contador}o número aleatório: {random.randint(1, 100)}')
    contador += 1