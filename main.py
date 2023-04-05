#Llama al modulo principal y realiza las interaciones (entrada y salida)
import minecraft

n = input("$ ")
while n != "init":
    n = input("$ ")
print("")
print("Welcome to the world of minecraft 2d xyz")
print("")
x = minecraft.draw_world_empty()
z = minecraft.draw_player(x)
print("")

wood_blocks = 0
stone_blocks = 0

move_x = 1
move_y = 10
bloque_madera = " 3 "
bloque_piedra = " 5 "

#Al final de cada input agregar un espacio
movimientos = input("$ ")
while movimientos != "finish":
    lista = movimientos.split(", ")
    nuevos_movimientos = []
    for c in lista:
        if c not in ["build wood ","build stone ","extract ", "collect "]:
            l = c.split(" ",1)
            j = int(l[0])*l[1]
            nuevos_movimientos.append(j)
        else:
            nuevos_movimientos.append(c)

    nueva_lista = []
    for k in nuevos_movimientos:
        if k not in ["build wood ","build stone ","extract ", "collect "]:
            m = k.split(" ")
            for b in m:
                nueva_lista.append(b)
        else:
            nueva_lista.append(k)
    
    for i in nueva_lista:
        if i == "up":
            move_y = move_y - 1
        elif i == "down":
            move_y = move_y + 1
        elif i == "right":
            move_x = move_x + 1
        elif i == "left":
            move_x = move_x - 1
        elif i == "destroy ":
            minecraft.destroy_blocks(move_x, move_y, z)
        elif i == "extract ":
            if z[move_y][move_x+1] == " 3 ":
                wood_blocks = wood_blocks + 1
            elif z[move_y][move_x+1] == " 5 ":
                stone_blocks = stone_blocks + 1
            minecraft.collect_blocks(move_x, move_y, z)
        elif i =="build wood ":
            if wood_blocks >= 1:
                wood_blocks = wood_blocks - 1
                minecraft.build(move_x, move_y, z, bloque_madera)
            else:
                print("No tienes bloques de madera")
        elif i == "build stone ":
            if stone_blocks >= 1:
                stone_blocks = stone_blocks - 1
                minecraft.build(move_x, move_y, z, bloque_piedra)
            else:
                print("No tienes bloques de piedra")
    if move_x <= -1 or move_x+1 >= 40:
        print("Usted se salío del mapa")
    elif move_y <= 0 or move_y >= 19:
        print("Usted se salío del mapa")
    else:
        minecraft.move_player(move_x, move_y, z)
        print("$ wood blocks =",wood_blocks)
        print("$ stone blocks =",stone_blocks)
    print("")
    movimientos = input("$ ")