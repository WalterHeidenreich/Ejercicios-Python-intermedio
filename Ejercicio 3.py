diccionario={"nombre": "Walter", "apellido": "Perez", "edad":30}
try: 
   clave=diccionario ["domicilio"]
except KeyError:
    print("La clave domicilio no existe")