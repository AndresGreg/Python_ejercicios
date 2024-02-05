import curses
from curses import wrapper
import os
import time
import random
import winsound

cmd = 'mode 200,60' #resize windows terminal cols, lines
os.system(cmd)
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
#winsound.Beep(frequency, duration)
#winsound.Beep(2500, 500)




logo_l1 = '                                                   ███████╗██╗      ██████╗ ████████╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗                                                   '
logo_l2 = '                                                   ██╔════╝██║     ██╔═══██╗╚══██╔══╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝                                                   '
logo_l3 = '                                                   ███████╗██║     ██║   ██║   ██║       ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗                                                     '
logo_l4 = '                                                   ╚════██║██║     ██║   ██║   ██║       ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝                                                     '
logo_l5 = '                                                   ███████║███████╗╚██████╔╝   ██║       ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗                                                   '
logo_l6 = '                                                   ╚══════╝╚══════╝ ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝                                                   '
\
rueda1 = """
    ___   
   /   |  
  / /| |  
 / ___ |  
/_/  |_|  
          
    __ __ 
   / //_/ 
  / ,<    
 / /| |   
/_/ |_|   
          
    _____ 
  / __  / 
 / / / /  
/ /_/ /   
\___\_\   
          
       __ 
      / / 
 __  / /  
/ /_/ /   
\____/    
          
   _  __  
  | |/ /  
  |   /   
 /   |    
/_/|_|    
           
"""
rueda1 = "    ___      /   |    / /| |   / ___ |  /_/  |_|                __ __    / //_/   / ,<     / /| |   /_/ |_|                 _____   / __  /  / / / /  / /_/ /   \___\_\                    __       / /  __  / /  / /_/ /   \____/                 _  __    | |/ /    |   /    /   |    /_/|_|               "

menu_menu = ["Deposit", "Play", "Bonus", "Exit"]
saldo = 0
bonus = 0
is_jugando = False
letra = ""

def ventana_salida():
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    MAGENTA_WHITE = curses.color_pair(2)
    ventana_sal = curses.newwin(5, 40, 30, 80) #exit window
    ventana_sal.clear
    ventana_sal.attron(MAGENTA_WHITE)
    ventana_sal.border()
    ventana_sal.attroff(MAGENTA_WHITE)
    ventana_sal.addstr(2,5,"Are you sure? (Y/N)")
    ventana_sal.refresh()
    ventana_sal.nodelay(0)
    key_sal = ventana_sal.getkey()
    if key_sal == "y":
         quit()
    else:
         del ventana_sal
         return True
    
def ventana_bank(banca, saldo, edit):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    CYAN_BLUE = curses.color_pair(1)
    MAGENTA_WHITE = curses.color_pair(2)
    
    banca.clear()
    banca.addstr(2, 6, "<=BANK=>", CYAN_BLUE)
    banca.addstr(4, 3, "Balance:", CYAN_BLUE)
    banca.addstr(5, 3, f"{str(saldo)} tokens") 

    banca.attron(CYAN_BLUE)
    banca.border()
    banca.attroff(CYAN_BLUE)
    banca.refresh()
    if edit:
         while edit:
            banca.clear()
            curses.curs_set(1)
            curses.echo()
            banca.nodelay(0)
            banca.addstr(2, 6, "<=BANK=>", CYAN_BLUE)
            banca.addstr(4, 2, "Balance:")
            



            banca.addstr(5, 2, "Input tokens:")
            
           
            banca.attron(MAGENTA_WHITE)
            banca.border()
            banca.attroff(MAGENTA_WHITE)
            banca.refresh()
            saldo_bytes = banca.getstr(6,2,5)
            saldo = saldo_bytes.decode("utf-8")
            if saldo.isnumeric():
                saldo = str(saldo)
                saldo = int(saldo)
                edit = False

            else:
                banca.addstr(8,1,"Invalid input!")
                
            curses.curs_set(0)
            curses.noecho()
    
    banca.clear()
    banca.addstr(2, 6, "<=BANK=>", CYAN_BLUE)
    banca.addstr(4, 2, "Balance:")
    banca.addstr(5, 2, f"{str(saldo)} tokens") 

    banca.attron(CYAN_BLUE)
    banca.border()
    banca.attroff(CYAN_BLUE)
    banca.refresh()
    return saldo

