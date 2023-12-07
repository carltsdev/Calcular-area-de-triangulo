print("calcular el area de un triangulo")
print("--‐--------------")
from math import*

a=float(input('ingrese lado A='))
b=float(input('ingrese lado B='))
c=float(input('ingrese lado A='))
t=(a+b+c)/2
s=sqrt(t*(t-a)*(t-b)*(t-c))
print(" ")
print("El area es :",s)