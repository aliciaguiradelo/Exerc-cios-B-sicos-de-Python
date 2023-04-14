#Criando classe Aluno já inicializando seus atributos com construtor padrão e valor default
class Aluno:
    def __init__(self, id = '', nome = '', idade = 0, ra = '', curso = ''):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__ra = ra
        self.__curso = curso
    #Invés de getters e setters usamos @properties
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    @property
    def ra(self):
        return self.__ra
    @ra.setter
    def ra(self, ra):
        self.__ra = ra
    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self, curso):
        self.__curso = curso