import base64
import pyDes

Rta=int(input("Bienvenido\n\n1.1. Cifrar\n2. Descifrar\n\nRta: "))

if Rta==1:
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
  print("Guardado como ",""+archivo)
else:
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

  print("Guardado como ", ""+archivo)