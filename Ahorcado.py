
import random
from os import system

with open("diccionario_sin_acentos.txt", "r", encoding="utf8") as f:
    diccionario = f.readlines()



palabra_secreta = random.choice(diccionario)
palabra_usuario = []
letra_usuario = " "

for letras in palabra_secreta:
        palabra_usuario.append (" ")
del palabra_usuario[-1]

def pantalla_principal():
    global intentos
    system("cls")
    print("<--AHORACADO v1-->")
    print(f"Te quedan {intentos} intentos!")
    print(f"La palabra secreta tiene {len(palabra_usuario)} letras!") # hay un espacio en el diccionario??

    for letras in palabra_usuario:
        if letras != " ":
                print(letras, end=" ")    
        else:
            print("_", end=" ")

def input_usuario_letra():
     global palabra_usuario
     global letra_usuario
     letra_usuario = input("\n")
     

def revisa_letra():
     global palabra_usuario
     global palabra_secreta
     global letra_usuario
     
     for i in range(0, (len(palabra_usuario))):
        if palabra_secreta[i] == letra_usuario:
            
            palabra_usuario[i] = letra_usuario
          
        
            
            
     
intentos = 20
while True:
     a = 0
     pantalla_principal()
     
     input_usuario_letra()
     revisa_letra()
     intentos -= 1
  
     palabra_usuario_rev = "".join(palabra_usuario)
     palabra_usuario_rev = str(palabra_usuario_rev)
     
     if " " not in palabra_usuario_rev:
        pantalla_principal()
       
        print("\nganas!")
        
        break
     
     if intentos == 0:
          print("pierdes!")
          print(f"la palabra secreta era:{palabra_secreta}")
          break
     
    
     











