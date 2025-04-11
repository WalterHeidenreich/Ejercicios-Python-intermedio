
try:
    n1=int(input("Escribi un numero:"))
    n2=int(input("Escribi otro numero:"))
    resultado=n1/ n2
    print("El resultado es:", resultado)
except ZeroDivisionError as e:
    print(f"Hay un error, no se puede dividir por cero. {e}")    
except ValueError as b:
     print(f"Hay un error, numero no valido. {b}")  
