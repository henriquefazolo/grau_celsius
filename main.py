'''
leia do teclado uma temperatura em graus Celsius e mostre na tela o seu valor convertido em Kelvin.
Lembrando que 0 grau Kelvin = -273,15 Celsius.(Valores inválidos: números negativos)
'''

grau_celsius = -1

while grau_celsius < 0:
    grau_celsius = float(input('Insira o valor em Celsius: '))

print(f'Temperatura em Kelvin = {grau_celsius + 273.15:.2f} graus')
