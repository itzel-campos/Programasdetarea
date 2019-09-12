Palabra = input ("Dame la palabra que quieres verificar \n")
Palindromo = Palabra [:: -1]

Palabrasinespacio = Palindromo.split(",")

if Palabra == Palabrasinespacio:
    print ("Esta palabra es un palindromo {}" .format (Palindromo))
else :
    print("Esta palabra no es un palindromo")

