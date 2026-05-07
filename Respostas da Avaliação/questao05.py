quantidade = 0
while quantidade < 1: 
    quantidade = int(input('Digite a quantidade de valores: '))

contador = 1
numeros = []
for i in range(quantidade):
    numero = int(input(f'Digite o valor {contador}: '))
    numeros.append(numero) # [1, 3, 4]
    contador += 1

quantidade_acima_da_média = 0
for numero in numeros:
    soma = sum(numeros)
    média = soma / quantidade
    menor = min(numeros)
    maior = max(numeros)
    if numero > média:
        quantidade_acima_da_média = quantidade_acima_da_média + 1


print(f'A soma total é: {soma}')
print(f'A média é: {média:.0f}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print(f'A quantidade de números acima da média é {quantidade_acima_da_média}')
