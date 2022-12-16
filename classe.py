from lerArqivo import *

class Filme:
    __nome: str
    __diretor: str
    __ano: str
    __genero: str
    __avaliacao: str

    def __init__(self, nome, diretor, ano, genero, avaliacao):
        self.__nome = nome
        self.__diretor = diretor
        self.__ano = ano
        self.__genero = genero
        self.__avaliacao = avaliacao
    
    def get_nome(self):
        return self.__nome

    def get_diretor(self):
        return self.__diretor

    def get_ano(self):
        return self.__ano

    def get_genero(self):
        return self.__genero

    def get_avaliacao(self):
        return self.__avaliacao    