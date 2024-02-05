import random
from os import system

#VARIABLES
tecla = "y"
baraja = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
mano_jugador = []
mano_mesa = []
valor_mano_jugador = 0
valor_mano_mesa = 0
jugador_se_planta = False
mesa_se_planta = False
ganancia = 0
banca = 0
apuesta = 0
primera_carta = True
opcion_tecla = "y"


#FUNCIONES

def primera_pantalla():

    system("cls")
    print("<--BlackJack v2-->")

    print("Cuantos tokens quieres cargar en la banca? ")
    global banca
    banca = input()

    system("cls")
    print("<--BlackJack v2-->")
    print(f"Tienes {banca} en la banca!")
    print("Cuantos tokens quieres apostar por partida? ")
    global apuesta
    apuesta = input()

    return

def actualiza_pantalla():
    system("cls")
    print("<--BlackJack v2-->")
    print(f"Tienes {banca} en la banca!")
    print(f"Apuesta de {apuesta} por tirada!")
    print(f"Tus cartas son: {mano_jugador}, con un valor de: {valor_mano_jugador} puntos!")
    print(f"Las cartas de la mesa son: {mano_mesa}, con un valor de: {valor_mano_mesa} puntos!")

def actualiza_pantalla_final():
    global banca
    global apuesta
    global valor_mano_mesa
    global valor_mano_jugador
    global ganancia
    global tecla

    system("cls")
    print("<--BlackJack v2-->")
    print(f"Tienes {banca} en la banca!")
    print(f"Apuesta de {apuesta} por tirada!")
    print(f"Tus cartas son: {mano_jugador}, con un valor de: {valor_mano_jugador} puntos!")
    print(f"Las cartas de la mesa son: {mano_mesa}, con un valor de: {valor_mano_mesa}")
    revisa_marcadores()
    
    if valor_mano_mesa == 21:
        print("La mesa gana con BlackJack!")
    
    if valor_mano_jugador == 21 and valor_mano_mesa != 21:
        print(f"Tienes BlackJack!, ganas {ganancia} tokens!")
    
    if valor_mano_jugador < 21 and valor_mano_mesa < 21:
        print(f"te has plantado con {valor_mano_jugador}")
        print(f"la mesa se planta con {valor_mano_mesa}")
        if valor_mano_jugador > valor_mano_mesa:
            print(f"Ganas {ganancia} tokens!")
        else:
            print(f"No has ganado!")
    
    if valor_mano_mesa > 21:
        print("La mesa se ha pasado!")
    if valor_mano_mesa > 21 and valor_mano_jugador <= 21:
        print(f"Ganas {ganancia} tokens!")
    if valor_mano_jugador > 21:
        print("Te has pasado!, pierdes!")
   
    print("Quieres volver a jugar? (y/n/b)")
    tecla = input()
    return tecla



def pantalla_principal():
    
    global mano_jugador
    global mano_mesa
    global valor_mano_jugador
    global valor_mano_mesa
    global jugador_se_planta
    global mesa_se_planta
    global tecla
    
    
    primera_jugada()
    actualiza_pantalla()
    
    while jugador_se_planta == False:
        if check_puntos_jugador() == True:
            print("Quieres una carta mas?(y/n) ")
            if input() == "y":
                mas_carta_jugador()
                check_puntos_jugador()
                actualiza_pantalla()
            else:
                jugador_se_planta = True
                break
        else:
            break    
            

    
    actualiza_pantalla()
    check_puntos_mesa()
    if valor_mano_jugador <= 21:
        while mesa_se_planta == False and valor_mano_jugador > valor_mano_mesa:
            if check_puntos_mesa() == True:
                mas_carta_mesa()
                actualiza_pantalla()
            else: 
                mesa_se_planta == True
                break
    actualiza_pantalla_final()    

    

def revisa_marcadores():
    global valor_mano_mesa
    global valor_mano_jugador
    global apuesta
    global banca
    global ganancia
    

    if valor_mano_jugador == 21 and valor_mano_mesa == 21:
        banca = int(banca) - int(apuesta)
    if valor_mano_jugador == 21 and valor_mano_mesa != 21:
        ganancia = int(apuesta) * 5
        banca = int(banca) + int(ganancia)
    
    if valor_mano_mesa > 21 and valor_mano_jugador < 21:
        ganancia = int(apuesta) * 2
        banca = int(banca) + int(ganancia)

    if valor_mano_jugador > valor_mano_mesa and valor_mano_jugador <21:    
        ganancia = int(apuesta) * 2
        banca = int(banca) + int(ganancia)
    
    else:
       banca = int(banca) - int(apuesta)         
        

    
        

    


def check_puntos_jugador():
    global valor_mano_jugador

    if valor_mano_jugador >= 21:
        return False
    
    elif valor_mano_jugador < 21:
        return True
    
def check_puntos_mesa():
    global valor_mano_mesa
    global valor_mano_jugador

    if valor_mano_mesa >= 16 and valor_mano_mesa >= valor_mano_jugador:
        return False
    
    else:
        return True





def primera_jugada():

    global mano_jugador
    global mano_mesa
    global valor_mano_jugador
    global valor_mano_mesa

    
    carta_devuelta, valor = coge_carta()
    mano_jugador.append(carta_devuelta)
    valor_mano_jugador = valor_mano_jugador + valor
   

    carta_devuelta, valor = coge_carta()
    mano_mesa.append(carta_devuelta)
    valor_mano_mesa = valor_mano_mesa + valor
    

    carta_devuelta, valor = coge_carta()
    mano_jugador.append(carta_devuelta)
    valor_mano_jugador = valor_mano_jugador + valor
    

    carta_devuelta, valor = coge_carta()
    mano_mesa.append(carta_devuelta)
    valor_mano_mesa = valor_mano_mesa + valor
    
def mas_carta_jugador():
    global mano_jugador
    global valor_mano_jugador

    carta_devuelta, valor = coge_carta()
    mano_jugador.append(carta_devuelta)
    valor_mano_jugador = valor_mano_jugador + valor

def mas_carta_mesa():
    global mano_mesa
    global valor_mano_mesa

    carta_devuelta, valor = coge_carta()
    mano_mesa.append(carta_devuelta)
    valor_mano_mesa = valor_mano_mesa + valor



def coge_carta():

    global baraja
    
    carta = 0
    while carta == 0:
        index_carta = random.randint(0, 51)
        carta = baraja[index_carta]
        baraja[index_carta] = 0
        
        if carta == 0:
            pass
        else:
            if carta == "J" or carta == "Q" or carta == "K":
                valor_carta = 0.5
            elif carta == "A":
                valor_carta = 1
            else:
                valor_carta = int(carta)

            return carta, valor_carta
    




def reset_baraja():
    global baraja
    global mano_jugador
    global mano_mesa
    global valor_mano_jugador
    global valor_mano_mesa
    global jugador_se_planta
    global mesa_se_planta
    global ganancia

    baraja = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    mano_jugador = []
    mano_mesa = []
    valor_mano_jugador = 0
    valor_mano_mesa = 0
    jugador_se_planta = False
    mesa_se_planta = False
    ganancia = 0








#MAIN LOOP
seguir = "y"
primera_pantalla()
while seguir == "y":

    if tecla == "y":
        system("cls")
        pantalla_principal()
        reset_baraja()
    if tecla == "b":
        primera_pantalla()
        reset_baraja()

else:
    quit