# Imprimir listagem de números de 1 a 10:
x = 1;
while (x<=10):
    print(x);
    x = x+1;


# Algoritmo que imprime uma saudação (Bom dia!) 3x:
repete_saudacao = 1;
while (repete_saudacao<=3):
    print('olá, seja bem vindo!');
    repete_saudacao = repete_saudacao + 1;


# Algoritmo que imprime apenas os números pares existentes dentro de um intervalo fornecido pelo usuário:
inicio_intervalo = int(input('Informe o primeiro número do intervalo desejado: '));
fim_intervalo = int(input('Informe o último número do seu intervalo: '));

count = inicio_intervalo;
while (count <= fim_intervalo):
    if(count % 2 == 0):
        print(count);
    count = count + 1;


# Cálculo da Média do aluno, a partir de suas 4 notas em uma disciplina:
soma = 0;   # Variável acumuladora
count = 1;  # Variável de contagem
while (count <= 5):
    nota = float(input(f'Informe a sua {count}ª Nota: '));
    soma = soma + nota;
    count = count + 1;
media = soma / 5;
print(f'Média final: {media}');


# Validando dados de entrada com um loop:
num = int(input('Digite um número maior que zero: '));

while(num<=0):
    print('Digite um caractere válido!');
    num = int(input('Digite um número maior que zero: '));

print(f'Muito bem, você digitou o número {num}');