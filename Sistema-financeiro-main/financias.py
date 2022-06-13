from datetime import datetime
import json

try:
    with open('carteira.json', 'r') as arquivo:
        carteira = json.loads(arquivo.read())
    id_transacao = carteira["id_transacao"]
    carteira.pop("id_transacao")
except:
    carteira = {}
    id_transacao = 1

def listarTransacoes():
    if len(carteira == 0):
        print('\nSem transação!!!')
        return
    print('Suas transações: ')
    for transacao in sorted(
        carteira.values(),
        key = lambda: str(transacao["Identificador"]),
        reverse = True
    ):
        print(f'{transacao["indentificdor"]} - {transacao["data"]} - {transacao["descricao"]}: R${transacao["valor"]:.2f}')

def adicionarTransacao():
    global id_transacao

    descricao = input('\nDigite a descrição da transação: ')
    try:
        valor = float(input('Digite o valor da transação (com sinal de - se for despesas): '))
    except:
        print('Informe um valor real/float!!!')
    data = str(datetime.now())

    transacao = {
        'valor': valor,
        'descricao': descricao,
        'data' : data,
        'identificador': str(id_transacao)
    }

    carteira['id_' + str(id_transacao)] = transacao
    id_transacao += 1
    print('Transação adicionada com sucesso!!!')

def deletarTransacao():
    identificador = "id_" + input('\nDigite o ID da transação que deseja deletar: ')
    transacao = carteira.pop(identificador)

    print(f'Transação {transacao["indentificdor"]} - {transacao["descricao"]}, no valor de R${transacao["valor"]:.2f} foi excluída!!!')

def editarTransacao():
    id_transacao = int(input('\nDigite o ID da transação que quer editar: '))
    identificador = "id_" + str(id_transacao)    

    descricao = input('\nDigite a nova descrição da transação: ')
    try:
        valor = float(input('Digite o novo valor da transação (com sinal de - se for despesas): '))
    except:
        print('Informe um valor real/float!!!')
    nova_data = input('Digite S para mudar a data de transição para atual ou N para manter data antiga: ').upper()
    if nova_data == "S":
        data = str(datetime.now())
    else:
        data = carteira[identificador]["data"]
    
    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "identidicador": id_transacao
    }
    carteira["id_" + str(id_transacao)] = transacao
    print(f'Transação {id_transacao} editada com sucesso!!!')

def consultarSaldo():
    saldo = 0
    for transacao in carteira.values():
        saldo += transacao["valor"]
    print(f'\nSeu saldo atual é R${saldo:.2f}')

def salvarCarteira():
    c = carteira.copy()
    c["id_transacao"] = id_transacao
    with open('carteira.json', 'w') as arquivo:
        arquivo.write(json.dumps(c))

def main():
    while True:
        op = input("""\nDigite:
        \rL - Listar transações
        \rA - Acidionar transações
        \rD - Deletar transações
        \rE - Editar transações
        \rC - Consultar transações
        \rQ - Sair do programa
        \rS - Salvar transações    
        \rSua entrada: 
        """).upper()

        if op == 'A':
            adicionarTransacao()
            salvarCarteira()

        elif op == 'E':
            editarTransacao()
            salvarCarteira()    

        elif op == 'D':
            deletarTransacao()
            salvarCarteira()   

        elif op == 'C':
            consultarSaldo()

        elif op == 'L':
            listarTransacoes()

        elif op == 'S':
            salvarCarteira()

        elif op == 'Q':
            exit()

        else:
            print('Operação inválida')

main()