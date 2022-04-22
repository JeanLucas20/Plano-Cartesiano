print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ")
print("● ● ● ● ● WELCOME ● ● ●  ● ●")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ")


print("") ## Lo agrego para que no me quede pegado lo del print de arriba con el codigo :)

### Input
a= (input("Ingrese la coorednada en el eje X: "))
a=int(a)
b= (input("Ingrese la coorednada en el eje Y: "))
b=int(b)

c= (a, b)

### Processing
if a>0 and b>0 :
     print("La coordenada"+ str(c) + " está en el cuadrante 1.") ###Output

if a<0 and b>0:
    print("La coordenada"+ str(c) + " está en el cuadrante 2.") ###Output


if a<0 and b<0:
    print("La coordenada"+ str(c) + " está en el cuadrante 3.") ###Output


if a>0 and b<0:
    print("La coordenada"+ str(c) + " está en el cuadrante 4.") ###Output

if a==0 and b==0:
    print("La coordenada"+ str(c) + " está en el punto de origen.") ###Output

if a==0 and b!=0:
    print("La coordenada"+ str(c) + " está en el eje y.") ###Output

if a!=0 and b==0:
    print("La coordenada"+ str(c) + " está en el eje X.") ###Output

