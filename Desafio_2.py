def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        return saldo, extrato, "Número máximo de saques diários atingido."
    if valor <= 0:
        return saldo, extrato, "Valor inválido. Tente novamente."
    if valor > saldo:
        return saldo, extrato, "Saldo insuficiente."
    if valor > limite:
        return saldo, extrato, "O valor do saque excede o limite."

    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    return saldo, extrato, "Saque realizado com sucesso!"

def depositar(saldo, valor, extrato):
    if valor <= 0:
        return saldo, extrato, "Valor inválido. Tente novamente."

    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato, "Depósito realizado com sucesso!"

def exibir_extrato(saldo, *, extrato):
    movimentacoes = extrato if extrato else "Não foram realizadas movimentações."
    return f"\n=== Extrato ===\n{movimentacoes}\nSaldo atual: R$ {saldo:.2f}\n================"

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        return "Usuário já cadastrado."

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    return "Usuário cadastrado com sucesso!"

def criar_conta_corrente(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if not usuario:
        return "Usuário não encontrado."

    numero_conta = len(contas) + 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    return f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}!"

def listar_contas(contas):
    if not contas:
        return "Nenhuma conta cadastrada."

    resumo = "\n=== Contas Cadastradas ===\n"
    for conta in contas:
        resumo += (f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, "
                   f"Titular: {conta['usuario']['nome']}\n")
    return resumo

def main():
    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor para depósito: R$ "))
            saldo, extrato, mensagem = depositar(saldo, valor, extrato)
            print(mensagem)

        elif opcao == "s":
            valor = float(input("Informe o valor para saque: R$ "))
            saldo, extrato, mensagem = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                             limite=limite, numero_saques=numero_saques,
                                             limite_saques=LIMITE_SAQUES)
            if "sucesso" in mensagem:
                numero_saques += 1
            print(mensagem)

        elif opcao == "e":
            print(exibir_extrato(saldo, extrato=extrato))

        elif opcao == "nu":
            print(criar_usuario(usuarios))

        elif opcao == "nc":
            print(criar_conta_corrente(AGENCIA, contas, usuarios))

        elif opcao == "lc":
            print(listar_contas(contas))

        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário!")
            break

        else:
            print("Operação inválida. Por favor, selecione novamente.")

if __name__ == "__main__":
    main()
