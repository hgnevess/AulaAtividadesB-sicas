
soma = 0
contador = 0
for i in range(100, 501):  
    if i % 2!= 0:  
        soma += i
        contador += 1
media = soma / contador
print("Soma dos valores ímpares:", soma)
print("Média dos valores ímpares:", media)