import datetime


class Historico:
# classe que chama uma lista de 
# movimentação da conta

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self._transacoes = list()


# lista está sendo protegida por encapsulamento 
    @property
    def get_transacao(self):
        return self._transacoes


    @get_transacao.setter
    def set_transacao(self, novo_dado):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)


    def imprime(self):
        print(f'Data abertura: {self.data_abertura}')
        print('Transação: ')
        for t in self._transacoes:
            print('-', t)



class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf


    @property
    def get_nome(self):
        return self._nome


    @get_nome.setter
    def set_nome(self, novo_nome):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)


    @property
    def get_sobrenome(self):
        return self._sobrenome


    @get_sobrenome.setter
    def set_sobrenome(self, novo_sobr):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)


    @property
    def get_cpf(self):
        return self._cpf


    @get_cpf.setter
    def set_cpf(self, novo_cpf):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)



class Conta:

    __total_contas = 0

    def __init__(self, numero, cliente, saldo=0, limite=0):
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        self._titular = cliente 
        self.historico = Historico()
        type(self).__total_contas += 1


    @classmethod
    def get_total_contas(cls):
        return cls.__total_contas


    @property
    def get_numero(self):
        return self._numero


    @get_numero.setter
    def set_numero(self, novo_numero):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)


    @property
    def get_titular(self):
        return self._titular


    @get_titular.setter
    def set_titular(self, novo_titular):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)


    @property
    def get_limite(self):
        return self._limite


    @get_limite.setter
    def set_limite(self, novo_limite):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)


    @property
    def get_saldo(self):
        return self._saldo


    @get_saldo.setter
    def set_saldo(self, novo_saldo):
        try:
            raise ValueError('ERROR: impossivel trocar valores pessoais')
        except ValueError as er:
            print(er)


    def confirmar_acao(self, tipoDeProcesso, valor=0):
        if tipoDeProcesso == 'depositar': 
            if valor < self._limite and self._saldo < self._limite:
                self._saldo += valor
                self.historico.get_transacao.append(f'Deposito de {valor}')
                return True
            else:
                raise ValueError('ALERTA: (erro: VALUE INVALID_depositar)')
        elif tipoDeProcesso == 'sacar':
            if self._saldo >= valor:
                self._saldo -= valor
                self.historico.get_transacao.append(f'Saque de {valor}')
                return True
            else:
                raise ValueError('ALERTA: (erro: VALUE INVALID_sacar)')


    def depositar(self, valor):
        return self.confirmar_acao('depositar', valor)


    def sacar(self, valor):
        return self.confirmar_acao('sacar', valor)


    def transfere_para(self, destino, valor):
        regua_limite = destino._saldo
        if regua_limite + valor > destino._limite:
            raise ValueError('ERROR: sistema_bancario.py(L: 181/182)')
        else:
            retiro = self.sacar(valor)
            self.historico.get_transacao.pop()
            if retiro:
                self.historico.get_transacao.append(
                    f'Transferencia para {destino.get_titular.get_nome}'
                    f' {destino.get_titular.get_sobrenome} de valor: {valor}'
                )
                destino.historico.get_transacao.append(
                    f'Transferencia feita de {self.get_titular.get_nome}'
                    f' {self.get_titular.get_sobrenome} de valor: {valor}'
                )
                destino.depositar(valor)
                destino.historico.get_transacao.pop()


    def extrato(self):
        print(f'Número: {self._numero}\nSaldo: {self._saldo}\nLimite: {self._limite}')
        self.historico.get_transacao.append(
            f'Tirou extrato = saldo de {self._saldo}'
        )

