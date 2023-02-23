number_1=(input("ingrese numero:"))
n=1
number_2=number_1
int(number_2)
if number_1.isnumeric():
    number_1=int(number_1)
    number_2=int(number_2)
    while n<number_1:
        number_2=number_2+n 
        n=n+1
    print(number_2)
else:    
    print("el numero ingresado no es entero")  