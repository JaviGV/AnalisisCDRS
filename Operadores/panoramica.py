def panoramica(*perfiles):
    # Construye (como unión disjunta) un perfil constituido por todos los subperfilestotales de los distintos perfiles  proporcionados.
    #    Si el conjunto de perfiles proporcionado es vacío retorna un perfil por horas (24-dimensional) nulo
    # Imput:       perfiles _ un numero indefinido de perfiles (con estructura tipo desglose: como genera 'analisisphpc(.)')
    #                   Nótese que, puesto que sólo intervienen los subperfilesTotales, es indiferente proporcionar
    #                   un desglose completo o un desglose que sólo contenga al subperfilTotal para cada perfil
    #
    # Invocación típica:
    #                     totalescallsMMNbNv = panoramica(dglcallsMieMed, dglcalls141231, dglcalls141224)

    # CÓDIGO
    if perfiles:
        Totales = []
        Criba = {}
        i = 0
        for perfil in perfiles:
                Totales.append("{}. {}".format(i, perfil[0][0]))    # para prevenir la posibilidad de que coincidan las claves, anteponemos
                                                                    # un indice para conseguir la unión disjunta (de otra forma lo sobreescribiríamos)
                Criba["{}. {}".format(i, perfil[0][0])] = perfil[1][perfil[0][0]]
                i += 1
        return [Totales, Criba]
    else:
        return [['cero'], {'cero': [0]*24}]