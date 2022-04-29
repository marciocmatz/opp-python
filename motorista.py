# Em Python podemos tipar o tipo de dado a ser inserido, no entanto, essa tipagem é do tipo fraca.
# Ou seja, não necessariamente é preciso seguir o que foi tipado.

class Motorista:

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print(f'Dirigindo um {veiculo}')

    def cantar(self) -> None:
        print('Lalala')

    def apresentar_idade(self) -> int:
        return self.idade