#CIFRADO AFIN
def Euclides(a, b):
  if b == 0:
    return a
  else:
    return Euclides(b, a%b)
		
def Ext_Euclides(a, b):
  if b == 0:
    return (a, 1, 0)
  else:
    d, x_, y_ = Ext_Euclides(b, a%b)
    x, y = y_, x_ - int(a/b)*y_
    return (d, x, y)

def Inversa(a, n):
  if Euclides(a, n) == 1:
    mgd, x, y = Ext_Euclides(a, n)
    return x % n
  else:
    print("No existe inversa")
#VOLVEMOS A USAR LAS FUNCIONES DEL ANTERIOR EJERCICIO

words = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ") #La lsita de letras
words.index("D")  #La letra "D" esta en el index 3, words[3] = "D"

import random
random.randint(0,26)  #dominio = [0, 26],pertenece al cirulo de Z_27

# Generador random de llaves:
a = random.randint(0,26)
while a%3==0:   #while para validar, "a" no puede ser mod de 3, ya que 27 es multiplo de 3
  a = random.randint(0,26)
b = random.randint(0,26)

print("La Llave Generada es: {%d, %d}" % (a,b))

def Cifrado(cadena):
  nueva_cadena = ""

  for i in cadena:
    nueva_cadena += words[ (a * words.index(i) + b) % 27]
  
  return nueva_cadena

def Descifrado(cadena):
  a_ = Inversa(a, 27)
  nueva_cadena = ""

  for i in cadena:
    nueva_cadena += words[ (a_ * (words.index(i) - b)) % 27]
  return nueva_cadena

mensaje_cifrado = Cifrado("ELEMENTALMIQUERIDOWATSON")
print(mensaje_cifrado)
print(Descifrado(mensaje_cifrado))

Descifrado("OKHFSNKFNWFCWJHSNCHQYWFSWF")

#########################
# Probamos las posibles combinaciones de a y b paradescifrar el mensaje
#########################
# Esta es una extension del codigo de Cifrado Afin

A = [i for i in range(27) if i%3!=0]
A

B = list(range(27))
B

message = "SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV"
for a in A:
  for b in B:
    print("Keys = {%d, %d}  Descifrado = %s \n\n" % (a,b,Descifrado(message)))

###############  
# DESPUES DE PROBAR CON TODAS LAS POSIBLES LLAVES SE OBTUVO QUE LA LLAVE 23,17 ERA LA CORRECTA O LA QUE MAS SENTIDO TENIA
###############

a, b = 23, 17
print("Keys =  {%d, %d}  Descifrado = %s" % (a,b,Descifrado(message)))

'''
Keys =  {23, 17}  Descifrado = NOEXISTENPREGUNTASSINRESPUESTASOLOPREGUNTASMALFORMULADAS
'''
