# Conceitos estudados: 
# Classes
# Atributos
# Métodos
# Contexto


class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal +1')

    def voltar_canal(self):
        print('Canal -1')

    def escolher_canal(self, canal):
        print(f'Alterado para o canal {canal}')


controleSala = ControleRemoto('SONY', 'Sala')
controleQuarto = ControleRemoto('LG', 'Quarto')

print(controleSala.televisao)
print(controleSala.comodo)

controleSala.avancar_canal()
controleSala.voltar_canal()
controleQuarto.escolher_canal('ESPN')