def reset_windows(menu, banca, ventana_principal, ventana_bonus, ventana_premios):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    CYAN_BLUE = curses.color_pair(1)
    

    menu.attron(CYAN_BLUE)
    menu.border()
    menu.attroff(CYAN_BLUE)
    banca.attron(CYAN_BLUE)
    banca.border()
    banca.attroff(CYAN_BLUE)
    ventana_bonus.attron(CYAN_BLUE)
    ventana_bonus.border()
    ventana_bonus.attroff(CYAN_BLUE)
    ventana_principal.attron(CYAN_BLUE)
    ventana_principal.border()
    ventana_principal.attroff(CYAN_BLUE)
    ventana_premios.attron(CYAN_BLUE)
    ventana_premios.border()
    ventana_premios.attroff(CYAN_BLUE)
    menu.refresh()
    banca.refresh()
    ventana_principal.refresh()
    ventana_bonus.refresh()
    ventana_premios.refresh()


def menu_selec (menu, indice):
    menu.keypad(True) 
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    CYAN_BLUE = curses.color_pair(1)
    MAGENTA_WHITE = curses.color_pair(2)

    menu.clear()
    menu.addstr(2, 6, "<=MENU=>", CYAN_BLUE)

    for i, fila in enumerate(menu_menu):
          if i == indice:
                menu.attron(MAGENTA_WHITE)
                menu.addstr(i*2+5, 4, fila)
                menu.attroff(MAGENTA_WHITE)
          else:
               menu.addstr(i*2+5, 4, fila)

    menu.attron(MAGENTA_WHITE)
    menu.border()
    menu.attroff(MAGENTA_WHITE)           
    menu.refresh()

def borrar1(pad1_1, pad1_2, pad1_3):
    pad1_3.erase()
   
    pad1_2.erase()
   
    pad1_1.erase()
 

def borrar2(pad2_1, pad2_2, pad2_3):
    
    pad2_3.erase()
    
    pad2_2.erase()
   

    pad2_1.erase()
    

def borrar3(pad3_1, pad3_2, pad3_3):

    pad3_3.erase()
 
    pad3_2.erase()

    pad3_1.erase()

def refresca(pad1_1, pad1_2, pad1_3, pad2_1, pad2_2, pad2_3, pad3_1, pad3_2, pad3_3):
    pad1_1.refresh(0, 0, 46, 52, 52, 72) #FILA BAJA
    pad2_1.refresh(0, 0, 46, 92, 52, 112)
    pad3_1.refresh(0, 0, 46, 132, 52, 152)

    pad1_2.refresh(0, 0, 39, 52, 45, 72)    #FILA MEDIA
    pad2_2.refresh(0, 0, 39, 92, 45, 112)
    pad3_2.refresh(0, 0, 39, 132, 45, 152)

    pad1_3.refresh(0, 0, 32, 52, 38, 72)    #FILA ALTA
    pad2_3.refresh(0, 0, 32, 92, 38, 112)
    pad3_3.refresh(0, 0, 32, 132, 38, 152)


    

