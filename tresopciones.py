Letra = input("Introduce una letra del abecedario \n")
Listadeletras = ["A", "B", "C"]

while Letra not in Listadeletras:
    Letra = input ("Dame otra opcion \n")
    if Letra in Listadeletras:
            print("Esta opcion es valida")
        
