import Crypto
import binascii
import base64
import pyDes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#private_key=""
#public_key=""
random_generator = Crypto.Random.new().read # Fuente segura de Entropía
#Generación de llaves

#       PRIVADA
# Argumentos (Tamaño de llaves,numero aleatorio)
private_key = RSA.generate(1024, random_generator)
print("Llave privada creada")

#       PUBLICA
# Se genera a partir de la llave privada
public_key = private_key.publickey()
print("Llave pública creada")

fd = open("private_key.pem","wb")
fd.write(private_key.exportKey("PEM"))
fd.close()

fd = open("public_key.pem","wb")
fd.write(private_key.publickey().exportKey("PEM"))
fd.close()

    

def descifradoRSA():
    ################################
    #           DESCIFRADO         #
    ################################
    #   Para descifrar se hace uso de la llave privada
    archivo=input("Ingrese el nombre del archivo a cifrar: ")
    with open(archivo, "rb") as img_file:
        image = base64.b64encode(img_file.read())

    
    encrypted_message = base64.b64decode(image)


    cipher = PKCS1_OAEP.new(private_key) #Objeto de descifrado
    message = cipher.decrypt(encrypted_message) #Mensaje en Claro

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(message))
    image.close()
    print("Guardado como ",""+archivo)

def cifradoRSA():
    archivo=input("Ingrese el nombre del archivo a cifrar: ")
    with open(archivo, "rb") as img_file:
        image = base64.b64encode(img_file.read())

    #############################
    #           CIFRADO         #
    #############################

    cipher = PKCS1_OAEP.new(public_key) #Objeto para cifrar
    encrypted_message = cipher.encrypt(image) # MENSAJE CIFRADO
    encrypted64 = base64.b64encode(encrypted_message)

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(encrypted64))
    image.close()
    print("Guardado como ",""+archivo)

def cifradoDES():
    archivo=input("Ingrese el nombre del archivo a cifrar: ")
    with open(archivo, "rb") as img_file:
        image = base64.b64encode(img_file.read())

    key = input("Da la llave de 8 caracteres: ")
    print("Archivo en base64: ", image)

    k = pyDes.des(key.encode(), pyDes.CBC, b"\0\1\0\1\0\1\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted = k.encrypt(image)

    print("Archivo cifrado: ", encrypted)
    encrypted64 = base64.b64encode(encrypted)
    print("Archivo cifrado en base64: ", encrypted64)

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(encrypted64))
    image.close()

def descifradoDES():
    archivo = input("Ingresa el nombre del archivo a descifrar: ") 
    key = input("Ingrese la clave (8 caracteres): ")
    with open(archivo, "rb") as img_file:
        image2 = base64.b64encode(img_file.read())
    print("Archivo leido en base64: ", image2)

    decrypted = base64.b64decode(image2)

    k = pyDes.des(key.encode(), pyDes.CBC, b"\0\1\0\1\0\1\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    decrypted = k.decrypt(decrypted)

    print("Archivo descifrado en base 64: ", decrypted)

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(decrypted))
    image.close()

def seleccionOpcion():
    correcto=False
    numero=0
    while(not correcto):
        try:
            num = int(input("Introduce la opción que deseas: "))
            correcto = True
        except:
            print("Error. Debes introducir un número entero")
    return num

def documentacionInicio():
    print("##########################################\n")
    print("##############\tINTRODUCCION\t################\n")
    print("##########################################\n\n")
    print("El siguiente programa tiene como objetivo realizar el cifrado de y descifrado")
    print("archivos por medio de dos algoritmos, uno simétrico (DES) y otro asimétri (RSA)")
    print("Recordando que el primero usa una llave simétrica, que en este programa se")
    print("ingresará por medio de teclado, y la asimétrica hace uso de dos llaves, una ")
    print("privada y otra pública, que este programa proveerá de manera aleatoria generando")
    print("un archivo .pem que será la llave a utilizar\n\n")
    print("Las opciones que este programa tiene son las siguientes: ")
    print("\t\t1) Cifrado que se hará utilizando DES")
    print("\t\t2) Descifrado que se hará utilizando DES")
    print("\t\t3) Cifrado que se hará utilizando RSA")
    print("\t\t4) Descifrado que se hará utilizando RSA")
    print("\n\nLa generación de llaves privadas y públicas necesarias para RSA se hacen")
    print("en cuanto se inicia este código, pero si se llegaran a necesitar, se guardan en ")
    print("los archivos private_key.pem y public_key.pem")

    input("\n\nIngrese alguna tecla para continuar...\n\n")

salir = False
opcion = 0
documentacionInicio()
while (not salir):
    print("Bienvenido, seleccione la opción que desee.")
    print("1) Cifrado DES")
    print("2) Descifrado DES")
    print("3) Cifrado RSA")
    print("4) Descifrado RSA")
    print("5) Salir")

    opcion = seleccionOpcion()
    if opcion == 1:
        print("Cifrado DES")
        cifradoDES()
    elif opcion == 2:
        print("Descifrado DES")
        descifradoDES()
    elif opcion == 3:
        print("Cifrado RSA")
        cifradoRSA()
    elif opcion == 4:
        print("Descifrado RSA")
        descifradoRSA()
    elif opcion == 5:
        print("Saliendo...")
        salir = True
    else:
        print("La opción debe estar entre 1 y 5")