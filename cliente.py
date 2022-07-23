class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # aqui, a função aponta diretamente para o atributo "nome". Então ao colocarmos o @property
    # não há necessidade de colocar os () na hora de excecutar a função.
    # é como se estivéssemos chamando o atributo diretamente, mas antes, passamos pela função.
    @property
    def nome(self):
       return self.__nome.title()

    @nome.setter # aqui podemos modificar o nome diretamente, acessando o atributo
    def nome(self, nome):
        self.__nome = nome

