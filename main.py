#Rocket technologies S.A.S.
#Programacion del juego Adivina el numero
#By DK

import random

guessTaken = 0 #Cuenta las veces que el jugador participo
minNumber = 1 #este es el rango del numero minimo
maxNumber = 100 #este es el rango maximo del numero

print("Cual es su nombre: ")
userName: str = input() #creamos una variable uername y luego le asignamos lo que el usuario escriba por teclado

numero = random.randint(minNumber, maxNumber)
print("muy bien " + userName + " estoy pensando en un numero, a ver si lo adivinas, el numero esta entre " + str(minNumber) + " y " + str(maxNumber))

while guessTaken <5:
    print ("Es tu turno, Intentalo: ")
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < numero:
        print("Tu numero es muy Bajo " + userName)
    if guess > numero:
        print("Tu numero es demasiado alto " + userName)
    if guess == numero:
        break
if guess == numero:
    print("Bien hecho " + userName + " lo lograste en " + str(guessTaken) + " intentos")
else:
    print ("Lo siento " + userName + " no lo has logrado.")

