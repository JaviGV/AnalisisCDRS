def enproporcion(a, b):
    # Construye el perfil TOTAL cociente a/b (como es natural, componente a componente) de los perfiles proporcionados
    # Imput:    a,b _ perfiles a comparar (con estructura tipo desglose, como la generada por 'analisisphpc(.)')
    #                    Puesto que solo operamos con los subperfilesTotales es indiferente proporcionar un desglose completo
    #                    o un desglose que solo contenga al subperfilTotal
    #
    # Invocación típica:
    #                    dglsmspcallsMieMed = enproporcion(dglsmsMieMed, dglcallsMieMed)
    #
    # NOTA: observese el carácter inverso de ambos parámetros en el resultado (a/b)
    size = len(a[1][a[0][0]])
    if len(b[1][b[0][0]]) != size:
        return False
    else:
        c = [float(a[1][a[0][0]][i])/b[1][b[0][0]][i] for i in range(0, size)]
        return [[("{}/{}".format(a[0][0], b[0][0]), "rat")], {("{}/{}".format(a[0][0], b[0][0]), "rat"):c}]