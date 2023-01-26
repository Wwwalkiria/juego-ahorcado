
import random
import time

print("\x1b[1;33m"+"*" * 40)
print("***","\x1b[1;35m" "BIENVENID@ AL JUEGO DEL AHORCADO","\x1b[1;33m""***")
print("*" * 40)

lista1 = [ "alemania", "belice", "dinamarca", "eslovaquia", "portugal", "finlandia" , "gambia",
    "islandia", "paises bajos", "kirguistan", "mozambique" , "tailandia"," bolivia" , " uruguay" ]

lista2 = ["magenta", "amarillo", "violeta","marron" , "turquesa", "verde","blanco" , "indigo",]

lista3= ["el padrino" , " cinema paradiso" , "mago de Oz" ," psicosis","amityville", "blade runner",
         "tiburon" , " toy story", "hellraiser" , "rocky" , "Rambo", "el club de la palea", ]
lista4= ["desoxirribonucleico","esternocleidomastoideo","electroencefalografista ", "paralelepípedo",
           "palindromo","delicuescencia", "serigrafia", "resiliencia","heterodoxo","confinamiento",
                 "sintaxis","armagedon","impoluto","transustanciacion","sexagesimal"]


nombre=input("\x1b[1;36m""como te llamas? ""\x1b[1;32m")
print(" ")
print("hola, "+nombre,"... " )
print(" ")
print(" ", "    ","     ", "    ", "    ","\x1b[1;38m""ᕙ(`▿´)ᕗ","\x1b[1;32m" "es hora de jugar!")
time.sleep(1)
print("\x1b[1;31m"+"*" * 20)
print("*","\x1b[1;37m" "  R E G L A S:  ","\x1b[1;31m""*")
print("*" * 20)
print(" ")
print("\x1b[1;32m""LETRA EQUIVOCADA:  pierde", "\x1b[1;31m", " ♥  ","\x1b[1;32m""una vida")
print("PALABRA EQUIVOCADA:  pierde", "\x1b[1;31m", " ♥ ♥ ♥ ","\x1b[1;32m""tres vidas")
print(" ")
input("\x1b[1;36m"" [enter] para continuar.. ""\x1b[1;32m")

print(" ")
time.sleep(0.5)
print ("ahora elije una categoria de palabras para jugar:"  )
time.sleep(1)
print("\x1b[1;36m"" * PAISES [1] ")
print("\x1b[1;33m"" * COLORES [2] ")
print("\x1b[1;35m"" * PELICULAS [3] ")
print("\x1b[1;31m"" * PALABRAS XTRA DIFICILES [4]""\x1b[1;32m")


opcion = 0
while opcion not in (1,2,3,4):
    print(" ")
    opcion= int(input("tu eleccion es: "))
    if opcion == 1:
        palabraElegida = (random.choice(lista1)).upper()
    elif opcion == 2:
        palabraElegida = (random.choice(lista2)).upper()
    elif opcion == 3:
        palabraElegida = (random.choice(lista3)).upper()
    elif opcion == 4:
        palabraElegida = (random.choice(lista4)).upper()
    else:
        print("OPCION INCORRECTA: ingrese un Nro del 1 al 4 ")


if opcion == 1:
    print( " elegiste:""\x1b[1;36m"" PAISES ""\x1b[1;32m")
if opcion == 2:
    print( " Elegiste ""\x1b[1;33m"" COLORES ""\x1b[1;32m")
if opcion == 3:
    print( " Elegiste ""\x1b[1;35m"" PELICULAS ""\x1b[1;32m")
if opcion == 4:
    print(" Elegiste ""\x1b[1;35m"" CATEGORIA INFERNAL ""\x1b[1;32m")
    print("\x1b[1;31m""realmente te deseo mucha suerte(la vas a necesitar!..)""\x1b[1;32m")

time.sleep(0.5)

palabraUsuario=" "
len(palabraElegida)
print(f"la palabra tiene {len(palabraElegida)} letras")
print(" ")
vidas= []
vidas = ["♥", "♥", "♥", "♥", "♥", "♥", "♥"]
vidas= (len(vidas))
print("\x1b[1;31m" "♥", "♥", "♥", "♥", "♥", "♥", "♥")
print ("\x1b[1;32m" "tienes un total de", vidas, " vidas:")
time.sleep(0.5)
print(" ")
print("\x1b[1;38m""comienza a adivinar....""\x1b[1;32m")

