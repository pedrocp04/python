# -*- coding: utf-8 -*-
import math import sqrt

a = float(input("Digite o valor de a: ")
b= float(input("Digite o valor de b: ")
c= float(input("Digite o valor de c: ")

delta= b**2 + 4 * a * c
raiz_delta= sqrt(delta)

if raiz_delta < 0:
  print("Raiz negativa")
else:
  x1 = (-b + raiz_delta)/ 2 * a
  x2 = (-b - raiz_delta)/ 2 * a
  
print("As raizes são: ", x1, "e", x2)
  
