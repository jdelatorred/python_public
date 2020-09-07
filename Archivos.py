try:
    #archivo abieto para escritura
    archivo = open("texto.txt", "w")

    print archivo

    archivo.write("Linea uno\nLinea dos\nLinea tres\nLinea Cuatro\nLinea Cinco")

    archivo.close()

    #archivo abieto para adicionar
    archivo = open("texto.txt", "a")

    archivo.write("\nLinea Seis\nLinea Siete\nLinea Ocho\nLinea Nueve\nLinea Diez")

    archivo.close()

    #archivo abieto para lectura
    archivo = open("texto.txt", "r")

    while 1:
        texto = archivo.readline()
        if texto == "":
            break
        else:
            print texto

    archivo.close()

except:
    print 'No existe el archivo'