while vidas > 0:
    coincidencias = 0
    for letra in palabraElegida:
        if letra in palabraUsuario:
            print(letra,end="\x1b[1;38m""")

        else:
            print("\x1b[1;38m""_",end="")
            coincidencias+= 1
    if coincidencias ==0:
        print(" ")
        print(" ")
        print(" ")
        print("¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ")
        print(" ")
        print(f"\033[5;35m"  "    adivinaste la palabra!!!!! "),
        time.sleep(1)
        print("felicidades!!!")
        time.sleep(1)
        print("GANASTE!!!")
        print("la palabra era: ", "\x1b[1;36m", palabraElegida, "\x1b[1;32m")
        input("\x1b[1;32m""[enter] para terminar ")
        break

    tuletra=input("\x1b[1;32m""\n introduce una letra o arriezga una palabra: ")




    if len(tuletra) == 1:
        palabraUsuario+=tuletra


        if tuletra not in palabraElegida:
            vidas-=1
            if vidas== 0:
                print(" ")
                time.sleep(0.5)
                print("\x1b[1;31m""PERDISTE!  ( ˘︹˘ )""\x1b[1;32m")
            else:
                time.sleep(0.5)
                print(" ")
                print("  ", "    ", "     ", "\x1b[1;31m""equivocacion ( ˘︹˘ )" "\x1b[1;32m"  )
                print(" ")
                print (f"la letra ","\x1b[1;39m", tuletra ,"\x1b[1;32m"," no esta en la palabra" )

                print("te quedan",+vidas," vidas")
                print(" ")
            if vidas == 6:
                print("\x1b[1;31m""♥", "♥", "♥", "♥", "♥", "♥""\x1b[1;32m")
            if vidas == 5:
                print("\x1b[1;31m""♥", "♥", "♥", "♥", "♥""\x1b[1;32m")
            elif vidas == 4:
                print("\x1b[1;31m""♥", "♥", "♥", "♥", "\x1b[1;32m")
            elif vidas == 3:
                print("\x1b[1;31m""♥", "♥", "♥""\x1b[1;32m")
            elif vidas == 2:
                print("\x1b[1;31m""♥", "♥""\x1b[1;32m")
            elif vidas == 1:
                print("\x1b[1;31m""♥", "(Ultima vida)""\x1b[1;32m")



    else:
        if tuletra == palabraElegida:
            print(" ")
            print("¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ")
            time.sleep(0.5)

            print(f"\033[5;35m"  "    adivinaste la palabra!!!!! "),
            time.sleep(1)
            print(" ")
            print("felicidades!!!")
            time.sleep(1)
            print(" ")
            print("GANASTE!!!")
            time.sleep(1)
            print("la palabra era: ", "\x1b[1;36m", palabraElegida, "\x1b[1;32m")
            input("\x1b[1;32m""[enter] para terminar ")
            break



        else:
            vidas-=3
            if vidas <= 0:
                print(" ")
                print("PERDISTE!  ( ˘︹˘ )")
                print("la palabra era: ","\x1b[1;36m",palabraElegida,"\x1b[1;32m")
            else:
                print(" perdiste 3 vidas")
        print("te quedan", +vidas, " vidas")
        if vidas ==5:
                print("\x1b[1;31m""♥","♥", "♥", "♥", "♥""\x1b[1;32m")
        if vidas == 4:
            print("\x1b[1;31m""♥", "♥", "♥", "♥", "\x1b[1;32m")
        if vidas == 3:
            print("\x1b[1;31m""♥", "♥", "♥""\x1b[1;32m")
        elif vidas == 2:
                print("\x1b[1;31m""♥","♥""\x1b[1;32m")
        elif vidas == 1:
                print("\x1b[1;31m""♥","(Ultima vida)""\x1b[1;32m" )
print()
print ("\x1b[1;34m""👍👍👍👍👍""\x1b[1;38m" "gracias por participar","\x1b[1;34m""👍👍👍👍👍")


