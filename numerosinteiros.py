positivos = 0
negativos = 0

for i in range(20):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor > 0:
        positivos += valor
    elif valor < 0:
        negativos += 1

print(f'Postivos: {positivos}')
print(f'Negativos: {negativos}')