def play(ventana_principal,ventana_bonus, bonus, is_jugando, banca, ventana_premios):
    doble_nada(ventana_premios, False, letra)
    col_l1 = "                                 ██╗                                   ██████╗                                 ██████╗                                      "
    col_l2 = "                                ███║                                   ╚════██╗                                ╚════██╗                                     "
    col_l3 = "                                ╚██║                                    █████╔╝                                 █████╔╝                                     "
    col_l4 = "                                 ██║                                   ██╔═══╝                                   ╚═══██╗                                    "
    col_l5 = "                                 ██║                                   ███████╗                                 ██████╔╝                                    "
    col_l6 = "                                 ╚═╝                                   ╚══════╝                                 ╚═════╝                                     "
    fil_l1 = "                           >              <                        >              <                        >              <                                 "
    fil_l2 = "               ============>              <========================>              <========================>              <============                     "
    fil_l3 = "               ============>              <========================>              <========================>              <============                     "
    fil_l4 = "                           >              <                        >              <                        >              <                                 "
    
    global saldo
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    CYAN_BLUE = curses.color_pair(1)
    MAGENTA_WHITE = curses.color_pair(2)
    ventana_bonus.clear()
    ventana_bonus.attron(CYAN_BLUE)
    ventana_bonus.border()
    ventana_bonus.attroff(CYAN_BLUE)    
    ventana_bonus.refresh()
    ventana_principal.nodelay(0)
    ventana_principal.clear()
    ventana_principal.addstr(1, 1, col_l1, CYAN_BLUE)
    ventana_principal.addstr(2, 1, col_l2, CYAN_BLUE)
    ventana_principal.addstr(3, 1, col_l3, CYAN_BLUE)
    ventana_principal.addstr(4, 1, col_l4, CYAN_BLUE)
    ventana_principal.addstr(5, 1, col_l5, CYAN_BLUE)
    ventana_principal.addstr(6, 1, col_l6, CYAN_BLUE)


    ventana_principal.attron(MAGENTA_WHITE)
    ventana_principal.border()
    ventana_principal.attroff(MAGENTA_WHITE)
    ventana_principal.refresh()
    pad1_1 = curses.newpad(10,10)
    pad1_2 = curses.newpad(10,10)
    pad1_3 = curses.newpad(10,10)
    pad2_1 = curses.newpad(10,10)
    pad2_2 = curses.newpad(10,10)
    pad2_3 = curses.newpad(10,10)
    pad3_1 = curses.newpad(10,10)
    pad3_2 = curses.newpad(10,10)
    pad3_3 = curses.newpad(10,10)

    a = "    ___      /   |    / /| |   / ___ |  /_/  |_|            "
    k = "    __ __    / //_/   / , <    / /| |   /_/ |_|             "
    q = "    _____   / __  /  / / / /  / /_/ /   \___\_\             "
    j = "       __       / /  __  / /  / /_/ /   \____/              "
    x = "   _  __    | |/ /    |   /    /   |    /_/|_|              "
    
    rueda_col1 = [a, k, k, q, q, q, j, j, j, j, x, x, x, x, x]
    rueda_col1 = rueda_col1 * 5
   

    pad1_1.refresh(0, 0, 46, 52, 52, 72) #FILA BAJA
    pad2_1.refresh(0, 0, 46, 92, 52, 112)
    pad3_1.refresh(0, 0, 46, 132, 52, 152)

    pad1_2.refresh(0, 0, 39, 52, 45, 72)    #FILA MEDIA
    pad2_2.refresh(0, 0, 39, 92, 45, 112)
    pad3_2.refresh(0, 0, 39, 132, 45, 152)

    pad1_3.refresh(0, 0, 32, 52, 38, 72)    #FILA ALTA
    pad2_3.refresh(0, 0, 32, 92, 38, 112)
    pad3_3.refresh(0, 0, 32, 132, 38, 152)



    vueltas1 = random.randrange(5, 30)
    vueltas2 = random.randrange(25, 45)
    vueltas3 = random.randrange(40, 60)
    random_num1 = random.randrange(1, 15)
    random_num2 = random.randrange(1, 15)
    random_num3 = random.randrange(1, 15)

    for i in range(vueltas3+1):
        
        if vueltas1 > i:
            borrar1(pad1_1, pad1_2, pad1_3)
            random_icono1_1 = rueda_col1[random_num1 +1 + i]
            pad1_3.addstr(random_icono1_1)
            
            random_icono1_2 = rueda_col1[random_num1 + i]
            pad1_2.addstr(random_icono1_2)
            
            random_icono1_3 = rueda_col1[random_num1 - 1 + i]
            pad1_1.addstr(random_icono1_3)
            refresca(pad1_1, pad1_2, pad1_3, pad2_1, pad2_2, pad2_3, pad3_1, pad3_2, pad3_3)
        if vueltas1 == i:
            pad1_2.erase()
            final1 = random_num1 + i
            random_icono1_2 = rueda_col1[final1]
            pad1_2.addstr(random_icono1_2, MAGENTA_WHITE)
            refresca(pad1_1, pad1_2, pad1_3, pad2_1, pad2_2, pad2_3, pad3_1, pad3_2, pad3_3)
   
        if vueltas2 > i:
            borrar2(pad2_1, pad2_2, pad2_3)
            random_icono2_1 = rueda_col1[random_num2 +1 + i]
            pad2_3.addstr(random_icono2_1)
            
            random_icono2_2 = rueda_col1[random_num2 + i]
            pad2_2.addstr(random_icono2_2)
           
            random_icono2_3 = rueda_col1[random_num2 - 1 + i]
            pad2_1.addstr(random_icono2_3)
            refresca(pad1_1, pad1_2, pad1_3, pad2_1, pad2_2, pad2_3, pad3_1, pad3_2, pad3_3)
        if vueltas2 == i:
            pad2_2.erase()
            final2 = random_num2 + i
            random_icono2_2 = rueda_col1[final2]
            pad2_2.addstr(random_icono2_2, MAGENTA_WHITE)
            refresca(pad1_1, pad1_2, pad1_3, pad2_1, pad2_2, pad2_3, pad3_1, pad3_2, pad3_3)

        if vueltas3 > i:
            borrar3(pad3_1, pad3_2, pad3_3)
            random_icono3_1 = rueda_col1[random_num3 +1 + i]
            pad3_3.addstr(random_icono3_1)
            
            random_icono3_2 = rueda_col1[random_num3 + i]
            pad3_2.addstr(random_icono3_2)
           
            random_icono3_3 = rueda_col1[random_num3 - 1 + i]
            pad3_1.addstr(random_icono3_3)
            refresca(pad1_1, pad1_2, pad1_3, pad2_1, pad2_2, pad2_3, pad3_1, pad3_2, pad3_3)
        if vueltas3 == i:
            pad3_2.erase()
            final3 = random_num3 + i
            random_icono3_2 = rueda_col1[final3]
        
            pad3_2.addstr(random_icono3_2, MAGENTA_WHITE)
            
            ventana_principal.addstr(16, 1, fil_l1, MAGENTA_WHITE)
            ventana_principal.addstr(17, 1, fil_l2, MAGENTA_WHITE)
            ventana_principal.addstr(18, 1, fil_l3, MAGENTA_WHITE)
            ventana_principal.addstr(19, 1, fil_l4, MAGENTA_WHITE)
            ventana_principal.refresh()
            refresca(pad1_1, pad1_2, pad1_3, pad2_1, pad2_2, pad2_3, pad3_1, pad3_2, pad3_3)
            
        time.sleep(i*0.0005) #0.05
        
        
    saldo = check_premios(random_icono1_2, random_icono2_2, random_icono3_2, ventana_bonus, ventana_premios)
    
    ventana_bank(banca, saldo, False)
    
    ventana_principal.getch()
    ventana_principal.clear()
    
    ventana_principal.refresh()


