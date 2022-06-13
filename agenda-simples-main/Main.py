def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input("""
        ==================================
                Projeto Agenda Python
        Menu:
        [1] Cadastrar contato
        [2] Listar contato
        [3] Deletar contato
        [4] Buscar contato pelo nome
        [5] Sair da agenda
        ==================================
        Escolha uma das opções acima:
        """)
        while opcao != '5':
            if opcao == '1':
                cadastrarContato()
            elif opcao == '2':
                listarContato()
            elif opcao == '3':
                deletarContato()
            elif opcao == '4':
                buscarContatoPeloNome()
            else:
                sair()
        voltarMenuPrincipal = input('Voltar ao menu principal [S/N]').lower()

def cadastrarContato():
    idContato = input('\nEscolha o ID do contato: ')
    nome = input('Escreva o nome do contato: ').title()
    telefone = input('Escreva o telefone do contato: ')
    email = input('Escreva o email do contato: ')
    try:
        agenda = open('agenda.txt', 'a')
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'!!!!!!Contato gravado com sucesso!!!!!!')
    except:
        print('ERRO na gravação do contato!')
    
def listarContato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nome = input('Digite o nome a deletar: ').lower()
    agenda = open('agenda.txt', 'r')
    auxiliar = []
    auxiliar_2 = []
    for i in agenda:
        print(i)
        auxiliar.append(i)
    for i in range(0, len(auxiliar)):
        if nome not in auxiliar[i].lower():
            auxiliar_2.append(auxiliar[i])
    agenda = open('agenda.txt','w')
    for i in auxiliar_2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    listarContato()

def buscarContatoPeloNome():
    nome = input(f'Nome a ser procurado: ').upper()
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        if nome == contato.split(';')[1].upper():
            print(contato)
    agenda.close()

def sair():
    exit()

def main():
    menu()

main()

