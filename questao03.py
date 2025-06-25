print("-----------------------")
print("ESCOLHA UMA OPÇÃO")
print("[1] MÉDIA DOS NÚMEROS")
print("[2] MAIOR E MENOR")
print("[3] MULTIPLICAÇÃO")
print("[4] DIVISÃO")
print("-----------------------")
opcao = int(input("Digite uma opção: "))

if(opcao == 1):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    media = float
    
    media = ((n1 + n2)/2)
    
    print("A média é %.2f" %media)
elif (opcao == 2):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    
    if(n1 > n2):
        print("O 1° número é o maior!")
    else:
        print("O 2° número é o maior!")
elif (opcao == 3):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    
    mult = int
    mult = n1 * n2
    
    print("A multiplicação é: %d" %mult)
elif (opcao == 4 ):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    
    divisao = float
    
    divisao = n1/n2
    
    print("A divisão é: %2.f" %divisao)
else:
    print("Opção inválida!!!")
    