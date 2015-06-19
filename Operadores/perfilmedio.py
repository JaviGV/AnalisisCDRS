def perfilmedio(*perfiles):
    # Construye el perfil medio (de la forma natural, como la media aritmetica componente a componente) de los perfiles proporcionados;
    #    restringuido a que todos los perfiles correspondan al mismo tipo de operación (en caso contrario devuelve False). Si el 
    #    conjunto de perfiles proporcionado es vacío retorna un perfil por horas (24-dimensional) nulo
    # Imput:     perfiles _ un numero indefinido de perfiles (con estructura tipo desglose: como genera 'analisisphpc(.)')
    #
    # Invocación típica:
    #                    dglcallsMieMed = perfilmedio(dglcalls141217, dglcalls141210, dglcalls141126, dglcalls150114)

    # CÓDIGO
    if perfiles:
        metodo = perfiles[0][0][0][0]
        size = len(perfiles[0][1][perfiles[0][0][0]])
        SxE = [(metodo, 'med')]
        Criba = {(metodo, 'med'): [0]*size}
        for perfil in perfiles:
            if perfil[0][0][0] == metodo and len(perfil[1][perfil[0][0]]) == size:
                Criba[(metodo, 'med')] = [Criba[(metodo, 'med')][i]+perfil[1][perfil[0][0]][i] for i in range(0, size)]
                for n in perfil[0][1:]:
                    if n not in SxE:
                        SxE.append(n)
                        Criba[n] = perfil[1][n]
                    else:
                        Criba[n] = [Criba[n][i]+perfil[1][n][i] for i in range(0, size)]
            else:
                return False
        m = len(perfiles)
        for k in Criba.keys():
            Criba[k] = [Criba[k][i]/m for i in range(0, size)]
        return [SxE, Criba]
    else:
        return [['cero'], {'cero': [0]*24}]
