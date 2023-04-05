
from colorama import Back, Fore, init, Style
def draw_world_empty():
    init()
    filas = 20
    columnas = 40
    mundo=[]

    for i in range(filas):
        lista = []
        for j in range(columnas):
            if i == 0 and j == 27 or i == 0 and j == 28 or i == 0 and j == 29 or i == 1 and j == 26 or i == 1 and j == 27 or i == 1 and j == 28 or i == 1 and j == 29 or i == 2 and j == 27 or i == 2 and j == 28 or i == 2 and j == 29 or i == 3 and j == 26 or i == 3 and j == 28 or i == 1 and j==30 or i==3 and j == 30:
                lista.append(" 1 ")
            elif i == 2 and j == 21 or i == 3 and j == 20 or i == 3 and j == 21 or i == 3 and j == 22 or i == 4 and j == 19 or i == 4 and j == 20 or i == 4 and j == 21 or i == 4 and j == 22 or i == 4 and j == 23 or i == 5 and j == 4 or i == 5 and j == 10 or i == 5 and j == 16 or i == 5 and j == 18 or i == 5 and j == 19 or i == 5 and j == 20 or i == 5 and j == 21 or i == 5 and j == 22 or i == 5 and j == 23 or i == 5 and j == 24 or i == 6 and j == 3 or i == 6 and j == 4 or i == 6 and j == 5 or i == 6 and j == 9 or i == 6 and j == 10 or i == 6 and j == 11 or i == 6 and j == 15 or i == 6 and j == 16 or i == 6 and j == 17 or i == 7 and j == 2 or i == 7 and j == 3 or i == 7 and j == 4 or i == 7 and j == 5 or i == 7 and j == 6 or i == 7 and j == 8 or i == 7 and j == 9 or i == 7 and j == 10 or i == 7 and j == 11 or i == 7 and j == 12 or i== 7 and j == 14 or i == 7 and j == 15 or i == 7 and j == 16 or i == 7 and j == 17 or i == 7 and j == 18 or i == 7 and j == 24 or i == 7  and j == 28 or i == 8 and j == 23 or i == 8 and j == 24 or i == 8 and j == 25 or i == 8 and j == 27 or i == 8 and j == 28 or i == 8 and j == 29 or i == 12 and j == 0 or i==12 and j == 1 or i == 12 and j == 2 or i == 12 and j == 3 or i == 12 and j == 4 or i == 12 and j == 5 or i == 12 and j == 6 or i == 12 and j == 7 or i == 12 and j == 8 or i == 12 and j == 9 or i == 12 and j == 10 or i == 12 and j == 11 or i == 12 and j == 12 or i == 12 and j == 13 or i == 12 and j == 14 or i == 12 and j == 15 or i == 12 and j == 16 or i == 12 and j == 17 or i == 12 and j == 18 or i == 12 and j == 19 or i == 12 and j == 20 or i == 12 and j == 21 or i == 12 and j == 22 or i == 12 and j == 23 or i == 12 and j == 24 or i == 12 and j == 28 or i == 12 and j == 29 or i == 2 and j == 36 or i == 3 and j == 35 or i == 3 and j == 36 or i == 3 and j == 37 or i ==4 and j==34 or i == 4 and j==35 or i ==4 and j == 36 or  i ==4 and j== 37 or i == 4 and j == 38 or i==5 and j==33 or i == 5 and j==34 or i == 5 and j==35 or i ==5 and j == 36 or  i ==5 and j== 37 or i == 5 and j == 38 or i == 5 and j==39 or i == 7 and j==38 or i==8 and j==37 or i==8 and j==38 or i==8 and j==39 or i==12 and j==30 or i==12 and j==31 or i==12 and j==32 or i==12 and j==33 or i==12 and j==34 or i==12 and j==35 or i==12 and j==36 or i==12 and j==37 or i==12 and j==38 or i==12 and j==39:
                lista.append(" 2 ")
            elif (i == 6 and j ==21) or (i == 7 and j ==21) or (i == 8 and j == 4) or (i == 8 and j == 10) or (i == 8 and j == 16) or (i == 8 and j == 21) or (i == 9 and j == 4) or (i == 9 and j == 10) or (i == 9 and j == 16) or (i == 9 and j == 21) or (i == 9 and j == 24) or (i == 9 and j == 28) or (i == 10 and j == 4 )or (i == 10 and j == 10 )or (i == 10 and j == 16) or (i == 10 and j == 21) or (i == 10 and j == 24) or (i ==10 and j == 28) or (i == 11 and j == 4) or (i == 11 and j == 10) or (i == 11 and j == 16) or (i == 11 and j == 21) or (i == 11 and j == 24) or (i == 11 and j == 28) or (i==6 and j == 36)or (i==7 and j == 36)or (i==8 and j == 36)or (i==9 and j == 36)or (i==10 and j == 36)or (i==11 and j == 36) or (i==9 and j== 38)or (i==10 and j== 38)or (i==11 and j== 38):
                lista.append(" 3 ")
            elif i == 9 and j == 7 or i == 10 and j == 6 or i == 10 and j == 7 or i == 10 and j == 8 or i == 10 and j ==15 or i == 11 and j == 6 or i == 11 and j == 7 or i == 11 and j == 8 or i == 11 and j == 11 or i == 11 and j == 14 or i == 11 and j == 15 or i == 11 and j == 19 or i == 11 and j == 29 or i ==13 and j == 4 or i == 14 and j == 22 or i == 14 and  j == 24 or i == 15 and j == 6 or i == 15 and j == 9 or i == 15 and j == 22 or i == 16 and j == 1 or i == 16 and j == 22 or i == 17 and j == 4 or i == 17 and j == 22 or i == 18 and j == 6 or i == 18 and j == 14 or i == 18 and j == 28 or i == 11 and j ==34 or i==15 and j==33 or i==15 and j==36 or i==17 and j==36 or i==17 and j==39:
                lista.append(" 5 ")
            elif i == 12 and j == 25 or i == 12 and j == 26 or i == 12 and j == 27 or i == 13 and j == 25 or i == 13 and j == 26 or i == 13 and j == 27 or i == 14 and j == 25 or i == 14 and j == 26 or i == 14 and j == 27 or i == 15 and j == 25 or i == 15 and j == 26 or i == 15 and j == 27:
                lista.append(" 7 ")
            elif i == 13 and j == 0 or i == 13 and j ==1 or i == 13 and j == 2 or i == 13 and j == 3 or i == 13 and j == 5 or i == 13 and j == 6 or i == 13 and j == 7 or i == 13 and j == 8 or i == 13 and j == 9 or i == 13 and j == 10 or i == 13 and j == 11 or i == 13 and j == 12 or i == 13 and j == 13 or i == 13 and j == 14 or i == 13 and j == 15 or i == 13 and j == 16 or i == 13 and j == 17 or i == 13 and j == 18 or i == 13 and j == 19 or i == 13 and j == 20 or i == 13 and j == 21 or i == 13 and j == 22 or i == 13 and j == 23 or i == 13 and j == 24  or i == 13 and j == 28 or i == 13 and j == 29 or i == 14 and j == 0 or i == 14 and j == 1 or i == 14 and j == 2 or i == 14 and j == 3 or i == 14 and j == 4 or i == 14 and j == 5 or i == 14 and j == 6 or i == 14 and j == 7 or i == 14 and j == 8 or i == 14 and j == 9 or i == 14 and j == 10 or i == 14 and j == 11 or i == 14 and j == 12 or i == 14 and j == 13 or i == 14 and j == 14 or i == 14 and j == 15 or i == 14 and j == 16 or i == 14 and j == 17 or i == 14 and j == 18 or i == 14 and j == 19 or i == 14 and j == 20 or i == 14 and j == 21 or i == 14 and j == 23 or i == 14 and j == 28 or i == 14 and j == 29 or i == 15 and j == 0 or i == 15 and j == 1 or i == 15 and j == 2 or i == 15 and j == 3 or i == 15 and j == 4 or i == 15 and j == 5 or i == 15 and j == 7 or i == 15 and j == 8  or i == 15 and j == 10 or i == 15 and j == 11 or i == 15 and j == 12 or i == 15 and j == 13 or i == 15 and j == 13 or i == 15 and j == 14 or i == 15 and j == 15 or i == 15 and j == 16 or i == 15 and j == 17 or i == 15 and j == 18 or i == 15 and j == 19 or i == 15 and j == 20 or i == 15 and j == 21 or i == 15 and j == 23 or i == 15 and j == 24 or i == 15 and j == 28 or i == 15 and j == 29 or i == 16 and j == 0 or i == 16 and j == 2 or i == 16 and j == 3 or i == 16 and j == 4 or i == 16 and j == 5 or i == 16 and j == 6 or i == 16 and j == 7 or i == 16 and j == 8 or i == 16 and j == 9 or i == 16 and j == 10 or i == 16 and j == 11 or i == 16 and j == 12 or i == 16 and j == 13 or i == 16 and j == 14 or i == 16 and j == 15 or i == 16 and j == 15 or i == 16 and j == 16 or i == 16 and j == 17 or i == 16 and j == 17 or i == 16 and j == 18 or i == 16 and j == 19 or i == 16 and j == 20 or i == 16 and j == 21 or i == 16 and j == 23 or i == 16 and j == 24 or i == 16 and j == 25 or i == 16 and j == 26 or i == 16 and j == 27 or i == 16 and j == 28 or i == 16 and j == 29 or i == 17 and j == 0 or i == 17 and j == 1 or i == 17 and j == 2 or i == 17 and j == 3 or i == 17 and j == 5 or i == 17 and j == 6 or i == 17 and j == 7 or i == 17 and j == 8 or i == 17 and j == 9 or i == 17 and j == 10 or i == 17 and j == 11 or i == 17 and j == 12 or i == 17 and j == 13 or i == 17 and j == 14 or i == 17 and j == 15 or i == 17 and j == 16 or i == 17 and j == 17 or i == 17 and j == 18 or i == 17 and j == 19 or i == 17 and j == 20 or i == 17 and j == 21 or i == 17 and j == 23 or i == 17 and j == 24 or i == 17 and j == 25 or i == 17 and j == 26 or i == 17 and j == 27 or i == 17 and j == 28 or i == 17 and j == 29 or i == 18 and j == 0 or i == 18 and j == 1 or i == 18 and j == 2 or i == 18 and j == 3 or i == 18 and j == 4 or i == 18 and j == 5 or i == 18 and j == 7 or i == 18 and j == 8 or i == 18 and j == 9 or i == 18 and j == 10 or i == 18 and j == 11 or i == 18 and j == 12 or i == 18 and j == 13 or i == 18 and j == 15 or i == 18 and j == 16 or i == 18 and j == 17 or i == 18 and j == 18 or i == 18 and j == 19 or i == 18 and j == 20 or i == 18 and j == 21 or i == 18 and j == 22 or i == 18 and j == 23 or i == 18 and j == 24 or i == 18 and j == 25 or i == 18 and j == 26 or i == 18 and j == 27  or i == 18 and j == 29 or i == 19 or i==13 and j==30 or i == 13 and j==31 or i==13 and j==32 or i==13 and j==33 or i==13 and j==34 or i==13 and j==35 or i==13 and j==36 or i==13 and j==37 or i==13 and j==38 or i==13 and j==39 or i == 14 and j == 30 or i == 14 and j == 31 or i == 14 and j == 32 or i == 14 and j == 33 or i == 14 and j == 34 or i == 14 and j == 35 or i == 14 and j == 36 or i == 14 and j == 37 or i == 14 and j == 38 or i == 14 and j == 39 or i==15 and j==30 or i==15 and j==31 or i==15 and j==32 or i==15 and j==34 or i==15 and j==35 or i==15 and j==37 or i==15 and j==38 or i==15 and j==39 or i==16 and j==30 or i==16 and j==31  or i==16 and j==32  or i==16 and j==33  or i==16 and j==34 or i==16 and j==35 or i==16 and j==36 or i==16 and j==37 or i==16 and j==38 or i==16 and j==39 or i==17 and j==30 or i==17 and j==31 or i==17 and j==32 or i==17 and j==33 or i==17 and j==34 or i==17 and j==35 or i==17 and j==37 or i==17 and j==38 or i==18 and j==30 or i==18 and j==31 or i==18 and j==32 or i==18 and j==33 or i==18 and j==34 or i==18 and j==35 or i==18 and j==36 or i==18 and j==37 or i==18 and j==38 or i==18 and j==39:
                lista.append(" 8 ")
            else:
                lista.append(" 0 ")
        mundo.append(lista)
    return mundo

