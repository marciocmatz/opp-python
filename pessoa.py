# Conceitos estudados:
# Encapsulamento privado


class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def __apresentar_documento(self):
        print(self.__cpf)

    def beber(self, bebida):
        if self.idade >= 18:
            self.__apresentar_documento()
            print('Bebida liberada')
        else:
            print('Bebida nao liberada.')



ronaldo = Pessoa('Ronaldo', 20, '123456789')
ronaldo.beber('Cerveja')

adriano = Pessoa('Adriano', 17, '234567890')
adriano.beber('Cerveja')
