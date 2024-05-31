import random

def seleccionar_palabra():
    palabras = ["python", "desarrollo", "ahorcado", "programacion"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    return progreso

def ahorcado():
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 6
    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos > 0:
        progreso = mostrar_progreso(palabra, letras_adivinadas)
        print(f"Palabra: {progreso}")
        letra = input("Adivina una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            letras_adivinadas.append(letra)
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")
        
        if set(palabra) <= set(letras_adivinadas):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break
    else:
        print(f"Has perdido. La palabra era: {palabra}")

if __name__ == "__main__":
    ahorcado()
