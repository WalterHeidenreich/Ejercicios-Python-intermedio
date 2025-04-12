nombre_archivo = input("Ingresa el nombre del archivo: ")

try:
   
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
    print("Creando el archivo.")
    
    try:
       
        with open(nombre_archivo, 'w') as archivo:
           
            print(f"Archivo '{nombre_archivo}' creado correctamente.")
    
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

except Exception as e:
    print(f"Error inesperado: {e}")