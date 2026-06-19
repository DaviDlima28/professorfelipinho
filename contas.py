num = float(input("Digite um numero: "))
num2 = float(input("Digite o segundo numero: "))

opcao = int(input("Escolha uma operação: \n 1 soma \n 2 subtração \n 3 divisão \n 4 multiplicação "))

if opcao == "1":
    (print("A soma é: ", num + num2))
elif opcao == "2":
    (print("A subtração é: ", num - num2))
elif opcao == "3":
    (print("A divisão é: ", num / num2 ))