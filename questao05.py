salario = float(input("Digite o seu salário: "))

if (salario <= 800):
    print("Você tem direito ao aumento de 35%")
    salario_reaj =  float
    
    salario_reaj = (salario + (salario*0.35))
    print("Salario reajustado é: R$ %.2f" %salario_reaj)
elif (salario > 800):
    print("Você tem direito ao aumento de 15%!")
    salario_reaj =  float
    
    salario_reaj = (salario + (salario*0.15))
    print("Salario reajustado é: R$ %.2f" %salario_reaj)
    