class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado
    
    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor
        else:
            print('O valor deve ser um booleano.')

al = Alarme(False)
al.__estado  # Irá dar erro pois é um atributo privado.
al.get_estado()  # Irá exibir False
al.set_estado('Valor qualquer')  # Irá dar erro pois a validação pede um valor booleado e não string.
al.set_estado(True)  # Irá setar o valor do atributo __estado para True
al.get_estado()  # Irá exibir True
