import msvcrt
import time

def esperaSalida():
    continuar = True
    tiempoLimite = 4
    print("Presiona Enter para salir o espera {} segundos...".format(tiempoLimite))
    inicio = time.time()

    while continuar:
        # Verifica si se ha presionado una tecla
        if msvcrt.kbhit():
            entrada = msvcrt.getch().decode()
            if entrada == "\r":
                continuar = False
        elif time.time() - inicio > tiempoLimite:
            continuar = False

    return (time.time() - inicio > tiempoLimite)