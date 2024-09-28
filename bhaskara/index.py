import math
a = int(input('informe o valor de a: '))
b = int(input('informe o valor de b: '))
c = int(input('informe o valor de c: '))

delta = (b**2) - (4*a*c)

raiz1 = (((-1)*b) + (delta**0.5))/2*a
raiz2 = (((-1)*b) - (delta**0.5))/2*a

if a == 0:
    print("nao é uma equação de segundo grau")
elif delta <0:
    print("nao possui raízes reais")
elif delta==0:
    print("a equaçao possui apenas uma raíz real", raiz1)
else:
    print("a equaçao possui as seguintes raízes reais" , raiz1 , raiz2) 

