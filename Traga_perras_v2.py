import random
import numbers 
from prettytable import PrettyTable
from os import system
import time

# Colores copia de video de barras de progreso https://www.youtube.com/watch?v=0e2DexQlDYk&t=368s
color_red = "\033[91m"
color_purple = "\33[95m"
color_blue1 = "\33[34m"
color_blue2 = "\33[36m"
color_blue3 = "\33[96m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_brown = "\33[33m"
color_yellow = "\33[93m"
color_grey = "\33[37m"
color_default = "\033[0m"


COLUMNAS = 4
FILAS = 3
CARTAS_POR_RUEDA = 9
saldo = 0
apuesta = 0
linea_ganadora1 = False
linea_ganadora2 = False
linea_ganadora3 = False
random_columna1 = 0
random_columna2 = 0
random_columna3 = 0

rueda1 = ["\33[36mA\033[91m", "\33[93mK\033[91m", "\33[93mK\033[91m", "\033[32mQ\033[91m", "\033[32mQ\033[91m", "\033[32mQ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m",]
rueda2 = ["\33[36mA\033[91m", "\33[93mK\033[91m", "\33[93mK\033[91m", "\033[32mQ\033[91m", "\033[32mQ\033[91m", "\033[32mQ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m",]
rueda3 = ["\33[36mA\033[91m", "\33[93mK\033[91m", "\33[93mK\033[91m", "\033[32mQ\033[91m", "\033[32mQ\033[91m", "\033[32mQ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m", "\33[37mJ\033[91m",]

c1l1 = "X"
c2l1 = "X"
c3l1 = "X"
c1l2 = "X"
c2l2 = "X"
c3l2 = "X"
c1l3 = "X"
c2l3 = "X"
c3l3 = "X"
cajon = PrettyTable()
cajon.add_column("<--TRAGAOERRAS v2-->",
        ["FILA 1","FILA 2","FILA 3"])
cajon.add_column("Columna 1", [c1l1, c1l2, c1l3])
cajon.add_column("Columna 2", [c2l1, c2l2, c2l3])
cajon.add_column("Columna 3", [c3l1, c3l2, c3l3])
cajon.add_column("PREMIO", [" ", " "," " ])

def bucle_principal(input_var):
    while input_var != "n" or input_var != "s":
        if input_var == "s":
            input_var = pantalla_inicio()
    
        if input_var == "n":
            pantalla_salida()
            return
        if input_var == "y":
            input_var = pantalla()
            
    
def azar():
    
    return random.randint(0, 9)


def anim():
    global saldo 
    global apuesta
    global random_columna1
    global random_columna2
    global random_columna3
    global c1l1 
    global c2l1 
    global c3l1
    global c1l2
    global c2l2 
    global c3l2 
    global c1l3 
    global c2l3 
    global c3l3 
   
      #tirada
    random_columna1 = azar()
    random_columna2 = azar()
    random_columna3 = azar()
    #tirada
    bucle = 0
    for i in range(0,50):
    #listas
        system("cls")
        print(f"{color_red}<--TRAGRAPERRAS V2-->")
        print(f"Tienes un saldo de {color_default}{saldo}{color_red} tokens!")
        print(f"Con una apuesta de {color_default}{apuesta}{color_red} por linea!")

        if random_columna1 != CARTAS_POR_RUEDA and random_columna1 != CARTAS_POR_RUEDA-1:
            c1l1 = rueda1[random_columna1]
            c1l2 = rueda1[random_columna1 + 1]
            c1l3 = rueda1[random_columna1 + 2]
            random_columna1 = random_columna1 + 1

        if random_columna1 == CARTAS_POR_RUEDA:
            c1l1 = rueda1[0]
            c1l2 = rueda1[1]
            c1l3 = rueda1[2]
            random_columna1 = 1

        if random_columna1 == CARTAS_POR_RUEDA - 1:
            c1l1 = rueda1[CARTAS_POR_RUEDA - 1]
            c1l2 = rueda1[CARTAS_POR_RUEDA]
            c1l3 = rueda1[0]
            
            random_columna1 = 0
        

        if random_columna2 != CARTAS_POR_RUEDA and random_columna2 != CARTAS_POR_RUEDA-1:
            c2l1 = rueda2[random_columna2]
            c2l2 = rueda2[random_columna2 + 1]
            c2l3 = rueda2[random_columna2 + 2]
            random_columna2 = random_columna2 + 1
        if random_columna2 == CARTAS_POR_RUEDA:
            c2l1 = rueda2[0]
            c2l2 = rueda2[1]
            c2l3 = rueda2[2]
            random_columna2 = 1
        if random_columna2 == CARTAS_POR_RUEDA - 1:
            c2l1 = rueda2[CARTAS_POR_RUEDA - 1]
            c2l2 = rueda2[CARTAS_POR_RUEDA]
            c2l3 = rueda2[0]
            random_columna2 = 0
       

        
        if random_columna3 != CARTAS_POR_RUEDA and random_columna3 != CARTAS_POR_RUEDA-1:
            c3l1 = rueda3[random_columna3]
            c3l2 = rueda3[random_columna3 + 1]
            c3l3 = rueda3[random_columna3 + 2]
            random_columna3 = random_columna3 + 1

        if random_columna3 == CARTAS_POR_RUEDA:
            c3l1 = rueda3[0]
            c3l2 = rueda3[1]
            c3l3 = rueda3[2]
            random_columna3 = 1
        if random_columna3 == CARTAS_POR_RUEDA - 1:
            c3l1 = rueda3[CARTAS_POR_RUEDA - 1]
            c3l2 = rueda3[CARTAS_POR_RUEDA]
            c3l3 = rueda3[0]
            random_columna3 = 0
       

        cajon.del_column("<--TRAGAOERRAS v2-->")
        cajon.del_column("Columna 1")
        cajon.del_column("Columna 2")
        cajon.del_column("Columna 3")
        cajon.del_column("PREMIO")
        
        cajon.add_column("<--TRAGAOERRAS v2-->",
            ["FILA 1","FILA 2","FILA 3"])
        cajon.add_column("Columna 1", [c1l1, c1l2, c1l3])
        cajon.add_column("Columna 2", [c2l1, c2l2, c2l3])
        cajon.add_column("Columna 3", [c3l1, c3l2, c3l3])
        cajon.add_column("PREMIO", ["Suerte!", "Suerte!", "Suerte!"])
        bucle = bucle + 1

      
        print(cajon)
        
       
        time.sleep(0.005 * bucle)
        #system("cls")

        if bucle == 500:
         
         return
    return
        

        




    


def pantalla_salida():
    system("cls")
    print("Adios!")
     
        
def pantalla():
    anim()
    global saldo 
    global apuesta
    system("cls")
    print(f"{color_red}<--TRAGRAPERRAS V2-->")
    print(f"Tienes un saldo de {color_default}{saldo}{color_red} tokens!")
    print(f"Con una apuesta de {color_default}{apuesta}{color_red} por linea!")

  


    #listas
    cajon.del_column("<--TRAGAOERRAS v2-->")
    cajon.del_column("Columna 1")
    cajon.del_column("Columna 2")
    cajon.del_column("Columna 3")
    cajon.del_column("PREMIO")
    
    linea_ganadora1 = False
    linea_ganadora2 = False
    linea_ganadora3 = False     
     
    benef = 0
    if c1l1 == c2l1 == c3l1:
            benef = benef + 1000
            linea_ganadora1 = True
    if c1l2 == c2l2 == c3l2:
            benef = benef + 1000
            linea_ganadora2 = True
    if c1l3 == c2l3 == c3l3:
            benef = benef + 1000
            linea_ganadora3 = True
        
    beneficios = benef

    #Ruedas
    cajon.add_column("<--TRAGAOERRAS v2-->",
    ["FILA 1","FILA 2","FILA 3"])
    cajon.add_column("Columna 1", [c1l1, c1l2, c1l3])
    cajon.add_column("Columna 2", [c2l1, c2l2, c2l3])
    cajon.add_column("Columna 3", [c3l1, c3l2, c3l3])
    benef = 0
    if c1l1 == c2l1 == c3l1:
            benef = benef + 5*apuesta
            linea_ganadora1 = True
    if c1l2 == c2l2 == c3l2:
            benef = benef + 5*apuesta
            linea_ganadora2 = True
    if c1l3 == c2l3 == c3l3:
            benef = benef + 5*apuesta
            linea_ganadora3 = True

    lineas_ganadoras = [linea_ganadora1, linea_ganadora2, linea_ganadora3]

    if linea_ganadora1 or linea_ganadora2 or linea_ganadora3 == True:
        cajon.add_column("PREMIO", [lineas_ganadoras[0], lineas_ganadoras[1], lineas_ganadoras[2]])
        lineas_ganadoras = []
    else:
        cajon.add_column("PREMIO", ["False", "False", "False"])

    print(cajon)
  
        
    beneficios = benef
    if beneficios == 0:
        print("No has ganado nada!")
    else:
        print(f"Has ganado {color_default}{beneficios}{color_red} tokens!")
       
        saldo = saldo + beneficios
    saldo = saldo - (apuesta * 3)
    if saldo <= 0:
         return "n"
    #ruedas
    print("Volver a tirar (y), seleccion de apuesta (s), salir (n)")
    tirada_input = input()
    if tirada_input == "n" or tirada_input == "s" or tirada_input == "y":
        return tirada_input
    


    

      

        
    

    



   


    
    """if beneficios == 0:
        print("No has ganado nada!")
    else:
        print(f"Has ganado {color_default}{beneficios}{color_red} tokens!")
        saldo = saldo + beneficios
    #ruedas"""
    
    """ print("Volver a tirar (y), seleccion de apuesta (s), salir (n)")
    tirada_input = input()
    if tirada_input == "n" or tirada_input == "s":
        return tirada_input
    
    return "y"
   """


def pantalla_inicio():
    global saldo 
    global apuesta 
    datos_correctos1 = True
    datos_correctos2 = True
    system("cls")
    print(f"{color_red}<--TRAGRAPERRAS V2-->")

    #FASE DINERO
    
        
    while datos_correctos1:
        system("cls")
        print(f"{color_red}<--TRAGRAPERRAS V2-->")
        print("Cuantos tokens quieres cargar? ", end=" ")
        saldo_input = input()
        if saldo_input.isdigit() and int(saldo_input) >= 3:
            saldo = int(saldo_input)
            datos_correctos1 = False
        

        else:
            print("Minimo 3 tokes. Solo acepta digitos!")
            if  saldo_input == "n": 
                return saldo_input
        
    #FASE APUESTA
    while datos_correctos2:
        system("cls")
        print(f"{color_red}<--TRAGRAPERRAS V2-->")
        print(f"Cuantos tokens quieres cargar? {saldo}")
        print("Cuantos tokens por liena quieres apostar? ", end=" ")
        apuesta_input = input()
        if apuesta_input.isdigit() and int(apuesta_input) >= 1:
            apuesta = int(apuesta_input)
            datos_correctos2 = False
        
        else:
            print("Minimo 1 apuesta. Solo acepta digitos!")
            if  apuesta_input == "n": 
                return apuesta_input

    input_var = "y"
    return input_var

    

input_var = "s" #s de seleccion de apuesta, por defecto al arrancar

bucle_principal(input_var)




