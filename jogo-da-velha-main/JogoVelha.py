import os
import random

"""
- Jogo em turnos.
- Um jogador escolhe 'O' o outro escolhe 'X' como marcador.
- Em cada turno um jogador escolhe onde vai marcar no tabuleiro.
- Se uma linha, coluna, ou diagonal contem o mesmo marcador, o jogador que tem aquele marcador ganhou o jogo.
- Senao se todas as celulas tem algum marcador, foi empate!
- Senao, turno eh do outro jogador.

+---+---+---+
| O | X | O |
+---+---+---+
|   | X |   |
+---+---+---+
|   | O | X |
+---+---+---+
"""

def jogada(tabuleiro, nome_jogador, marcador):
    """
    Recebe a entrada do jogador um e adiciona o marcador 'X' nessa posicao

    @param tabuleiro matrix 3x3 de caracteres.
    """
    jogada_valida = False
    while not jogada_valida:
        entrada = input(f"{nome_jogador}, Digite linha e coluna:")
        valores = entrada.split(" ")

        try:
            linha = int(valores[0]) - 1
            coluna = int(valores[1]) - 1

            if linha < 0 or linha > 2:
                print("Jogada invalida, a linha deve ser entre 1-3")
            elif coluna < 0 or coluna > 2:
                print("Jogada invalida, a coluna deve ser entre 1-3")
            elif tabuleiro[linha][coluna] != ' ':
                print("Jogada invalida, posicao ja esta ocupada")
            else:
                jogada_valida = True
                tabuleiro[linha][coluna] = marcador
        except IndexError:
            print("Jogada invalida, tente novamente! Exemplo: '1 2'.")
        except ValueError:
            print("Jogada invalida, os valores devem ser inteiros!")


def jogador_ganhou(tabuleiro, marcador):
    for i in range(3):
        ganhou_linha = True
        for j in range(3):
            if tabuleiro[i][j] != marcador:
                ganhou_linha = False
                break
        if ganhou_linha:
            return True

    for i in range(3):
        ganhou_coluna = True
        for j in range(3):
            if tabuleiro[j][i] != marcador:
                ganhou_coluna = False
                break
        if ganhou_coluna:
            return True

    ganhou_diagonal_principal = True
    for i in range(3):
        if tabuleiro[i][i] != marcador:
            ganhou_diagonal_principal = False
            break

    if ganhou_diagonal_principal:
        return True

    if marcador == tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return True

    return False

def jogo_empatado(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == ' ':
                return False
    return True

tabuleiro_string = """    1   2   3  
  +---+---+---+
1 | %s | %s | %s |
  +---+---+---+
2 | %s | %s | %s |
  +---+---+---+
3 | %s | %s | %s |
  +---+---+---+"""

def mostrar(tabuleiro):
    valores = tuple((celula for linha in tabuleiro for celula in linha))
    print(tabuleiro_string % valores)

def jogo():
    nome_jogador_um = input("Nome do jogador 1: ")
    nome_jogador_dois = input("Nome do jogador 2: ")

    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    turno_jogador_um = random.randint(0, 1) == 0

    while True:
        os.system("clear")
        mostrar(tabuleiro)

        if turno_jogador_um:
            jogada(tabuleiro, nome_jogador_um, 'X')
        else:
            jogada(tabuleiro, nome_jogador_dois, 'O')

        if jogador_ganhou(tabuleiro, 'X'):
            print(f"{nome_jogador_um} GANHOU!")
            break
        elif jogador_ganhou(tabuleiro, 'O'):
            print(f"{nome_jogador_dois} GANHOU!")
            break
        elif jogo_empatado(tabuleiro):
            print("JOGO EMPATOU!")
            break

        turno_jogador_um = not turno_jogador_um

    print("")
    print("Resultado final:")
    mostrar(tabuleiro)


def main():
    while True:
        jogo()

main()
