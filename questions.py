import random
words = {
    "Programación" : ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "Clubes" : ["lanus", "quilmes", "river", "boca", "chacarita", "ferro", "velez", "temperley"],
    "Computadora" : ["procesador", "grafica", "ram", "fuente", "gabinete", "monitor", "teclado", "mouse", "auriculares"]
}

print("¡Bienvenido al Ahorcado!")
print("Escriba el nombre de alguna de las siguientes categorías para jugar:")

for key in words:
    print(f" {key}")
    
while True:
    # le decimos que elija una categoría
    categoria_elegida = input("Ingrese el nombre de la categoría: ").capitalize()
    
    # nos fijamos si existe esa categoría
    if categoria_elegida in words:
        # mezclamos la categoría para que salgan palabras al azar y no se repitan
        lista_palabras = random.sample(words[categoria_elegida], len(words[categoria_elegida]))
        break
    else:    
        print("Categoría no existente")

for word in lista_palabras:
    guessed = []
    attempts = 6
    gano = False
    puntaje = 0
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if len(letter) == 1 and letter.isalpha():    
            if "_" not in progress:
                print("¡Ganaste!")
                gano = True
                puntaje += 6
                break
            elif "_" in progress:
                print(f"Intentos restantes: {attempts}")
                print(f"Letras usadas: {', '.join(guessed)}")
                letter = input("Ingresá una letra: ")
                if letter in guessed:
                    print("Ya usaste esa letra.")
                elif letter in word:
                    guessed.append(letter)
                    print("¡Bien! Esa letra está en la palabra.")
                else:
                    guessed.append(letter)
                    attempts -= 1
                    puntaje -= 1
                    print("Esa letra no está en la palabra.")
                    print()
        else:
            print("Entrada no válida")

    if not gano:
        puntaje = 0
        print(f"¡Perdiste! La palabra era: {word}")

    print(f"Puntuación: {puntaje}/6")