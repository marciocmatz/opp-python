# Responsabilidade Única: de maneira resumida um método deve ser responsável apenas por uma coisa dentro do código.

# Do modo que essa classe foi criada, toda a responsabilidade de cadastrar um usuário está dentro de um só método.
class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando banco de dados')
            print(f'Cadastrando usuário {nome} que tem {idade} anos.')
        else:
            print('Dados inválidos.')

############################################################################
############################################################################

# Já essa classe, está respeitando o principio da responsabilidade única, onde cada método tem uma função específica dentro do cadastro. 
# Aqui será mais possível de arrumar algo no código caso um dia seja necessário.
class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_dados(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else: 
            return False

    def __armazenar_dados(self, nome: str, idade: int) -> bool:
        print('Acessando banco de dados')
        print(f'Cadastrando usuário {nome} que tem {idade} anos.')

    def __indicar_erro(self) -> None:
        print('Dados inválidos.')

# Agora imagine que é possível abstrair ainda mais métodos, transformando eles em outras classes.
# Tudo isso ajuda na hora de refatorar e também na hora de reutilizar código.
