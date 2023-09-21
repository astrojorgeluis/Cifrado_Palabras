entrada = input("Bienvenido al cifrado chapow, que necesitas? \
                : \n 0 - Cifrar una frase \n 1 - Descrifrar una frase\nRespuesta : ")

if entrada == "0":

    palabra = input("Ingresa tu frase a cifrar : ")
    palabra2 = ""
    pos = 2
    for letra in palabra:
        palabra2 = palabra2+palabra[pos]
        pos = pos - 1
    palabra2 = palabra2.lower()
    print("Tu frase cifrada es :",palabra2)

elif entrada == "1":
    palabra2 = input("Ingresa tu frase a descifrar : ")
    pos = 2
    palabra3 = ""
    for letra in palabra2:
        palabra3 = palabra3+palabra2[pos]
        pos = pos - 1
    palabra3 = palabra3.lower()
    print("Tu frase descifrada es :",palabra3)

else :
    "Input invalido, ingresa una de las opciones"