def check_premios(final1, final2, final3, ventana_bonus, ventana_premios):
    global saldo
    global letra
    if final1 == final2 and final1 == final3:
        
        if final1 == "    ___      /   |    / /| |   / ___ |  /_/  |_|            ":
            letra = "a"
            saldo = saldo + 1000
        if final1 == "    __ __    / //_/   / , <    / /| |   /_/ |_|             ":
            letra = "k"
            saldo = saldo + 500
        if final1 == "    _____   / __  /  / / / /  / /_/ /   \___\_\             ":
            letra = "q"
            saldo = saldo + 250
        if final1 == "       __       / /  __  / /  / /_/ /   \____/              ":
            letra = "j"
            saldo = saldo + 150
        if final1 == "   _  __    | |/ /    |   /    /   |    /_/|_|              ":
            letra = "x"
            saldo = saldo + 50
        

        premio(ventana_bonus, ventana_premios)
    else:
        saldo = saldo - 10
    return saldo

def premio(ventana_bonus, ventana_premios):
    col_l1 = "                                               ██╗██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗                                                 "
    col_l2 = "                                               ██║╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║                                                 "
    col_l3 = "                                               ██║ ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║                                                 "
    col_l4 = "                                               ╚═╝  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝                                                 "
    col_l5 = "                                               ██╗   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗                                                 "
    col_l6 = "                                               ╚═╝   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝                                                 "
    ventana_bonus.addstr(4, 1, col_l1)
    ventana_bonus.addstr(5, 1, col_l2)
    ventana_bonus.addstr(6, 1, col_l3)
    ventana_bonus.addstr(7, 1, col_l4)
    ventana_bonus.addstr(8, 1, col_l5)
    ventana_bonus.addstr(9, 1, col_l6)
    ventana_bonus.refresh()
    winsound.Beep(2500, 200)
    winsound.Beep(3000, 200)
    winsound.Beep(3500, 200)
    doble_nada(ventana_premios, True, letra)
    
