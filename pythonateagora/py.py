# dias = int(input('quantos dias voce trabalha por mes '))
# salario = int(input('qual e o seu salario '))
# horas = float(input('quantas horas voce trabalha por dia '))
# ganha = salario / dias
# print('voce ganha por dia ', ganha)
# print('voce ganha por hora ', ganha / horas)

# h = float(input('informe sua altura '))
# wm = (72.7 * h) - 58
# wf = (62.1 * h) - 44.7
# print('para homens ', wm, 'para mulheres ', wf)

# kg = float(input('quantos kg de peixe voce pescou '))
# excesso = kg - 50
# multa = (excesso)

# if kg>50:
# multa = (excesso*4)
# print('o excesso é ', excesso)
# print('o valor da multa é ', multa)

# area = int(input('informe a area '))
# litro = area/3
# latas = litro/18
# preço = math.ceil(latas*80)
# print('quantidade de latas ', math.ceil(latas))
# print('valor da tinta ', preço)

# 15. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a) comprar apenas latas de 18 litros;
# b) comprar apenas galões de 3,6 litros;
# c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10%

#area = int(input('informe a area '))
#litro = area / 6
#lata = litro / 18
#galao = litro / 3.6
#precol = math.ceil(lata * 80)
#precog = math.ceil(galao * 25)
#print('quantidade de latas ', math.ceil(lata))
#print('valor da tinta ', preco)

#a=1
#=3
#if a==2:
#print('teste if')
#else:
#  print('teste else')

#a = int(input('informe um numero '))
#b = int(input('informe mais um numero '))

#soma = a + b
#if soma>10:
#print('a soma é ', soma)

#a = float(input('informe um valor '))
#b = float(input('informe um valor '))
#c = float(input('informe  um valor '))

#if (a + b) < c:
#  print('a soma A + B é menor que C')

#else:
#  print('a soma A + B é maior que C')

#Ler quatro números  referentes a quatro notas e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o valor da média do aluno para qualquer condição.

#a = int(input('informe a primeira nota: '))
#b = int(input('informe a segunda nota: '))
#c = int(input('informe a terceira nota: '))
#d = int(input('informe a ultima nota: '))
#media = (a+b+c+d)/4

#if (a+b+c+d)/4>=5:
#  print("voce foi aprovado")
#else:
#  print("voce foi reprovado")

#print("sua media é: ", media)

#Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis por 2 e 3.

# a = int(input('informe a primeira nota: '))
# b = int(input('informe a segunda nota: '))
# c = int(input('informe a terceira nota: '))
# d = int(input('informe a ultima nota: '))

# if (a/2 or a/3) == a/2 or a/3:
#   print(a)

# if b/2 or b/3:
#   print(b)
# else:
#   print("nao")

# if c/2 or c/3:
#   print(c)

# if d/2 or d/3:
#   print(d)

# Faça um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# Infantil A             5 – 7 anos;

# Infantil B         8 – 10 anos

# Juvenil A         11 – 13 anos

# Juvenil B         14 – 17 anos

# Adulto             18 – 60 anos

# Senior              acima de 60 anos.

# a = int(input("informe a sua idade: "))

# if 5 <= a <= 7:
#   print('voce esta na categoria infantil a')
# if 8 <= a <= 10:
#   print('voce esta na categoria infantil b')

# if 11 <= a <= 13:
#   print('voce esta na categoria juvenil a')

# if 14 <= a <= 17:
#   print('voce esta na categoria juvenil b')

# if 18 <= a <= 60:
#   print('voce esta na categoria adulto')

# if a > 60:
#   print('voce esta na categoria senior')

#Determine o resultado lógico das expressões mencionadas, assinalando se são verdadeiras ou falsas.  Considere para as respostas os seguintes valores: X = 1, A= 3, B = 5, C = 8 e D = 7.

# não(X>3)
# (X<1) e não (B>D)
# não (D<0) e (C>5)
# não(X>3) ou (C<7)
# (A>B) ou (C>B)
# (X>=2)
# (X<1) e (B>=D)

# x = 1
# a = 3
# b = 5
# c = 8
# d = 7

# if not(x>3):
#   print("1verdadeiro")

# else:
#   print("1falso")

# if (x<1) and not(b>d):
#   print("2verdadeiro")

# else:
#   print("2falso")

# if not(d<0) and (c>5):
#   print("3verdadeiro")

# else:
#   print("3falso")

# if not(x>3) or (c<7):
#   print("4verdadeiro")

# else:
#   print("4falso")

