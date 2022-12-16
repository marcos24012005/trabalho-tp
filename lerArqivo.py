import json
import os.path

nome_arquivo = 'banco json'

def lerArquivo():
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()

    if len(data) == 0:
        return []

    data = json.loads(data)
    arq.close()

    return data

def salvarArquivo(dados):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(dados, indent=4)
    arq.write(data)
    arq.close()