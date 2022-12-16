import os
import json
from classe import Filme
nome_arquivo = "filmes.json"


def lerArquivo() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)


def salvarArquivo(filmes: list):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(filmes, indent=4)
    arq.write(data)
    arq.close()


def cadastrarFilme() -> dict:
    filme = {}
    filme['nome'] = input('Nome do Filme: ')
    filme['diretor'] = input(f'Qual é o Diretor? ')
    filme['ano'] = input('Ano do filme: ')
    filme['genero'] = input('Qual o gênero? ')
    filme['avaliacao'] = input('Qual a avaliação do filme (max 5 estrelas)? ')
    novoFilme = Filme(nome, diretor, ano, genero, avaliacao)
    filme['nome'] = novoFilme.get_nome()
    filme['diretor'] = novoFilme.get_diretor()
    filme['ano'] = novoFilme.get_ano()
    filme['genero'] = novoFilme.get_genero()
    filme['avaliacao'] = novoFilme.get_avaliacao()
    return filme


filmes = lerArquivo()
filmes.append(filme)
salvarArquivo(filmes)


def menu():
    os.system('clear')
    print(10 * '-=-')
    print('1 - Cadastrar Filme')
    print('2 - Ver Filmes')
    print('3 - Alterar filme')
    print('4 - Selecionar por Atributo')
    print('5 - Deletar Filme')
    print('6 - Sair')
    print(10 * '-=-')
    return int(input('Escolha uma opção: '))


def mostrarFilmes():
    os.system('clear')
    print(10 * '-=-')
    filmes = lerArquivo()
    for filme in filmes:
        print(f'Nome do Filme : {filme["nome"]}')
        print(f'Diretor : {filme["diretor"]}')
        print(f'Ano : {filme["ano"]}')
        print(f'Gênero : {filme["genero"]}')
        print(f'Avaliação : {filme["avaliacao"]}')
        print(10 * '-=-')
    input('Pressione ENTER para continuar...')
