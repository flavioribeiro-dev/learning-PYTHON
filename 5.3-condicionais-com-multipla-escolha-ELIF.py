# Estrutura ELIF = ELSE + IF -> EL+IF
preco_maca = 2.3;
preco_laranja = 3.6;
preco_banana = 1.85;

print('Escolha o produto: ');
print('1 - Maçã   //   2 - Laranja   //   3 - Banana');
produto = int(input("Qual sua escolha? "));
qtde_produto = float(input('Informe a quantidade: '));

if(produto == 1):   # maçã
    subtotal = qtde_produto * preco_maca;
    print(f'Subtotal: R$ {subtotal}');
elif (produto == 2):    # laranja
    subtotal = qtde_produto * preco_laranja;
    print(f'Subtotal: R$ {subtotal}');
elif (produto == 3):    # banana
    subtotal = qtde_produto * preco_banana;
    print(f'Subtotal: R$ {subtotal}');
else:
    print('Produto inexistente!');

nome = input('Qual o seu nome? ');
if (nome=="flavio" or nome=="Flavio" or nome=='flávio' or nome=="Flávio"):
    print("Usuário logado!!!");
else: 
    idade = int(input('Qual a sua idade? '));
    if (idade<18):
        print('Você não pode ter acesso a essas informações!');
    else:
        print(f'Por favor, Sr(a). {nome}, aguarde um momento!')
