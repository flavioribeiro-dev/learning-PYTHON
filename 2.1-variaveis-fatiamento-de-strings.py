ling = 'lógica de programação e algoritmos';
nome = 'Flávio'

# Selecionando a quantidade de itens de uma string:
print( len(nome) );

# Selecionando parte de uma String:
print(nome[0:6]);

# Variação da forma de seleção da quantidade de elementos de uma string com a quantidade de elementos de uma variável:
print(ling[24:len(ling)]);
print( nome[0:len(nome)] );

# Seleção de uma parte da string a partir de seu último elemento:
print(ling[-10:len(ling)]);

# Selecionando elementos de forma simplificada a partir de sua POSIÇÃO INICIAL ou FINAL, respectivamente:
print(nome[:3]);
print(nome[3:]);

