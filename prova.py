#2
# from math import *
# raio = float(input())
# area = 3.14159*(raio**2)
# s="A="+'{0:.4f}'.format(area)
# print(s)
#3
# def soma(x,y):
#     return x+y
# valor=soma(int(input()),int(input()))
# print("SOMA =",valor)
#4
# x=int(input())
# y=int(input())
# PROD=x*y
# print("PROD =",PROD)
#5
# A=float(input())
# A*=3.5
# B=float(input())
# B*=7.5
# MP=(A+B)/11
# s="MEDIA = "+'{0:.5f}'.format(MP)
# print(s)
#6
# A=float(input())
# A*=2
# B=float(input())
# B*=3
# C=float(input())
# C*=5
# MP=(A+B+C)/10
# s="MEDIA = "+'{0:.1f}'.format(MP)
# print(s)
#7
#DIFERENCA = (A * B - C * D)
# A=int(input())
# B=int(input())
# C=int(input())
# D=int(input())
# DIFERENCA = (A * B - C * D)
# DIFERENCA=str(DIFERENCA)
# print("DIFERENCA = "+ DIFERENCA)
#8
# NUMBER = int(input())
# HOURS = int(input())
# PRICE = float(input())
# SALARY = float(HOURS*PRICE)
# print("NUMBER = " + str(NUMBER))
# print("SALARY = U$ " + '{0:.2f}'.format(SALARY))
#9
# name = raw_input()
# salary = float(input())
# sale = float(input())
# salary+=sale*0.15
# print("TOTAL = R$ " + '{0:.2f}'.format(salary))
#10
# x = input()
# list = x.split(' ')
# cod1 = list[0]
# quant1 = int(list[1])
# preco1 = float(list[2])
# y = input()
# list2 = y.split(' ')
# cod2 = list2[0]
# quant2 = int(list2[1])
# preco2 = float(list2[2])
# soma = (preco1*quant1)+(preco2*quant2)
# frase = "VALOR A PAGAR: R$ " + '{0:.2f}'.format(soma)
# print(frase)
#11
const = 4/3
pi = 3.14159
raio = float(input())
result = const * pi * (raio**3)

print("VOLUME = " + '{0:.3f}'.format(result))