import os

VOTOS_BOLSONARO = 0
VOTOS_LULA = 0
VOTOS_CIRO = 0
VOTOS_SORAYA = 0
VOTOS_SIMONE = 0
BRANCOS_NULOS = 0
TOTAL = 0 
lista = ['22', '13', '12', '15', '44']
percent = []

while True:
    try:
        voto = int(input(f'Infome seu candidato: '))
        if voto == 22:
            VOTOS_BOLSONARO += 1
        elif voto == 13:
            VOTOS_LULA += 1
        elif voto == 12:
            VOTOS_CIRO += 1
        elif voto == 15:
            VOTOS_SIMONE += 1
        elif voto == 44:
            VOTOS_SORAYA += 1
        elif voto == '' and voto not in lista:
            BRANCOS_NULOS += 1
            
        else:
            pass
    except:
        BRANCOS_NULOS += 1
    
    TOTAL = VOTOS_BOLSONARO + VOTOS_LULA + VOTOS_CIRO + VOTOS_SIMONE + VOTOS_SORAYA + BRANCOS_NULOS

    os.system('cls')

    BOZO = (VOTOS_BOLSONARO / TOTAL) * 100
    LULA = (VOTOS_LULA / TOTAL) * 100
    CIRO = (VOTOS_CIRO / TOTAL) * 100
    SORAYA = (VOTOS_SORAYA / TOTAL) * 100
    SIMONE = (VOTOS_SIMONE / TOTAL) * 100
    BN = (BRANCOS_NULOS / TOTAL) * 100

    printar = f"""
Total de votos: {TOTAL}\n{"*" * 25}
Total Bolsonaro: {VOTOS_BOLSONARO} - {BOZO:,.1f}
Total Lula: {VOTOS_LULA} - {LULA:,.1f}
Total Ciro Gomes: {VOTOS_CIRO} - {CIRO:,.1f}
Total Soraya: {VOTOS_SORAYA} - {SORAYA:,.1f}
Total Simone: {VOTOS_SIMONE} - {SIMONE:,.1f}
Brancos e nulos: {BRANCOS_NULOS} - {BN:,.1f}"""
    print('*' * 25)
    print(printar)
    print('*' * 25)