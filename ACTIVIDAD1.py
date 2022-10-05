from ast import Break
from asyncio.windows_events import NULL
import random

opcion = 0
numEscogido = 0

numAleatorio = 0

#---------------------------------------------------------------- 

def ahorcado():
    with open("juego_penjat.txt","r") as file:
        alltext=file.read()
        words = list(map(str, alltext.split()))

    palabraRandom=random.choice(words)
    numeroLetras=len(palabraRandom)
    palabra_sin_descubrir = numeroLetras * "_" 
    contador_intentos=numeroLetras*2

    print(palabra_sin_descubrir)

    lista=list(palabra_sin_descubrir)
    count=0
    while contador_intentos>0 and "_" in palabra_sin_descubrir:
        letra=input("Selecciona la letra que crees que esta").upper()
        count=0
        #compruebo por cada letra de la cadena si la letra que me introducen coincide y en ese caso me quedo la posicion y en esa posicion remplazo el simbolo _ por la letra
        for i in palabraRandom:
            if(i==letra):
                lista[count]=letra
                palabra_sin_descubrir="".join(lista)
            
            count=count +1
        print(palabra_sin_descubrir)    
        contador_intentos=contador_intentos-1
        
    if(contador_intentos==0):
        print("Te has quedado sin intentos has perdido")
        file.close()
        juego()
    
    print(palabra_sin_descubrir)  
    print("Has ganado felicidades")
    file.close()
    juego()
            
    




#---------------------------------------------------------------- 

def numeroAleatorio():

    jugada = 0
    
        
    while(jugada < 3):
            numAleatorio=random.randint(1, 10)
            numEscogido = input("Indica un numero entero del 1 al 10 ")
            jugada = jugada + 1

            if(str.isdigit(numEscogido) == True):
                numEscogido = int(numEscogido)
                numAleatorio = int(numAleatorio)
            
                if (numAleatorio != numEscogido):
                    print("No has acertado tu has escogido ",numEscogido," la maquina ha escogido ",numAleatorio)
                    
                    
                    
                else:
                    print("Has acertado tu has escogido ",numEscogido," la maquina ha escogido ",numAleatorio,"\n volviendo al menu principal")
                    juego()
            
        
            else:
                print (numEscogido , " no es un numero valido")
                jugada = jugada - 1
    print("Has superado los intentos maximos volviendo al menu principal")
    juego()
    
#---------------------------------------------------------------- 
def piedraPapelTisores():
    puntosJugador = 0
    puntosMaquina = 0
    while (puntosMaquina < 3 and puntosJugador < 3):
        jugadaEscogida = input("Escoge una jugada: piedra, papel, tisores ")
        jugadaEscogida = jugadaEscogida.lower()
        jugadaPosibles = ["piedra","papel","tisores"]
        jugadaAleatoria = random.randint(0,2)
        jugadaMaquina=jugadaPosibles[jugadaAleatoria]
        
        if(jugadaEscogida == "piedra" or jugadaEscogida == "papel" or jugadaEscogida == "tisores" ):
            if (jugadaMaquina  == jugadaEscogida):
                print("Has empatado la maquina escogio ",jugadaMaquina," tu has escogido ",jugadaEscogida)   
            elif (jugadaMaquina  == "tisores" and jugadaEscogida == "piedra" or jugadaMaquina  == "papel" and jugadaEscogida == "tisores" or jugadaMaquina  == "piedra" and jugadaEscogida == "papel"):
                print("Has ganado la maquina escogio ",jugadaMaquina," tu has escogido ",jugadaEscogida)
                puntosJugador+=1
            else:
                print("Has perdido la maquina escogio ",jugadaMaquina," tu has escogido ",jugadaEscogida)
                puntosMaquina+=1
        else:
            print(jugadaEscogida ," no es una opcion valida")
            piedraPapelTisores()
        
    if (puntosJugador == 3):
        print("Has ganado al mejor de tres")
        juego()
    elif(puntosMaquina == 3 ):
        print("La maquina ha ganado al mejor de tres")
        juego()
#---------------------------------------------------------------- 
        
def juego():
    print("Selecione el juego al que quiere jugar \n 1.Adivina el numero del 1 al 10 \n 2.Paper pedra tisores \n 3.Ahorcado \n 4.Salir")
    
    
    opcion = input("Indica el numero del juego al que quieres jugar ")
    if(str.isdigit(opcion) == True):
        opcion = int(opcion)
        if (opcion >=1 and opcion <= 4 ):
            
            if opcion == 1:
                numeroAleatorio()
            elif opcion == 2:
                piedraPapelTisores()
            elif opcion == 3:
                ahorcado()
            elif opcion == 4:
                print("Hasta la proxima....")
        else:
            print("La opcion " ,opcion," no es valida vuelve a escoger ")
            juego()
    else:
            print("La opcion " ,opcion," no es valida vuelve a escoger ")
            juego()
        
#---------------------------------------------------------------- 




juego()