def draw_world (mundo) :
    init()
    for k in range(20):
        for l in range(30):
            if mundo[k][l] == " 0 ":
                print(Back.LIGHTWHITE_EX + Fore.LIGHTWHITE_EX + " 0 ", end="")
            elif mundo[k][l] == " 1 ":
                print(Back.YELLOW + Fore.YELLOW + " 1 ", end="")
            elif mundo[k][l] == " 2 ":
                print(Back.GREEN + Fore.GREEN + " 2 ", end="")
            elif mundo[k][l] == " 3 ":
                print(Back.RED + Fore.RED + " 3 ", end="")
            elif mundo[k][l] == " 4 ":
                print(Back.CYAN + Fore.CYAN + " 4 ", end="")
            elif mundo[k][l] == " 5 ":
                print(Back.WHITE + Fore.WHITE + " 5 ", end="")
            elif mundo[k][l] == " 6 ":
                print(Back.MAGENTA + Fore.MAGENTA + " 6 ", end="")
            elif mundo[k][l] == " 7 ":
                print(Back.BLUE + Fore.BLUE + " 7 ", end="")
            elif mundo[k][l] == " 8 ":
                print(Back.BLACK + Fore.BLACK + " 8 ", end="")
        print(Style.RESET_ALL)
    return mundo

