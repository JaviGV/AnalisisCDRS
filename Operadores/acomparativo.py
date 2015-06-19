def acomparativo(pp, pm, pan=False):
    # Construye el perfil diferencia entre dos dados (tipicamente, un perfil particular y un perfil medio previamente generado por el usuario)
    # Si se explicita "pan=True", se limita a construir ciegamente la diferencia de los subperfilesTotal; en otro caso
    #    construye el perfil diferencia completo (desglosado), bajo la restricción de tratarse de registros del mismo 
    #    tipo de operación (en caso contrario devuelve False)
    # Imput:     pp, pm _ perfilparticular, perfilmedio (ambos con estructura tipo desglose: como genera 'analisisphpc(.)')
    #            pan::boolean _ (por defecto False) decide la forma de proceder del programa:
    #                           False = genera perfil diferencia completo (desglosado)
    #                           True = genera únicamente el perfil Total de diferencia
    #
    # Invocación típica:
    #                    signcallsNvieja = acomparativo(dglcalls141231, dglcallsMieMed)
    #                    signsmspcallsNvieja = acomparativo(dglsmspcallsNvieja, dglsmspcallsMieMed, pan=True)
    #
    # NOTA: Observese el carácter antisimétrico de ambos parámetros (pp, pm) en el resultado (pp-pm)

    # CÓDIGO
    if pan:
        size = len(pp[1][pp[0][0]])
        c = [pp[1][pp[0][0]][i] - pm[1][pm[0][0]][i] for i in range(0, size)]
        return [[(pp[0][0][0], '{}dif'.format(pp[0][0][1]))], {(pp[0][0][0], '{}dif'.format(pp[0][0][1])): c}]

    metodo = pm[0][0][0]        # comprobar mismo tipo sms/calls/mms
    size = len(pp[1][pp[0][0]])
    if pp[0][0][0] == metodo:
        Criba = {(metodo, '{}dif'.format(pp[0][0][1])): [pp[1][pp[0][0]][i]-pm[1][pm[0][0]][i] for i in range(0, size)]} 
        for k in pp[0][1:]:                       # subperfiles del desglose en pp
            Criba[k] = pp[1][k]
        for k in set(pm[0][1:])-set(pp[0][1:]):   # subperfiles no tratados en pp que estén presentes en pm
            Criba[k] = [0]*size
        for k in pm[0][1:]:                       # diferencia 
            Criba[k] = [Criba[k][i]-pm[1][k][i] for i in range(0, size)]
        SxE = Criba.keys()   # cuidado no ordenado!!!! Para ser consistentes con el formato de desgloses, colocamos el indice del subperfilTotal en primer lugar
        SxE.insert(0, SxE.pop(SxE.index((metodo, '{}dif'.format(pp[0][0][1])))))
        return [SxE, Criba]
    else:
        return False