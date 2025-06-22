x = True;
y = False;

# x = 2;
# y = 4;

# Operador NOT (Negação):
print(x);
print(not x);
print(y);
print(not y);

# Operador AND (Conjunção "e"):
if(x%2==0 and y%2==0):
    print("Ambos os números fornecidos são PARES");
else:
    print('Pelo menos um dos número fornecidos é ÍMPAR');


# Operador OR (Disjunção "ou"):
if(x == True and y == True):
    print('Ambos os valores são Verdadeiros');
else:
    print('Um dos valores não é verdadeiro');

a = 10;
b = 1;
z = 5.5;
# res = not a>b;
res = (a>b) and (z==y)
print(res);

# Exercícios para o cálculo de Médias:
m1 = float(input("Informe a nota da primeira matéria: "));
m2 = float(input('Informe a nota da segunda matéria: '));
m3 = float(input('Agora, informe a nota da terceira matéria: '));
if(m1>7 and m2>7 and m3>7):
    print('O aluno está APROVADO');
else:
    print('O aluno foi reprovado em, pelo menos, uma matéria');