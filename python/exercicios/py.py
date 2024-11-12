# Construa um Algoritmo que, para um grupo de 50 valores inteiros, determine:

#             a) A soma dos números positivos;

#             b) A quantidade de valores negativos;

# soma = 0
# contneg = 0
# i = 1
# while i <=5:
#     num = int(input('informe um numero '))
#     if num > 0:
#         print('positivo')
#         soma = soma + num
#     elif num < 0:
#         print('negativo')
#         contneg = contneg +1
#     i += 1
# print ('negativo = ', contneg)
# print ('soma = ', soma)

# FOOOORRRRRRRRRRRR

# Faça um algoritmo que imprima todos os números pares compreendidos entre 85 e 907. O algoritmo deve também calcular a soma destes valores.



# num = 86
# while num <907:
#     print(num)
#     num += 2


# i = 85
# while i<907:
#     if i%2 ==0:
#         print(i)
#     i +=1


#Escreva um programa que pergunte ao usuário um número e após, imprima na tela a soma total de 1 até o número lido. Exemplo: 5: 1 + 2 + 3 + 4 + 5 = 15
        
#numero = int(input("informe um número"))
#soma = 0
#for i in range (1, numero+1):
#    print(i)
#    soma = soma + i
#print("A soma dos termos é" ,soma)

#Faça um programa que peça dois números, base e expoente, calcule e imprima o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

#base = int(input("informe a base"))
#expoente = int(input("informe o expoente"))
#potencia = 1
#for i in range (expoente):
#    potencia = potencia*base
#print(potencia)  

#Faça um programa para calcular e imprimir a soma dos cubos dos números pares compreendidos entre A e B (B > A). A e B são lidos pelo teclado.

#a = int(input("informe um número"))
#b = int(input("informe um número"))
#soma = 0
#if a>b:
#    a,b = b,a
#for i in range(a+1,b):
#    if i%2==0:
#        soma = soma + i**3
#print(soma)

# a = int(input('numero: '))
# b = int(input('numero 2: '))
# soma = 0
# if a > b:
#   a, b = b, a

# for i in range(a + 1, b):
#   if i % 2 == 0:
#     soma = soma + i**3

# print(soma)

# Faça um programa que receba um valor que foi depositado na poupança e exiba o valor com rendimento mês a mês durante o período de um ano. Considere fixo o juros da poupança em 0,5% a. m.

# a = float(input('valor depositado: '))
# b = 0

# for i in range(1, 13):
#   a = a * 0.005 + a
#   print(a)

# Número primo é aquele que só é divisível por ele mesmo e pelo número 1. Faça um programa que peça um número inteiro ao usuário e determine se o número informado é primo ou não.

# a = int(input('numero: '))
# b = 0
# for i in range(2, a):
#   if a % i == 0:
#     b += 1
# if b == 0:
#   print('primo')
# else:
#   print('não primo')














