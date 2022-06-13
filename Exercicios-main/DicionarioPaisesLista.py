estado = {}
brasil = []

for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()