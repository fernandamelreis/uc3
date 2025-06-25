print("-----------------------")
print("ESCOLHA UMA OPÇÃO")
print("[1] ADIÇÃO")
print("[2] SUBTRAÇÃO")
print("[3] MULTIPLICAÇÃO")
print("[4] DIVISÃO")
print("-----------------------")
opcao = int(input("Digite uma opção: "))

if(opcao == 1):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    soma = int
    
    soma = (n1 + n2)
    
    print("A soma é %d" %soma)
elif (opcao == 2):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    
    sub = int
    
    sub = (n1 - n2)
    
    print("A subtração é: %d" %sub)
    
elif (opcao == 3):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    
    mult = int
    mult = (n1 * n2)
    
    print("A multiplicação é: %d" %mult)
    
elif (opcao == 4 ):
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))
    
    divisao = float
    
    divisao = (n1/n2)
    
    print("A divisão é: %2.f" %divisao)
else:
    print("Opção inválida!!!")
    