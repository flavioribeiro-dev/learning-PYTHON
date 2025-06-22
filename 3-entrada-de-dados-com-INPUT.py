# Criando campos para receber ENTRADA DE DADOS do usuário: INPUT...
# --- O método INPUT sempre interpreta os dados como sendo do tipo String.

nome = input('Qual o seu nome?');
print(f'Olá, {nome}. Tudo bem?');

# Convertendo dados de entrada (string --> int OU fload) - (Casting de Variáveis)
# --- Para isso, precisamos utilizar antes do Input as funções INT ou a FLOAT (que farão as devidas conversões de tipo)
idade = int( input('Qual a sua idade?') );
print(idade);

nota1 = float( input('Primeira Nota: ') );
nota2 = float( input('Segunda Nota: ') );
media = (nota1+nota2)/2;
print(f'{nome}, sua média foi {media}');

n1 = int(input('Digite um número inteiro: '));
n2 = int(input('Digite outro número: '));
soma = n1+n2;
texto = 'O resultado da soma de {} com {} é {}'.format(n1,n2,n1+n2);
print(texto);
print(f'a soma de {n1} com {n2} é {n1+n2}'); 