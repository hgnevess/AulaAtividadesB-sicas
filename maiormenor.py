contador = 0
while contador <= 5:
    num1= int(input("Digite o numero 1: "))
    num2= int(input("Digite o numero 2: "))

    if num1 > num2:
        print("O maior numero é o {}".format(num1))
    else:
        print("O maior numero é o {}".format(num2))

