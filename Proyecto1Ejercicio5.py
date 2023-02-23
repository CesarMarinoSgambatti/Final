m= (input("ingrese la cantidad de terminos de la serie:"))
if not m.isnumeric() :
   raise TypeError("ingrese un número entero positivo")
m=int(m)
Valor_la_serie=0

for i in range(1,m+1):
    if i%2==0:
        Valor_la_serie-=1/(i**6)
    else:
        Valor_la_serie+=1/(i**6)
print("el valor de la serie es:", Valor_la_serie, "y el valor de pi es:", ((Valor_la_serie*30240)/31)**(1/6))
#despejé la ecuación inicial
