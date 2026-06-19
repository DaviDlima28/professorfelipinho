num = float(input("Digite um numero: "))
num2 = float(input("Digite o segundo numero: "))

while True:
    print("Escolha uma operação: \n 1 soma \n 2 subtração \n 3 divisão \n 4 multiplicação ")

    opcao = input("Sua opção: ") 
    
    if opcao == "1":
        (print("A soma é: ", num + num2))
        break
    elif opcao == "2":
        (print("A subtração é: ", num - num2))
        break
    elif opcao == "3":
        if num2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            (print("A divisão é: ", num / num2 ))
        break
    elif opcao == "4":
        (print("A multiplicação é ", num * num2))
        break
    else: 
        print("opção invalida, escolha uma das 4 operações disponiveis")