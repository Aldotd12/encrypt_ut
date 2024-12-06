from cryptography.fernet import Fernet

CLAVE = Fernet.generate_key()
fernet = Fernet(CLAVE)


def encriptar_texto(texto):
    texto_bytes = texto.encode('utf-8') 
    texto_encriptado = fernet.encrypt(texto_bytes)  
    return texto_encriptado.decode('utf-8')  


def desencriptar_texto(texto_encriptado):
    texto_bytes = texto_encriptado.encode('utf-8')  
    texto_desencriptado = fernet.decrypt(texto_bytes)  
    return texto_desencriptado.decode('utf-8')  


def encriptar_imagen(ruta_imagen):
    with open(ruta_imagen, 'rb') as archivo_imagen:
        imagen_bytes = archivo_imagen.read()
    imagen_encriptada = fernet.encrypt(imagen_bytes)
    return imagen_encriptada
    
def desencriptar_imagen(imagen_encriptada, archivo_salida):
    imagen_bytes_desencriptada = fernet.decrypt(imagen_encriptada)
    with open(archivo_salida, 'wb') as archivo_salida_imagen:
        archivo_salida_imagen.write(imagen_bytes_desencriptada)
        
    print(f"Imagen desencriptada y guardad en {archivo_salida}")               