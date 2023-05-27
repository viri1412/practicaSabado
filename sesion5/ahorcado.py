import random

from paquete import palabras,monitos

def getRandomWord(wordList):
    # Esta función devuelve una palabra aleatoria de la lista de palabras pasada.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(monitos.monitos[len(missedLetters)])
    print()

    print('Letras fallidas:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Reemplazar guiones bajos con letras adivinadas correctamente.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Mostrar la palabra secreta con espacios entre cada letra.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Devuelve la letra que el jugador ingresó. Esta función se asegura de que el jugador haya ingresado una sola letra y no otra cosa.
    while True:
        print('Adivina una letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor, ingresa una sola letra.')
        elif guess in alreadyGuessed:
            print('Ya has adivinado esa letra. Elige otra.')
        elif guess not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor, ingresa una LETRA.')
        else:
            return guess

def playAgain():
    # Esta función devuelve True si el jugador quiere jugar de nuevo; de lo contrario, devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

print('A H O R C A D O')
print('Adivina los nombres de ciudades en México, son ciudades de una sola palabra, sin acentos o mayúsculas')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(palabras.palabras)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Dejar que el jugador ingrese una letra.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Comprobar si el jugador ha ganado.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('¡Sí! La palabra secreta es "' + secretWord + '" ¡Has ganado!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Comprobar si el jugador ha adivinado demasiadas veces y ha perdido.
        if len(missedLetters) == len(monitos.monitos) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('¡Te has quedado sin intentos!\nDespués de ' +
                str(len(missedLetters)) + ' intentos fallidos y ' +
                str(len(correctLetters)) + ' intentos correctos, ' +
                'la palabra era "' + secretWord + '"')
            gameIsDone = True

    # Preguntar al jugador si quiere jugar de nuevo (solo si el juego ha terminado).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(palabras.palabras)
        else:
            break