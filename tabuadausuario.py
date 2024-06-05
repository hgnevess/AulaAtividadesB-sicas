numero = int(input("Digite um numero qualquer para saber sua tabuada: "))
contador = 0 
while contador <= 10 :
    resultado = numero*contador
    print('{} x {} = {}'.format(numero, contador, resultado))
    contador+=1