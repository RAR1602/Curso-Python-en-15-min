print("Hola mundo soy Roberto Abalo.")
print("Estos son mis primeros pasos en Python.")


#Comentario de código
print("A ver hasta donde llego.")


"""
Esto tambien es un comentario de código.
"""

texto = "Estoy comenzando en Python."
nombre = "Roberto"
apellido1 = "Abalo"
apellido2 = "Rodríguez"
altura = 1.79
anho = 2023
texto2 = "Yo mido"

print (anho)

#Concatenación
print("Me llamo" + " " + nombre + " " + apellido1 + " " + apellido2 + ".")
print(f"{texto2}, {altura} metros de altura en el {str(anho)}.") # El método str te convierte los valores a String

#Entrada de datos
correoEletronico = input("¿Cuál es tu correo electronico?\n")
print("Tu email es: " + correoEletronico)



# Condiciones

alturaUsuario = int(input("¿Cuál es tu altura?: "))
sexoUsuario = input("¿Hombre (H) ó Mujer (M)?")

mediaEspañola = 162
if sexoUsuario == "H":
    mediaEspañola = 176


if alturaUsuario >= mediaEspañola:
    print("Estas por encima de la média española.")
elif alturaUsuario <= mediaEspañola:
    print("Estas por debajo de la média española.")
else :
    print("Estas justo en la média española")



# Funciones



def mostrarAltura():
    alturaUsuario = int(input("¿Cuál es tu altura?: "))
    sexoUsuario = input("¿Hombre (H) ó Mujer (M)?")

    mediaEspañola = 162
    if sexoUsuario == "H":
        mediaEspañola = 176

    if alturaUsuario >= mediaEspañola:
        print("Estas por encima de la média española.")
    elif alturaUsuario <= mediaEspañola:
        print("Estas por debajo de la média española.")
    else :
        print("Estas justo en la média española")

mostrarAltura()
mostrarAltura()

numero = int(input("Introduzca un número: "))

def calculoPar(varNumero):
    resultado = ""

    if varNumero == 0:
        resultado = "El número introducido es 0." 
    elif(varNumero % 2 == 0):
        resultado = f"El número {varNumero}, es par."
    else:
        resultado = f"El número {varNumero}, es impar." 
    return resultado

print(calculoPar(numero))

personas = ["Roberto", "Mar", "Mysha", "Yara"]

print (personas[2])

for persona in personas:
    print("-" + persona)