# if (a>b) or (c>b):
#   print("5verdadeiro")

# else:
#   print("5falso")

# if (x>=2):
#   print("6verdadeiro")

# else:
#   print("6falso")

# if (x<1) and (b>=d):
#   print("7verdadeiro")

# else:
#   print("7falso")

# x = float(input('informe salario: '))
# y = x/100*10
# z = x-y
# a = z/100*5
# salario = z-a
# print('o salario é: ' , salario)

# #As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
# e R$ 1,00 se forem compradas pelo menos 12 unidades. Escreva um
# programa que leia o número de maçãs compradas, calcule e imprima o
# custo total da compra

#
# a = int(input('inforne k valor'))
# if a < 2:
#   print('baixo')
# else:
#   if a >= 6:
#     print('medio')
#   else:
#     if a <= 10:
#       print('grande')

# Escreva um programa que pergunte ao usuário um número e após, imprima na tela a soma total de 1 até o número lido. Exemplo: 5: 1 + 2 + 3 + 4 + 5 = 15

# num = int(input('informe um valor '))
# i = 1
# soma = 0
# while i <= num:
#     print(i)
#     i+=1
#     soma = soma + i - 1 #soma+=i
# print(soma)

# Faça um programa que peça dois números, base e expoente, calcule e imprima o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

# base = int(input('informe a base: '))
# expoente = int(input('informe o expoente: '))
# i = 0
# mult = 1
# while i < expoente:
#     print(base)
#     mult = mult*base
#     i += 1

# print(mult)

# Faça um programa para calcular e imprimir a soma dos cubos dos números pares compreendidos entre A e B (B > A). A e B são lidos pelo teclado.

# a = int(input('informe um valor: '))
# b = int(input('informe um valor: '))
# soma = 0
# while a<b:
#     if a%2==0:
#         print(a)
#         soma += a**3
#     a+=1
# if a<b:
#     print('a soma é: ', soma)
# while b<a:
#     if b%2==0:
#         print(b)
#         soma += b**3
#     b+=1
# print('a soma é: ', soma)

#  Faça um programa que receba um valor que foi depositado na poupança e exiba o valor com rendimento mês a mês durante o período de um ano. Considere fixo o juros da poupança em 0,5% a. m.

# saldo = float(input('informe o valor: '))
# juros = saldo*0.005
# i = 1

# while i <=12:
#     saldo+=juros
#     i += 1

# total = saldo + juros
# print(total)

# n = int(input('informe um numero: '))
# i = 2
# div = 0

# Número primo é aquele que só é divisível por ele mesmo e pelo número 1. Faça um programa que peça um número inteiro ao usuário e determine se o número informado é primo ou não.

# while i < n and div==0:
#   if n % i == 0:
#     div += 1
#   i += 1
# if div == 0:
#   print('é primo')
# else:
#   print('nao é primo')

# Escreva um programa que determine o fatorial de um número. Para este problema, tem-se como entrada o valor do número do qual se deseja calcular o fatorial. O fatorial de 0 é igual a 1. O fatorial de um número N(N!) é definido conforme a seguir:

# N! = 1 × 2 × 3 × 4 × ... × (N - 1) × N

# n = int(input('informe um numero: '))

# if n == 0:
#   print('fatorial de 0 é 1')

# elif n < 0:
#   print('nao existe')

# else:
#   i = 1
#   fat = 1
#   while i <= n:
#     fat = fat * i
#     i += 1
#   print(fat)

# ----------------------------------------------------------------

# Questão 1: Escreva um programa em Python que tenha as seguintes entradas:
# • um número n (número de termos de uma progressão aritmética)
# • a1 (o primeiro termo da progressão)
# • r (a razão da progressão)
# A partir dos dados de entrada, o programa deverá exibir os termos da progressão, bem como a soma dos termos.
# Exemplo de uma progressão aritmética com 5 termos, razão 2 e o primeiro termo sendo 1
# 1 3 5 7 9

# n = int(input('informe um numero: '))
# a = int(input('informe um numero: '))
# r = int(input('informe um numero: '))
# i = 1

# while i <= n:
#   print(a)
#   a += r
#   i += 1

#  --------------------------------------------------------------

# n = int(input('informe um numero: '))
# i = 1
# uf = 1
# pf = 1

# if n >= 2:
#   print(i)
#   print(i)
#   while i <= n:
#     aux = uf
#     uf += pf
#     pf = aux
#     print(uf)
#     i += 1

n = 0
i = 1
m = 7

while n < 1000:
  print(n)
  n += m
  i += 1
