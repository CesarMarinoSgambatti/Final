
'''
Problema 1/6:

Diseñe un programa que solicite a un usuario el valor de N para generar números aleatorios con la técnica del cuadrado medio.
El programa debe verificar que tal número posea al menos 4 dígitos, en caso contrario arroje un mensaje de error y vuelva a solicitar el número N.
Debe otorgarle al usuario como máximo, 3 oportunidades para introducir el número correctamente.
'''


intentos=0
a=0
NumeroDelCentroA=0
b=0
NumeroDelCentroB=0
c=0
numeroDelCentroC=0


'''
Identifico mis variables:
Se inicia con el intento igual a cero, de este modo si el usuario introduce un valor no válido se le sumará 1 y así sucesivamente hasta llegar a 3 (intentos=1; intentos=2; intentos=3) y no podrá continuar.
'''


'''
Con un ciclo while (mientras), establecemos el número de intentos (máximo 3) con la siguiente lógica:
Mientras el número de intentos sea menor a 3, realiza esta operación; si se llega a 3 intentos (if), imprime "se han agotado los intentos".
'''

'''
Dentro del ciclo while (con identación), pedimos que el usuario ingrese el número N entero, corroboramos que sea un número, que tenga al menos 4 dígitos.
n.isnumeric() es un método que permite identificar si es un número (true) o no (false).
La función len() indica la cantidad de caracteres en el valor de entrada. Si es mayor o igual a 4 se efectúa una operación, sino se indica que debe tener al menos 4 dígitos.
La instrucción raise permite ejecutar excepciones.
'''

'''
Si el número cumple con las condiciones, nos muestra: el número al cuadrado; el número aleatorio y los términos centrales.
El número aleatorio lo obtengo dividiendo el número entre (10 elevado al número de caracteres que posea). Garantizando que será un decimal.
El número ubicado en el medio del número al cuadrado, se obtiene pasándolo a string e indicando las posiciones de los caracteres que se tomarán (del 2 al 6).
'''
q=0
w=0

while intentos <3:
    n=(input("ingrese el valor de N:"))
    if not n.isnumeric() :
        raise TypeError("Ingrese un número entero positivo")
    n=int(n)    
   #La función LEN indica la cantidad de caracteres
    if len(str(n))>=4:
        a=n**2
        q=int((len(str(n)))//2)
        w=int(((3*(len(str(n)))))//2)
        print(w)
        NumeroDelCentroA=(str(a))[q:w]
        print("numero A al cuadrado:", a)
        print("número aleatorio de A:", a*10**(-2*int(len(str(n)))))
        print("numero del centro A:", NumeroDelCentroA)

        b=int(NumeroDelCentroA)**2
        q=int((len(str(NumeroDelCentroA)))//2)
        w=int(((3*(len(str(NumeroDelCentroA)))))//2)
        NumeroDelCentroB=str(b)[q:w]
        print("numero B al cuadrado:", b)
        print("número aleatorio de B:", b*10**(-2*int(len(str(n)))))
        print("numero del centro de B", NumeroDelCentroB)

        c=int(NumeroDelCentroB)**2
        q=int((len(str(NumeroDelCentroB)))//2)
        w=int(((3*(len(str(NumeroDelCentroB)))))//2)
        numeroDelCentroC=str(c)[q:w]
        print("numero C al cuadrado:", c)
        print("número aleatorio de C:", c*10**(-2*int(len(str(n)))))
        print("numero del centro de C", numeroDelCentroC)
    else:
        print("el numero debe tener al menos 4 digitos")
        intentos += 1
if intentos==3:
    print("se han agotado los intentos")

