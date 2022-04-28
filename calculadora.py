# Conceitos estudados:
# Encapsulamento privado


class Calculadora:

    def calcular(self, operacao, num1, num2):
        if operacao == '+':
            return self.__adicionar(num1, num2)
        elif operacao == '-':
            return self.__subrtrair(num2)(num1, num2)
        else:
            print('Operacao Invalida')

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subrtrair(self, num1, num2):
        return num1 - num2


calculadora = Calculadora()
resultado = calculadora.calcular('+', 2, 3)
print(resultado)
