from trabalho import *

while True:
    opcao = menu()
    if opcao == 1:
        cadastrarFilme()
    elif opcao == 2:
        mostrarFilmes()
    elif opcao == 3:
        os.system('clear')
        break