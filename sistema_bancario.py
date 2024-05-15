def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # keyword only
    if numero_saques >= limite_saques:
        print("Saque não realizado. Número máximo de saques excedido.\n")
    elif valor > saldo:
        print("Saque não realizado. Saldo insuficiente.\n")
    elif valor < 0 or valor > limite:
        print("Saque não realizado. Valor inválido.\n")
    else:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.\n")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /): # positional only
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.\n")
    else:
        print("Depósito não realizado. Valor inválido.\n")    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato): # positional only (saldo) e keyword only (extrato)
    print("\n--------- EXTRATO ---------\n")
    print("Não houve movimentações nesta conta." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}\n")
    print("---------------------------\n")

def cadastrar_usuario(lista_usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = buscar_usuario(cpf, lista_usuarios)
    
    if usuario:
        print("Não foi possível cadastrar o cliente. CPF já cadastrado.\n")
    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite seu endereço (logradouro, número - bairro - cidade / sigla do estado): ")
    
    lista_usuarios.append({"nome" : nome, "data de nascimento" : data_nascimento, "cpf" : cpf, "endereco" : endereco})
    print("Usuário cadastrado com sucesso.\n")

def cadastrar_conta_corrente(agencia, numero_conta, lista_usuarios, lista_contas):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = buscar_usuario(cpf, lista_usuarios)

    if usuario:
        lista_contas.append({"agência" : agencia, "número da conta" : numero_conta, "usuário" : usuario})
        print("Conta criada com sucesso.\n")
    else:
        print("Não foi possível criar a conta. Usuário não encontrado.\n")

def exibir_contas(lista_contas):
    for conta in lista_contas:
        imprimir = f'''
Agência:\t{conta["agência"]}
Conta:\t\t{conta["número da conta"]}
Titular:\t{conta["usuário"]["nome"]}
'''
        print(imprimir)
        print("-" * 30)

def buscar_usuario(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def menu():
    menu = '''
MENU
(1) Sacar
(2) Depositar
(3) Extrato
(4) Cadastrar usuário
(5) Cadastrar conta corrente
(6) Exibir contas cadastradas
(0) Sair

Opção escolhida: '''
    return float(input(menu))

def main():
    # constantes
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # variáveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    # listas
    lista_usuarios = []
    lista_contas = []

    while True:
        opcao = menu()

        if opcao == 1: # sacar
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 2: # depositar
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 3: # exibir extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4: # cadastrar cliente
            cadastrar_usuario(lista_usuarios)
        
        elif opcao == 5: # cadastrar conta
            numero_conta = len(lista_contas) + 1
            cadastrar_conta_corrente(AGENCIA, numero_conta, lista_usuarios, lista_contas)
        
        elif opcao == 6: # exibir contas cadastradas
            exibir_contas(lista_contas)
        
        elif opcao == 0: # sair
            print("Programa encerrado.\n")
            break
        
        else:
            print("Opção inválida.\n")

main()