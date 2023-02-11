import time

def cuentaAtras(n: int):
        for i in range(n, 0, -1):
                print(i)
                time.sleep(1)
        print("¡Despegue!")

cuentaAtras(10)
