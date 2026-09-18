def cadastrar():
    nome = input("Digite o nome do cliente:\n ")

    cpf = input("Digite o CPF do cliente:\n ")

    while len(str(cpf)) != 11:
      
        print("O CPF deve conter 11 dígitos. Por favor, tente novamente.")
        cpf = (input("Digite o CPF do cliente (somente números):\n "))

    idade = int(input("Digite a idade do cliente:\n "))

    return nome, cpf, idade



def criar_conta(nome, cpf, idade, numero_conta):
    if nome == None or cpf == None or idade == None:
        print("O cliente não pode criar uma conta, pois não possui todas as informações do cadastro.")
        return None
    else:
        print(f"Criando conta para o cliente {nome} ...\n\n\n")
        saldo = 0.0
        saldo = float(input("Digite o saldo inicial da conta:\n "))
        print(f"Conta criada com sucesso para o cliente {nome}\n")
        print(f"Informações da conta:\n Nome: {nome}\n CPF: {cpf}\n Idade: {idade}\n Saldo: {saldo}\n Conta: {numero_conta}\n\n\n")

    return nome, cpf, idade, saldo, numero_conta



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
     
def procurar_cliente(clientes, cpf):
    i = 0

    while i < len(clientes):
        if clientes[i][1] == cpf:
            return clientes[i]

        i += 1

    return None

def procurar_conta(contas, numero):
    i = 0

    while i < len(contas):
        if contas[i][4] == numero:
            return contas[i]

        i += 1

    return None

def listar_contas(contas):
    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
    else:
        print("\n===== CONTAS CADASTRADAS =====")

        i = 0

        while i < len(contas):
            print(f"Conta: {contas[i][4]}")
            print(f"Nome: {contas[i][0]}")
            print(f"CPF: {contas[i][1]}")
            print(f"Idade: {contas[i][2]}")
            print(f"Saldo: R$ {contas[i][3]:.2f}")
            print("-----------------------------")

            i += 1     

     
def main():
    clientes = []
    contas = []
    numero_conta = 1001
    opcao = 0


    print(" Bem- vindo ao Banco Dcomp! \n")

    while opcao != 8:

      opcao = int(input("Digite a opção desejada:\n 1 - Cadastrar cliente\n 2 - Criar conta\n 3 - Listar contas\n 4 - Procurar conta\n 5 - Consultar saldo\n 6 - Depositar\n 7 - Sacar\n 8 - Sair\n"))

      if opcao == 1:
        cliente = cadastrar()
        clientes.append(cliente)

      elif opcao == 2:
          cpf = input("Digite o CPF do cliente:\n ")
          cliente = procurar_cliente(clientes, cpf)

          if cliente == None:
            print("Cliente não encontrado.")
          else:
            conta = criar_conta(
            cliente[0],
            cliente[1],
            cliente[2],
            numero_conta
        )

          if conta != None:
            contas.append(conta)
            numero_conta += 1
            
      elif opcao == 3:
        listar_contas(contas)

      elif opcao == 4:
       numero = int(input("Digite o número da conta:\n "))
       conta = procurar_conta(contas, numero)

       if conta == None:
          print("Conta não encontrada.")
       else:
          print(f"Conta: {conta[4]}")
          print(f"Nome: {conta[0]}")
          print(f"CPF: {conta[1]}")
          print(f"Idade: {conta[2]}")
          print(f"Saldo: R$ {conta[3]:.2f}")

      elif opcao == 5:
       numero = int(input("Digite o número da conta:\n "))
       conta = procurar_conta(contas, numero)

       if conta == None:
        print("Conta não encontrada.")
       else:
        mostrar_saldo(conta[3])

      elif opcao == 6:
           numero = int(input("Digite o número da conta:\n "))
           conta = procurar_conta(contas, numero)

           if conta == None:
            print("Conta não encontrada.")
           else:
            conta[3] = depositar(conta[3])

      elif opcao == 7:
       numero = int(input("Digite o número da conta:\n "))
       conta = procurar_conta(contas, numero)

       if conta == None:
         print("Conta não encontrada.")
       else:
        conta[3] = sacar(conta[3])
      elif opcao == 8:
        print("Saindo do sistema...") 

if __name__ == "__main__":
    main()