def doble_nada(ventana_premios, blink, letra):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    CYAN_BLUE = curses.color_pair(1)
    MAGENTA_WHITE = curses.color_pair(2)
    ventana_premios.erase() 
 
    premios_text_a = """
      ___   
     /   |  
    / /| |  x1000
   / ___ |  
  /_/  |_|  
"""
    premios_text_k = """
      __ __ 
     / //_/ 
    / ,<    x500
   / /| |   
  /_/ |_|   
"""
    premios_text_q = """
      _____ 
    / __  / 
   / / / /  x250
  / /_/ /   
  \___\_\   
"""
    premios_text_j = """
         __ 
        / / 
   __  / /  x150
  / /_/ /   
  \____/    
"""
    premios_text_x = """
     _  __  
    | |/ /  
    |   /   x50
   /   |    
  /_/|_|    
"""
    ventana_premios.addstr(0,5, premios_text_a)
    ventana_premios.addstr(6,5, premios_text_k)
    ventana_premios.addstr(12,5, premios_text_q)
    ventana_premios.addstr(18,5, premios_text_j)
    ventana_premios.addstr(24,5, premios_text_x)
    if blink:
        
            if letra == "a":
                ventana_premios.addstr(0,5, premios_text_a, MAGENTA_WHITE)
                ventana_premios.refresh()
               
            if letra == "k":
                ventana_premios.addstr(6,5, premios_text_k, MAGENTA_WHITE)

            if letra == "q":
                ventana_premios.addstr(12,5, premios_text_q, MAGENTA_WHITE)
                
            if letra == "j":
                ventana_premios.addstr(18,5, premios_text_j, MAGENTA_WHITE)
                
            if letra == "x":
                ventana_premios.addstr(24,5, premios_text_x, MAGENTA_WHITE)
               
        
     
    ventana_premios.attron(CYAN_BLUE)
    ventana_premios.border()
    ventana_premios.attroff(CYAN_BLUE)  
    
    ventana_premios.refresh()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    CYAN_BLUE = curses.color_pair(1)
    MAGENTA_WHITE = curses.color_pair(2)
    #curses.LINES -1, curses.COLS -1
    global saldo
    
    stdscr.clear()
    stdscr.nodelay(1)
    # turn off cursor blinking
    curses.curs_set(0)
    stdscr.refresh()
    
    
    
 

    
       
        
    title = curses.newwin(8, 198, 1, 1) #title window
    pie_pagina = curses.newwin(3, 198, 56, 1) # inferior window
    menu = curses.newwin(15, 20, 9, 1) #menu window
    banca = curses.newwin(47, 20, 9, 179) #banca window
    ventana_bonus = curses.newwin(15, 158, 9, 21) #bonus window
    ventana_principal = curses.newwin(32, 158, 24, 21) #main window
    ventana_premios = curses.newwin(32, 20, 24, 1)
    

    stdscr.erase()
    title.erase()
    menu.erase()
    pie_pagina.erase()
    banca.erase()
    ventana_principal.erase()
    ventana_bonus.erase()
    ventana_premios.erase()

    stdscr.attron(CYAN_BLUE)
    stdscr.border()
    stdscr.attroff(CYAN_BLUE)
    title.attron(CYAN_BLUE)
    title.border()
    title.attroff(CYAN_BLUE)
    pie_pagina.attron(CYAN_BLUE)
    pie_pagina.border()
    pie_pagina.attroff(CYAN_BLUE)
    menu.attron(CYAN_BLUE)
    menu.border()
    menu.attroff(CYAN_BLUE)
    banca.attron(CYAN_BLUE)
    banca.border()
    banca.attroff(CYAN_BLUE)
    ventana_bonus.attron(CYAN_BLUE)
    ventana_bonus.border()
    ventana_bonus.attroff(CYAN_BLUE)
    ventana_principal.attron(CYAN_BLUE)
    ventana_principal.border()
    ventana_principal.attroff(CYAN_BLUE)
    ventana_premios.attron(CYAN_BLUE)
    ventana_premios.border()
    ventana_premios.attroff(CYAN_BLUE)
    

    title.addstr(1, 1, logo_l1 , CYAN_BLUE)
    title.addstr(2, 1, logo_l2 , CYAN_BLUE)
    title.addstr(3, 1, logo_l3 , CYAN_BLUE)
    title.addstr(4, 1, logo_l4 , CYAN_BLUE) 
    title.addstr(5, 1, logo_l5 , CYAN_BLUE) 
    title.addstr(6, 1, logo_l6 , CYAN_BLUE) 
    
    
   
    

    pie_pagina.addstr(1, 80, "SLOT MACHINE by Andres Gregorio 2024")
    
    
    indice = 0
     
    not_selection = True


            

    stdscr.refresh()
    title.refresh()
    menu.refresh()
    pie_pagina.refresh()
    banca.refresh()
    ventana_principal.refresh()
    ventana_bonus.refresh()
    ventana_premios.refresh()
    doble_nada(ventana_premios, False, letra)
    ventana_bank(banca, saldo, False)
    menu_selec(menu, indice)
    
    while not_selection:
          
            
        
        key = menu.getch()

        if key == curses.KEY_UP:
            indice = indice  -1
            if indice == -1:
                indice = 3
            
            
        elif key == curses.KEY_DOWN:
            indice = indice + 1
            if indice == 4:
                indice = 0
            

        elif key == curses.KEY_ENTER or key in [10, 13]:
            not_selection = False
            if indice == 3:
                reset_windows(menu, banca, ventana_principal, ventana_bonus, ventana_premios)
                not_selection = ventana_salida()
                ventana_principal.erase()
                ventana_principal.refresh()

            if indice == 0:
                 reset_windows(menu, banca, ventana_principal, ventana_bonus, ventana_premios)
                 saldo = ventana_bank(banca, saldo, True)
                 not_selection = True

            if indice == 1:
               
                reset_windows(menu, banca, ventana_principal, ventana_bonus, ventana_premios)
                play(ventana_principal, ventana_bonus, bonus, is_jugando, banca, ventana_premios)
                not_selection = True

        reset_windows(menu, banca, ventana_principal, ventana_bonus, ventana_premios)
        menu_selec(menu, indice)

    


    stdscr.refresh()
    title.refresh()
    menu.refresh()
    pie_pagina.refresh()
    banca.refresh()
    ventana_principal.refresh()
    ventana_bonus.refresh()
    menu.getch()

wrapper(main)

