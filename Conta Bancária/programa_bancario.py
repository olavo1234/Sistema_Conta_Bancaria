import math
from sys import platform
from os import system
import sistema_bancario

chamar_cliente = dict()
chamar_conta = dict()


def cadastrar_cliente():
    print('-'*30)
    print(f'  Informações do cliente nª {sistema_bancario.Conta.get_total_contas()+1}')
    print('-'*30)
    nome = str(input('Informe o seu nome: '))
    print()
    sobrenome= str(input('O seu sobrenome: '))
    print()
    cpf = str(input('Informe o seu cpf: '))

    obj = sistema_bancario.Cliente(nome=nome, sobrenome=sobrenome, cpf=cpf) 
    return obj


def criar_conta(cliente):
    print('-'*30)
    print(f'  Cadastro da conta Bancária')
    print('-'*30)
    numero = str(input('Digite o numero da conta: '))
    print()
    saldo = float(input('saldo: R$'))
    print()
    limite = float(input('limite estabelecido: R$'))

    obj = sistema_bancario.Conta(numero=numero, cliente=cliente, saldo=saldo, limite=limite)
    return obj


def criar_objetos_cliente(contador):
    ident = f'{contador}'
    novo_objeto = cadastrar_cliente()
    chamar_cliente[f'{ident}'] = novo_objeto


def criar_objetos_conta(contador):
    ident = f'{contador}'
    novo_objeto = criar_conta(chamar_cliente[f'{contador}'])
    chamar_conta[f'{ident}'] = novo_objeto


def main(numero): 
    for cont in range(1, numero+1):
        criar_objetos_cliente(cont)
        criar_objetos_conta(cont)
        limpar_tela()


def validar_input(limite1, limite2, stri1='', stri2=''):
    while True:
        string = int(input(stri1))
        if string > limite1 or string <= limite2:
            print(stri2)
        else:
            return string


def limpar_tela():
    if platform == 'win32':
        limpar = 'cls'
    else:
        limpar = 'clear'
    system(limpar)


def menu(acao):
    print(f'{acao} para:')
    for c in chamar_cliente:
            print(
                f'[{c}] - {chamar_conta.get(f'{c}').get_numero} / {chamar_cliente.get(f'{c}').get_nome}'
                f' {chamar_cliente.get(f'{c}').get_sobrenome}'
            )


numero_contas = validar_input(
    math.inf, 0, 'Digite o total de contas desejada: ', 
    'ALERTA: erro não pode ser menor que 1'
    )

main(numero_contas)

# implemetação do sistema
while True:

    print(
    """
>ESCOLHA UMA OPÇÃO<

[1] - Depositar
[2] - Sacar
[3] - Transferir
[4] - Extrato
[5] - Histórico
[6] - Ver dados pessoais
[7] - Encerrar

    """)

    escolha = validar_input(7, 0,'Escolha uma opção: ', 'INVÁLIDO: somente número de 1 a 7: ')
    print('-'*30)

    if escolha == 1:
        menu('Depositar')
        print('-'*30)
        conta_opcao = validar_input(numero_contas, 0, 'Escolha uma conta: ', 'Conta Inválida, tente novamente!: ')
        print('-'*30)
        valor = float(input('Valor do deposito: R$'))
        print('-'*30)
        try:
            chamar_conta.get(f'{conta_opcao}').depositar(valor)
            print('<DEPOSITO FEITO COM SUCESSO!>')
        except ValueError:
            print('ALERTA: O valor que você digitou ultrapassou o límite')
        _ = str(input('Voltar ->')).strip()
        limpar_tela()

    elif escolha == 2:
        menu('Sacar')
        print('-'*30)
        conta_opcao = validar_input(numero_contas, 0, 'Escolha uma conta: ', 'Conta Inválida, tente novamente!: ')
        print('-'*30)
        valor = float(input('Valor do saque: R$'))
        print('-'*30)
        try:
            chamar_conta.get(f'{conta_opcao}').sacar(valor)
            print('<SAQUE FEITO COM SUCESSO!>')
        except ValueError:
            print('ALERTA: O valor que você digitou ultrapassou o seu saldo')
        _ = str(input('Voltar ->')).strip()
        limpar_tela()

    elif escolha == 3:
        menu('transferir')
        print('-'*30)
        autor = validar_input(numero_contas, 0, 'Da conta: ', 'Conta Inválida, tente novamente!: ')
        conta_opcao = validar_input(numero_contas, 0, 'Para a conta: ', 'Conta Inválida, tente novamente!: ')
        if autor == conta_opcao:
            print('ALERTA: a transferência não será feita para a mesma pessoa')
            _ = str(input('Deseja voltar ->')).strip()
            limpar_tela()
            continue
        elif numero_contas == 1:
            print('ALERTA: a conta não será feita com só um usuário')
        print('-'*30)
        valor = float(input('Valor do tarnsferência: R$'))
        print('-'*30)
        try:
            chamar_conta.get(f'{autor}').transfere_para(chamar_conta.get(f'{conta_opcao}'), valor)
            print('<TRANSFERÊNCIA FEITO COM SUCESSO!>')
        except ValueError:
            print('ALERTA: O valor que você digitou ultrapassou o seu saldo/limite')
        _ = str(input('Voltar ->')).strip()
        limpar_tela()

    elif escolha == 4:
        menu('Extrato')
        print('-'*30)
        conta_opcao = validar_input(numero_contas, 0, 'Extrato da conta: ', 'Conta Inválida, tente novamente!: ')
        print('-'*30)
        limpar_tela()
        print()
        print('-'*25)
        chamar_conta.get(f'{conta_opcao}').extrato()
        print('-'*25)
        _ = str(input('voltar ->')).strip()
        limpar_tela()

    elif escolha == 5:
        menu('Histórico')
        print('-'*30)
        conta_opcao = validar_input(numero_contas, 0, 'Solicitar histórico da conta: ', 'Conta Inválida, tente novamente!: ')
        print('-'*30)
        limpar_tela()
        print()
        print('-'*35)
        chamar_conta.get(f'{conta_opcao}').historico.imprime()
        print('-'*35)
        _ = str(input('Voltar ->')).strip()
        limpar_tela()

    elif escolha == 6:
        menu('Ver dados')
        print('-'*30)
        conta_opcao = validar_input(numero_contas, 0, 'Solicitar dados da conta: ', 'Conta Inválida, tente novamente!: ')
        print('-'*30)
        limpar_tela()
        print()
        print('-'*30)
        print(
            f'Nome: {chamar_cliente.get(f'{conta_opcao}').get_nome}\n'
            f'Sobrenome: {chamar_cliente.get(f'{conta_opcao}').get_sobrenome}'
            f'\nCPF: {chamar_cliente.get(f'{conta_opcao}').get_cpf}'
            
            )
        print('-'*30)
        print()
        _ = str(input('Voltar ->')).strip()
        limpar_tela()

    elif escolha == 7:
        limpar_tela()
        print('<<PROGRAMA FECHADO>>')
        print('-VOLTE SEMPRE-')
        break
