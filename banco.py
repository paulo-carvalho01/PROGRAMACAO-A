def cadastrar():
    nome = input("Digite o nome do cliente:\n ")

    cpf = input("Digite o CPF do cliente:\n ")

    while len(str(cpf)) != 11:
      
        print("O CPF deve conter 11 dígitos. Por favor, tente novamente.")
        cpf = (input("Digite o CPF do cliente (somente números):\n "))

    idade = int(input("Digite a idade do cliente:\n "))

    return nome, cpf, idade



def criar_conta(nome, cpf, idade):
    if nome == None or cpf == None or idade == None:
        print("O cliente não pode criar uma conta, pois não possui todas as informações do cadastro.")
        return None
    else:
        print(f"Criando conta para o cliente {nome} ...\n\n\n")
        saldo = 0.0
        conta = 123456789-10
        saldo = float(input("Digite o saldo inicial da conta:\n "))
        print(f"Conta criada com sucesso para o cliente {nome}\n")
        print(f"Informações da conta:\n Nome: {nome}\n CPF: {cpf}\n Idade: {idade}\n Saldo: {saldo}\n Conta: {conta}\n\n\n")

    return nome, cpf, idade, saldo, conta



def mostrar_saldo(saldo):
            print(f"O saldo atual da conta é: R$ {saldo:.2f}")

            return saldo


def depositar(saldo):
    valor = float(input("Digite o valor a ser depositado:\n"))
    saldo += valor
    print(f"Deposito realizado, saldo atual:\n R$ {saldo:.2f}")

    return saldo

def sacar(saldo):
     valor = float(input("Digite o valor que deseja sacar:\n"))
     if valor > saldo:
          print(f"O valor que deseja sacar é maior que o saldo atual: {saldo:.2f}\n tente novamente.")
     else:
          saldo -= valor
          print(f"Saque realizado com sucesso!!")

          return saldo

     
def main():
 nome = None
 cpf = None
 idade = None
 conta = None
saldo = 0.0
opcao = 0

print(" Bem-vindo ao Banco Dcomp! \n")

while opcao != 6:

    opcao = int(input("Digite a opção desejada:\n 1 - Cadastrar cliente\n 2 - Criar conta\n 3 - Mostrar saldo\n 4 - Depositar\n 5 - Sacar\n 6 - Sair\n"))

    if opcao == 1:
        nome, cpf, idade = cadastrar()
    elif opcao == 2:
        criar_conta(nome, cpf, idade)
    elif opcao == 3:
        mostrar_saldo(saldo)
    elif opcao == 4:
        depositar(saldo)
    elif opcao == 5:
        sacar(saldo)
    elif opcao == 6:
        print("Saindo do sistema...")


if __name__ == "__main__":
    main()

