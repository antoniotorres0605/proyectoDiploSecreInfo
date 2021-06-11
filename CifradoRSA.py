import Crypto
import binascii
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP



random_generator = Crypto.Random.new().read # fuente segura de Entropía

#Generación de llaves
#       PRIVADA
# Argumentos (Tamaño de llaves,numero aleatorio)
private_key = RSA.generate(1024, random_generator)

#       PUBLICA
# Se genera a partir de la llave privada
public_key = private_key.publickey()

#CONVERSIÓN A UTF8
#private_key = private_key.exportKey(format='DER')
#public_key = public_key.exportKey(format='DER')

#private_key = binascii.hexlify(private_key).decode('utf8')
#public_key = binascii.hexlify(public_key).decode('utf8')

#PROCESO INVERSO
#private_key = RSA.importKey(binascii.unhexlify(private_key))
#public_key = private_key.publickey()
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

input("Ingrese alguna tecla para continuar...")
#print(encrypted_message)

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

print(base64.b64decode(message))