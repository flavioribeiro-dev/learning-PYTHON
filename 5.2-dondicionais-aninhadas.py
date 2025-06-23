preco_maca = 2.3;
preco_laranja = 3.6;
preco_banana = 1.85;

print('1 - Maçã');
print('2 - Laranja');
print('3 - Banana');
pedido_compra = int(input('Escolha o item que deseja comprar: '));
qtde_compra = float(input('Quantos kg? '));

if(pedido_compra == 1):     # maçã
    valor_compra = preco_maca*qtde_compra;
    print(f'Subtotal: R$ {valor_compra}');
else: 
    if(pedido_compra == 2):     # laranja
        valor_compra = preco_laranja*qtde_compra;
        print(f'Subtotal: R$ {valor_compra}')
    else: 
        if(pedido_compra == 3):     # banana
            valor_compra = preco_banana*qtde_compra;
            print(f'Subtotal: R$ {valor_compra}');
        else: 
            print('Produto Inexistente');
        