
largura_quadra = float(input('Largura da quadra: '))
comprimento_quadra = float(input('Comprimento da quadra: '))

area_quadra = largura_quadra * comprimento_quadra
print(f'Area da quadra é {area_quadra}')

largura_ceramica = float(input('Largura da ceramica: '))
comprimento_ceramica = float(input('Comprimento da ceramica: '))

area_ceramica = largura_ceramica * comprimento_ceramica
print(f'Area da ceramica é {area_ceramica}')

total_ceramicas = area_quadra // area_ceramica
#total_ceramicas = int(area_quadra / area_ceramica)

print(f'O total de ceramicas inteiras é {total_ceramicas}')



