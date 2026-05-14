numero = 0
while numero < 1: 
    numero = int(input('Digite um número: '))

contador = 1
testador = 0

for i in range(numero - 1):
    if numero % contador == 0:
        testador = testador + contador
    
    contador += 1

if testador == numero:
    print(f'{numero} é perfeito')

else testador != numero:
    print(f'{numero} não é perfeito')
