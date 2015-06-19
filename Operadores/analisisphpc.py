# Ejemplo registro CALLS
#    380510028|34794006|380510028|55117523|1|LDN|20141231|00:00:42|10|8-TELEFONICA GUATEMALA|11-SERCOM (PCS DIGITAL)|||012940007517080|NOROAMI
# Ejemplo registro SMS
#    52816504|54040001|1|20141231|00:00:52|8-TELEFONICA GUATEMALA|8-TELEFONICA GUATEMALA||380420283|NOROAMI
# Ejemplo registro MMS
#    34630867|34630867|2|20141231|12:27:51|846-TELEFONICA GUATEMALA|846-TELEFONICA GUATEMALA|||


def analisisphpc(f, **opt):
    # Para la lectura de un archivo cdrs y el desglose de sus registros por horas y por clientes de salida y entrada
    # Preparado para recibir como imput el nombre del archivo; tipicamente '/ruta/tipooperacionaaaammdd.dat'
    #    siendo tipooperacion in {calls, sms, mms}
    # Devuelve [SxE, criba], donde:
    #    SxE _ una lista con todos los pares (clienteSalida, clienteEntrada) (tuplas), y cuya primera entrada corresponde al total del día
    #    criba _ un diccionario relacionando cada elemento en SxE con su vector operaciones/hora (24 dimensional) asociado
    # NOTA: a este tipo de estructura de salida la llamaremos en adelante tipo desglose
    #
    # Invocación típica:
    #                    dglcalls141231 = analisisphpc('/disk0/home/bjgv/cdrs/calls20141231.dat')
    # Admite generalización a desglose por minuto, por intervalo de 5min, 10min, 15min...
    #                    dglcalls141231 = analisisphpc('/disk0/home/bjgv/cdrs/calls20141231.dat', tm = 5)
    #
    # Opciones:    tm::integer _ especifica subintervalo de tiempo
    #              sw::boolean _ escritura de los resultados por pantalla

    #CÓDIGO
    if 'tm' not in opt:
        frac = 60
    elif opt['tm'] in {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}:
        frac = opt['tm']
    else:
        return False

    loc = f.split('/')[-1].split('.')[0]        # nos quedamos con el nombre del archivo, sin su extensión 
    metodo = loc[:-8]                           # '/ruta/tipooperacionaaaammdd.dat' --> 'tipooperacionaaaammdd'  --> 'tipooperacion' 
    fecha = loc[-8:]                            #                                                                --> 'aaaammdd'

    SxE = [('TotalOP'.replace('OP', metodo), fecha)]        # Primera entrada en SxE = (total, día)
    horas = [0]*(24*60/frac)                                # Vector 24-dimensional (si frac=1) tipo; una posición por intervalo temporal
    criba = {('TotalOP'.replace('OP', metodo), fecha): horas}
    if metodo in {'sms', 'mms'}:                    #SMS&MMS
        for g in open(f):
            l = g.split('|')               #registro típico: ___[...]___|hh:mm:ss|clienteSalida|clienteEntrada|___[...]___  
            if (l[5], l[6]) not in SxE:    #                                [4]        [5]            [6]
                SxE.append((l[5], l[6]))
                criba[(l[5], l[6])] = [0]*(24*60/frac)
            h = l[4].split(':')
            h = int(h[0])*60/frac + int(h[1])/frac
            horas[h] += 1
            criba[(l[5], l[6])][h] += 1
    elif metodo == 'calls':                         #CALLS
        for g in open(f):
            l = g.split('|')               #registro típico: ___[...]___|hh:mm:ss|____|clienteSalida|clienteEntrada|___[...]___   
            if (l[9], l[10]) not in SxE:   #                               [7]              [9]           [10]
                SxE.append((l[9], l[10]))
                criba[(l[9], l[10])] = [0]*(24*60/frac)
            h = l[7].split(':')
            h = int(h[0])*60/frac + int(h[1])/frac
            horas[h] += 1
            criba[(l[9], l[10])][h] += 1
    else:
        return False
    
    if 'sw' in opt:
        if opt['sw']:
            for d in SxE:
                print "{}     :     {}".format(d, criba[d])

    return [SxE, criba]
