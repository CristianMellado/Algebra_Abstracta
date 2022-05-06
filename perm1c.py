#EJERCICIO 1: El Inverso Multiplicativo FUNCION INVERSA

def Euclides(a, b):
  if b == 0:
    return a
  else:
    return Euclides(b, a%b)
		
#####
		
def Ext_Euclides(a, b):
  if b == 0:
    return (a, 1, 0)
  else:
    d, _x_, _y_ = Ext_Euclides(b, a%b)
    x, y = _y_, _x_ - int(a/b)*_y_
    return (d, x, y)

#####
		
def Inversa(a, n):
  if Euclides(a, n) == 1:
    mgd, x, y = Ext_Euclides(a, n)
    return x % n     
  else:
    print("No existe inverso multiplicativo")
		
#####

Inversa(3,9)
Inversa(3,4)
