# Atribuição de Variáveis:
nome = 'Flavio';
idade = 90;
nota = 8.5;
job = 'dev fullstack'

# Composição de strings e variáveis com MARCADORES DE POSIÇÃO:
print('Meu nome é %s, tenho %i anos e tirei nota %.2f' %(nome, idade, nota))
print('Meu nome é %s, tenho %i anos e tirei nota %.2f' %(nome, nota, idade))
# ---- É necessário que o nome das variaveis esteja na mesma ordem de sua indicação com o marcador %

# Composição moderna de strings e variáveis:
print('Meu nome é {} e trabalho como {}' .format(nome, job))
# ---- Dessa forma, não preciso me preocupar com o tipo da variável e incorre menos em erros

# Método moderno ainda mais simplificado para composição de strings e variáveis:   ---   COMPOSIÇÃO COM F-STRINGS
print(f'Meu nome é {nome} e eu trabalho como {job} há pelo menos {idade} anos')