def draw_player (mundo) :
    init()
    cabeza = mundo[9][1]
    mundo[9][1] = " 4 "
    cuerpo = mundo[10][1]
    mundo[10][1] = " 4 "
    pies = mundo[11][1]
    mundo[11][1] = " 4 "
    seleccionador = mundo[10][2]
    mundo[10][2] = " 6 "
    draw_world(mundo)
    mundo[9][1] = cabeza
    mundo[10][1] = cuerpo
    mundo[11][1] = pies
    mundo[10][2] = seleccionador

    return mundo

def move_player(move_x , move_y , mundo):
    init()
    cabeza = mundo[move_y-1][move_x]
    mundo[move_y-1][move_x] = " 4 "
    cuerpo = mundo[move_y][move_x]
    mundo[move_y][move_x] = " 4 "
    pies = mundo[move_y+1][move_x]
    mundo[move_y+1][move_x] = " 4 "
    seleccionador = mundo[move_y][move_x+1]
    mundo[move_y][move_x+1] = " 6 "
    if move_x>=22 and move_x<32:
        for k in range(20):
            for l in range(move_x-21,move_x+9):
                if mundo[k][l] == " 0 ":
                    print(Back.LIGHTWHITE_EX + Fore.LIGHTWHITE_EX + " 0 ", end="")
                elif mundo[k][l] == " 1 ":
                    print(Back.YELLOW + Fore.YELLOW + " 1 ", end="")
                elif mundo[k][l] == " 2 ":
                    print(Back.GREEN + Fore.GREEN + " 2 ", end="")
                elif mundo[k][l] == " 3 ":
                    print(Back.RED + Fore.RED + " 3 ", end="")
                elif mundo[k][l] == " 4 ":
                    print(Back.CYAN + Fore.CYAN + " 4 ", end="")
                elif mundo[k][l] == " 5 ":
                    print(Back.WHITE + Fore.WHITE + " 5 ", end="")
                elif mundo[k][l] == " 6 ":
                    print(Back.MAGENTA + Fore.MAGENTA + " 6 ", end="")
                elif mundo[k][l] == " 7 ":
                    print(Back.BLUE + Fore.BLUE + " 7 ", end="")
                elif mundo[k][l] == " 8 ":
                    print(Back.BLACK + Fore.BLACK + " 8 ", end="")
            print(Style.RESET_ALL)
        mundo[move_y][move_x] = cuerpo
        mundo[move_y+1][move_x] = pies
        mundo[move_y-1][move_x] = cabeza
        mundo[move_y][move_x+1] = seleccionador
        return mundo
    elif move_x>=32:
        for k in range(20):
            for l in range(10,40):
                if mundo[k][l] == " 0 ":
                    print(Back.LIGHTWHITE_EX + Fore.LIGHTWHITE_EX + " 0 ", end="")
                elif mundo[k][l] == " 1 ":
                    print(Back.YELLOW + Fore.YELLOW + " 1 ", end="")
                elif mundo[k][l] == " 2 ":
                    print(Back.GREEN + Fore.GREEN + " 2 ", end="")
                elif mundo[k][l] == " 3 ":
                    print(Back.RED + Fore.RED + " 3 ", end="")
                elif mundo[k][l] == " 4 ":
                    print(Back.CYAN + Fore.CYAN + " 4 ", end="")
                elif mundo[k][l] == " 5 ":
                    print(Back.WHITE + Fore.WHITE + " 5 ", end="")
                elif mundo[k][l] == " 6 ":
                    print(Back.MAGENTA + Fore.MAGENTA + " 6 ", end="")
                elif mundo[k][l] == " 7 ":
                    print(Back.BLUE + Fore.BLUE + " 7 ", end="")
                elif mundo[k][l] == " 8 ":
                    print(Back.BLACK + Fore.BLACK + " 8 ", end="")
            print(Style.RESET_ALL)
        mundo[move_y][move_x] = cuerpo
        mundo[move_y+1][move_x] = pies
        mundo[move_y-1][move_x] = cabeza
        mundo[move_y][move_x+1] = seleccionador
        return mundo
    else:
        for k in range(20):
            for l in range(30):
                if mundo[k][l] == " 0 ":
                    print(Back.LIGHTWHITE_EX + Fore.LIGHTWHITE_EX + " 0 ", end="")
                elif mundo[k][l] == " 1 ":
                    print(Back.YELLOW + Fore.YELLOW + " 1 ", end="")
                elif mundo[k][l] == " 2 ":
                    print(Back.GREEN + Fore.GREEN + " 2 ", end="")
                elif mundo[k][l] == " 3 ":
                    print(Back.RED + Fore.RED + " 3 ", end="")
                elif mundo[k][l] == " 4 ":
                    print(Back.CYAN + Fore.CYAN + " 4 ", end="")
                elif mundo[k][l] == " 5 ":
                    print(Back.WHITE + Fore.WHITE + " 5 ", end="")
                elif mundo[k][l] == " 6 ":
                    print(Back.MAGENTA + Fore.MAGENTA + " 6 ", end="")
                elif mundo[k][l] == " 7 ":
                    print(Back.BLUE + Fore.BLUE + " 7 ", end="")
                elif mundo[k][l] == " 8 ":
                    print(Back.BLACK + Fore.BLACK + " 8 ", end="")
            print(Style.RESET_ALL)
        mundo[move_y][move_x] = cuerpo
        mundo[move_y+1][move_x] = pies
        mundo[move_y-1][move_x] = cabeza
        mundo[move_y][move_x+1] = seleccionador
        return mundo

def collect_blocks(move_x, move_y, mundo):
    mundo[move_y][move_x+1] = " 0 "
    return mundo
   
def destroy_blocks(move_x,move_y, mundo):
    mundo[move_y][move_x+1] = " 0 "
    return mundo

def build(move_x, move_y, mundo, bloque):
   if bloque == " 3 ":
    mundo[move_y][move_x+1] = " 3 "
    return mundo   
   elif bloque == " 5 ":
    mundo[move_y][move_x+1] = " 5 "
    return mundo