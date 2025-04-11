try:
    n1=int(input("Escribi un numero:"))
    n2=("Esto es una cadena:")
    resultado=sum(n1, n2)
    print("El resultado es:", resultado)
except TypeError:
    print(f"Error, una cadena no se puede sumar a un numero")


