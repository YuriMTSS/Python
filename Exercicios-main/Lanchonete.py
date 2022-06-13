"""O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado."""

lanches = [ 
    [ 'Cachorro quente', 100, 1.20, 30],
    [ 'Bauru simples', 101, 1.30, 45],
    [ 'Bauru com ovo', 102, 1.50, 45],
    [ 'Hamburger', 103, 1.20, 50],
    [ 'Cheeseburguer', 104, 1.30, 60],
    [ 'Refrigerante', 105, 1.00, 120]
]

lpedidos = []
planche=0
total = 0

pedido = input('Lanche e quantidade: ')
while pedido :
    codigo,quant = pedido.split();
    codigo = int(codigo);
    quant = int(quant);
    
    for e in lanches :
        if codigo in e:
            if e[3] > quant :
                planche = quant * e[2]
                lpedidos.append('\t{1} x {0} = {2:.2f}'.format(e[0], quant, planche))
                e[3] = e[3] - quant
            elif e[3] == 0 :
                print('\t{0} acabou !!!'.format(e[0]))
            else :
                print('\tSó tem mais {1} x {0} !!!!'.format(e[0],e[3]))
            break

    if planche == 0:
        print ('Codigo invalido.')
        
    # Soma ao total
    total = total + planche
    
    pedido = input('Lanche e quantidade: ')
    planche=0

print ('\n\nPedido Final:')
for e in lpedidos:
    print(e)
print ('Total: R$ {0:.2f}'.format(total) )


