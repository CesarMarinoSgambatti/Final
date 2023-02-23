

n=input("ingrese el número par y positivo:")
fila=[]
columna=[]
matriz=[]
K=0
a=1

if not n.isnumeric() or int(n)%2!=0: 
    raise TypeError("ingrese un número par y positivo")

n=int(n)
matriz=[]
b=n

#crear la matriz
for i in range(n):
    fila=[]
    for j in range(n):
        fila.append(0)
    matriz.append(fila)

#proximos dos ciclos for son para recorrer cada elemento de la matriz
for h in range(n):
    for d in range(n):
        #cuando k es 36-6=30 y k= 6*1
        if K<(n*n)-n:
            if K==n*a:
                a+=2
                K+=n 
        if K==b*n:
            b-=2
            K=K-(n*3)
        K+=1     
        matriz[h][d]=K

print(matriz)
