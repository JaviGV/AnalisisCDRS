def pintardesglose(c):
    # Pintar_ general. Dibuja un mapa de los gráficos que sirven al análisis; fundamentalmente tres:
    #     (a) Representación fiel
    #     (b) Escalado por el número total de llamadas (norm1)
    #     (c) Escalado en función al número máximo de llamadas por hora (normmáx)
    # Imput:     c _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    # Output:     salida gráfica tipo 0 _ mapa de gráficos asociados al perfil proporcionado
    #    -------------------------
    #    --          1          --     Nivel (a): tipo1
    #    -------------------------
    #    -   2   -   3   -   4   -     Nivel (b): tipo2 (todos los perfiles), tipo3 (todos, transparencia proporcional al peso (n1)),
    #    -------------------------                tipo4 (perfiles con más de 5000 llamadas totales)
    #    -   5   -   6   -   7   -     Nivel (c): tipo5 (todos los perfiles), tipo4 (todos, transparencia proporcional al peso (nmáx)),
    #    -------------------------                tipo4 (perfiles con más de 1000 llamadas en alguna hora)

    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
            '17', '18', '19', '20', '21', '22', '23', '24']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    
    fig = plt.figure(figsize=(18, 8), dpi=80)

    plt.subplot(2, 1, 1)
    plt.plot(xx, c[1][c[0][0]], 'o-', linewidth=2.5, color='blue', label=c[0][0])
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)
    for k in (set(c[0])-{c[0][0]}):
        plt.plot(xx, c[1][k], '-', linewidth=1.0, color='black', label=k)
    plt.xlabel('Hora')
    plt.ylabel('# operaciones')
    plt.title(u'OP, fraccionado por horas'.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))))
    
    plt.subplot(4, 3, 7)
    peson1 = {i: 0 for i in c[0]}
    peson1[c[0][0]] = norma1(c[1][c[0][0]])
    yy = [i/peson1[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, '+-', linewidth=1.5, color='blue')
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([rr[6*i]-0.5 for i in range(5)], [reloj[6*i] for i in range(5)])
    for k in set(c[0])-{c[0][0]}:
        peson1[k] = norma1(c[1][k])
        yy = [i/peson1[k] for i in c[1][k]]
        plt.plot(xx, yy, '-', linewidth=0.5, color='black')
    plt.title(u'normado: norma_1')
    
    plt.subplot(4, 3, 10)
    pesonm = {i: 0 for i in c[0]}
    pesonm[c[0][0]] = normmax(c[1][c[0][0]])
    yy = [i/pesonm[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, '+-', linewidth=1.5, color='blue')
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([rr[6*i]-0.5 for i in range(5)], [reloj[6*i] for i in range(5)])
    for k in set(c[0])-{c[0][0]}:
        pesonm[k] = normmax(c[1][k])
        yy = [i/pesonm[k] for i in c[1][k]]
        plt.plot(xx, yy, '-', linewidth=0.5, color='black')
    plt.title(u'normado: norma_max')
    
    plt.subplot(4, 3, 8)
    yy = [i/peson1[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, '+-', linewidth=1.5, color='blue')
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([rr[6*i]-0.5 for i in range(5)], [reloj[6*i] for i in range(5)])
    s1 = norma1([peson1[k] for k in set(c[0])-{c[0][0]}])
    luz1 = {k: peson1[k]/s1 for k in set(c[0])-{c[0][0]}}
    for k in set(c[0])-{c[0][0]}:
        yy = [i/peson1[k] for i in c[1][k]]
        plt.plot(xx, yy, '-', linewidth=0.5, color='black', alpha=luz1[k])
    plt.title(u'proporcional peso_n1')
    
    plt.subplot(4, 3, 11)
    yy = [i/pesonm[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, '+-', linewidth=1.5, color='blue')
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([rr[6*i]-0.5 for i in range(5)], [reloj[6*i] for i in range(5)])
    sm = normmax([pesonm[k] for k in set(c[0])-{c[0][0]}])
    luzm = {k: pesonm[k]/sm for k in set(c[0])-{c[0][0]}}
    for k in set(c[0])-{c[0][0]}:
        yy = [i/pesonm[k] for i in c[1][k]]
        plt.plot(xx, yy, '-', linewidth=0.5, color='black', alpha=luzm[k])
    plt.title(u'proporcional peso_nmax')
    
    plt.subplot(4, 3, 9)
    cota = 5000
    yy = [i/peson1[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, '+-', linewidth=1.5, color='blue')
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([rr[6*i]-0.5 for i in range(5)], [reloj[6*i] for i in range(5)])
    for k in [k for k in set(c[0])-{c[0][0]} if peson1[k] >= cota]:
        yy = [i/peson1[k] for i in c[1][k]]
        plt.plot(xx, yy, '-', linewidth=0.5, color='black')
    plt.title(u'n1, > %s' % cota)
    
    plt.subplot(4, 3, 12)
    cota = 1000
    yy = [i/pesonm[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, '+-', linewidth=1.5, color='blue')
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([rr[6*i]-0.5 for i in range(5)], [reloj[6*i] for i in range(5)])
    for k in [k for k in set(c[0])-{c[0][0]} if pesonm[k] >= cota]:
        yy = [i/pesonm[k] for i in c[1][k]]
        plt.plot(xx, yy, '-', linewidth=0.5, color='black')
    plt.title(u'nmax, > %s' % cota)
    
    plt.tight_layout()


def pintar1(c):
    # Pintar_ tipo1. Representación fiel (sin escalar) del perfil recibido
    #
    # Imput:     c _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    # Output:     salida gráfica tipo (a)1 

    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]))

    fig = plt.figure(figsize=(18, 8), dpi=80)

    plt.plot(xx, c[1][c[0][0]], 'o-', linewidth=2.5, color='blue', label=c[0][0])
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj) 
    for k in (set(c[0])-{c[0][0]}):
        plt.plot(xx, c[1][k], '+-', linewidth=1.0, color=paleta.next(), label=k)
    plt.legend(loc=2, fontsize=8)
    plt.xlabel('Hora')
    plt.ylabel('# operaciones')
    plt.title(u'OP, fraccionado por horas'.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))))


def pintar2(c):
    # Pintar_ tipo2. Representación del perfil recibido normando cada curva de acuerdo a su número de llamadas totales (norma1).
    #
    # Imput:     c _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    # Output:     salida gráfica tipo (b)2

    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', 
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]))
    
    fig = plt.figure(figsize=(18, 8), dpi=80)
    
    peson1 = {i: 0 for i in c[0]}
    for k in c[0]:
        peson1[k] = norma1(c[1][k])
    yy = [i/peson1[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, 'o-', linewidth=2.5, color='blue', label=c[0][0])
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)
    for k in set(c[0])-{c[0][0]}:
        yy = [i/peson1[k] for i in c[1][k]]
        plt.plot(xx, yy, '+-', linewidth=1.0, color=paleta.next(), label=k)
    plt.legend(loc=2, fontsize=9)
    plt.xlabel('Hora')
    plt.ylabel(u'Proporción de operaciones sobre el total del operador')
    plt.title(u'OP, fraccionado por horas; escalado según norma \
uno'.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))))


def pintar3(c):
    # Pintar_ tipo3. Representación del perfil recibido normando cada curva de acuerdo a su norma1 (número total de llamadas).
    #                   Cada curva se perfila con un nivel de trasnparencia proporcionado a su peso en dicha norma (i.e. a 
    #                   la cantidad de llamadas en el perfil respecto al perfil total)
    #
    # Imput:     c _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    # Output:     salida gráfica tipo (b)3 

    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]))
    
    fig = plt.figure(figsize=(18, 8), dpi=80)
    
    peson1 = {i: 0 for i in c[0]}
    for k in c[0]:
        peson1[k] = norma1(c[1][k])
    yy = [i/peson1[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, 'o-', linewidth=2.5, color='blue', label=c[0][0])
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)
    
    s1 = norma1([peson1[k] for k in set(c[0])-{c[0][0]}])
    luz1 = {k: peson1[k]/s1 for k in set(c[0])-{c[0][0]}}
    for k in [k for k in set(c[0])-{c[0][0]} if luz1[k] < 0.07]:
        luz1[k] = 0.07
    
    for k in set(c[0])-{c[0][0]}:
        yy = [i/peson1[k] for i in c[1][k]]
        plt.plot(xx, yy, '+-', linewidth=1.0, color=paleta.next(), alpha=luz1[k], label=k)
    plt.legend(loc=2, fontsize=9)
    plt.xlabel('Hora')
    plt.ylabel(u'Proporción de operaciones sobre el total del operador')
    plt.title(u'OP, fraccionado por horas; e_N1 (intensidad proporcional al peso \
del operador para la norma uno)'.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))))


def pintar5(c):
    # Pintar_ tipo5. Representación del perfil recibido normando cada curva en función a su número máximo de llamadas en
    #                   alguna hora (normamáx).
    #
    # Imput:     c _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    # Output:     salida gráfica tipo (c)5
    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]))
    
    fig = plt.figure(figsize=(18, 8), dpi=80)
    
    pesonm = {i: 0 for i in c[0]}
    for k in c[0]:
        pesonm[k] = normmax(c[1][k])
    yy = [i/pesonm[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, 'o-', linewidth=2.5, color='blue', label=c[0][0])
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)
    for k in set(c[0])-{c[0][0]}:
        yy = [i/pesonm[k] for i in c[1][k]]
        plt.plot(xx, yy, '+-', linewidth=1.0, color=paleta.next(), label=k)
    plt.legend(loc=2, fontsize=9)
    plt.xlabel('Hora')
    plt.ylabel(u'Proporción de operaciones sobre la máxima por hora del operador')
    plt.title(u'SMS, fraccionado por horas; ')
    plt.title(u'OP, fraccionado por horas; escalado según norma del \
máximo'.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))))


def pintar6(c):
    # Pintar_ tipo6. Representación del perfil recibido normando cada curva por normamáx (número máximo de llamadas en
    #                   una hora). Cada curva se perfila con un nivel de trasnparencia proporcionado a su peso para 
    #                   dicha norma (i.e. máxporhora del perfil respecto al máxporhora del perfil total)
    #
    # Imput:     c _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    # Output:     salida gráfica tipo (c)6

    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]))
    
    fig = plt.figure(figsize=(18, 8), dpi=80)
    
    pesonm = {i: 0 for i in c[0]}
    for k in c[0]:
        pesonm[k] = normmax(c[1][k])
    yy = [i/pesonm[c[0][0]] for i in c[1][c[0][0]]]
    plt.plot(xx, yy, 'o-', linewidth=2.5, color='blue', label=c[0][0])
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)
    
    sm = normmax([pesonm[k] for k in set(c[0])-{c[0][0]}])
    luzm = {k: pesonm[k]/sm for k in set(c[0])-{c[0][0]}}
    for k in [k for k in set(c[0])-{c[0][0]} if luzm[k] < 0.07]:
        luzm[k] = 0.07

    for k in set(c[0])-{c[0][0]}:
        yy = [i/pesonm[k] for i in c[1][k]]
        plt.plot(xx, yy, '+-', linewidth=1.0, color=paleta.next(), alpha=luzm[k], label=k)
    plt.legend(loc=2, fontsize=9)
    plt.xlabel('Hora')
    plt.ylabel(u'Proporción de operaciones sobre la máxima por hora del operador')
    plt.title(u'SMS, fraccionado por horas; ')
    plt.title(u'OP, fraccionado por horas; e_NM (intensidad proporcional al peso del operador para \
la norma del máximo)'.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))))


def pintar4(c, cota=5000):
    # Pintar_ tipo3. Representación (de un cribado) del perfil recibido normando cada curva de acuerdo a su norma1 
    #                   (número total de llamadas). Sólo se grafican aquellos perfiles con norma1 >= cota
    #
    # Imput:     c::dgl _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    #            cota::"numeric" _ establece el número total de llamadas mínimo para que un perfil se represente
    #                      (5000 salvo que se especifique otra cosa). Admite valores "absolutos" (enteros >=1) 
    #                      o "relativos" (que se entenderán como proporción del total); estos últimos puden ser 
    #                      especificados como coeficiente (0 <= nn < 1) o como string ('nn%' = 'nnp').
    # Output:     salida gráfica tipo (b)3
    # 
    # Invocación típica:
    #                    pintar4(dglcalls141231)     (equiv. pintar4(dglcalls141231, cota=5000))
    #                    pintar4(dglcalls141231, 0.012)     (equiv. pintar4(dglcalls141231, cota='1.2%'))
    
    if type(c) == tuple and len(c) == 2:
        cota = c[1]
        c = c[0]
    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]))           # POSIBLEMEJORA: crear paleta en función del número real de curvas pintadas
                                            # POSIBLEMEJORA2: crear paleta como diccionario para mantener colores fijos en cada par SxE
                                            #                    ¿paleta::dic global, y se van añadiendo colores que no estén?
    
    fig = plt.figure(figsize=(18, 8), dpi=80)
    
    peson1 = {i: 0 for i in c[0]}
    for k in c[0]:
        peson1[k] = norma1(c[1][k])
    yy = [i/peson1[c[0][0]] for i in c[1][c[0][0]]]
    if peson1[c[0][0]] > 1000:
        leyend = u"{}    :   {:,.0f}k  (total)".format(c[0][0], peson1[c[0][0]]/1000)
    else:
        leyend = u"{}    :   {:,.0f}  (total)".format(c[0][0], peson1[c[0][0]])
    plt.plot(xx, yy, 'o-', linewidth=2.5, color='blue', label=leyend)
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)
    
    if re.search('p|%', str(cota)):         # permite entrar cota como string(numporcent[p%])
        cota = float(str(cota)[:-1])
        cota = int(peson1[c[0][0]]*cota/100)
    elif cota < 1:                           # en otro caso (presuponemos numérico), se entiende 0.xx como porcentaje (xx/100)
        cota = int(peson1[c[0][0]]*cota)
    
    for k in [k for k in set(c[0])-{c[0][0]} if peson1[k] >= cota]:
        yy = [i/peson1[k] for i in c[1][k]]
        if peson1[k] > 1000:
            leyend = u"{}    :   {:,.0f}k".format(k, peson1[k]/1000)
        else:
            leyend = u"{}    :   {:,.0f}".format(k, peson1[k])
        plt.plot(xx, yy, '+-', linewidth=1.0, color=paleta.next(), label=leyend)
    plt.legend(loc=2, fontsize=9)
    plt.xlabel('Hora')
    plt.ylabel(u'Proporción de operaciones sobre el total del operador')
    plt.title(u'SMS, fraccionado por horas; ')
    titulo = u'OP, fraccionado por horas; e_N1 (operadores con más de %s operaciones)' % cota
    titulo = titulo.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8])))
    plt.title(titulo)


def pintar4e(c, *mini):
    # pintar4 extendido. Generaliza y relaja la invocación de pintar4
    # Invocación típica:
    #                    pintar4e(dglcalls141231, 5000, 0.12, 0.012)
    
    if type(c) == tuple and len(c) >= 2:           # pintar4'((dgl, m1, m2)) = pintar4'(dgl, m1, m2) (para estúpidos)
        mini = c[1:]
        c = c[0]
    
    if type(mini) == tuple and len(mini) == 1 and type(mini[0]) == tuple:
        mini = [k for k in mini[0]]                # pintar4'(dgl, ((m1, m2))) = pintar4'(dgl, m1, m2)
    if len(mini) != 0:                             # pintar4'(dgl, m1, m2, ...) = pintar4(dgl, m1); pintar4(dgl,m2); ...
        for k in [k for k in mini]:                
            pintar4(c, k)
    else:
        pintar4(c)


def pintar7(c, cota=1000):
    # Pintar_ tipo7. Representación (de un cribado) del perfil recibido normando cada curva por normamáx (número máximo 
    #                   de llamadas en una hora). Sólo se grafican aquellos perfiles con normamáx >= cota
    #
    # Imput:     c::dgl _ perfil con estructura tipo desglose (como la generada por 'analisisphpc(.)')
    #            cota::"numeric" _ establece el valor mínimo del máximo de operaciones por hora del perfil para que
    #                      éste se represente (1000 salvo que se especifique otra cosa). Admite valores "absolutos" 
    #                      (enteros >=1) o "relativos" (que se entenderán como proporción del máximo por horas del
    #                      perfil total), especificados como coeficiente (0 <= nn < 1) o como string ('nn%' = 'nnp').
    # Output:     salida gráfica tipo (c)7
    # 
    # Invocación típica:
    #                    pintar7(dglcalls141231)     (equiv. pintar7(dglcalls141231, 5000))
    #                    pintar7(dglcalls141231, cota=0.012)     (equiv. pintar7(dglcalls141231, '1.2%'))

    if type(c) == tuple and len(c) == 2:
        cota = c[1]
        c = c[0]
    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]))           # POSIBLEMEJORA: crear paleta en función del número real de curvas pintadas
                                            # POSIBLEMEJORA2: crear paleta como diccionario para mantener colores fijos en cada par SxE
                                            #                    ¿paleta::dic global, y se van añadiendo colores que no estén?
    fig = plt.figure(figsize=(18, 8), dpi=80)

    pesonm = {i: 0 for i in c[0]}
    for k in c[0]:
        pesonm[k] = normmax(c[1][k])
    yy = [i/pesonm[c[0][0]] for i in c[1][c[0][0]]]
    if pesonm[c[0][0]] > 1000:
        leyend = u"{}    :   {:,.0f}k  (máx)".format(c[0][0], pesonm[c[0][0]]/1000)
    else:
        leyend = u"{}    :   {:,.0f}  (máx)".format(c[0][0], pesonm[c[0][0]])
    plt.plot(xx, yy, 'o-', linewidth=2.5, color='blue', label=leyend)
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)

    if re.search('p|%', str(cota)):         # permite entrar cota como string(numporcent[p%])
        cota = float(str(cota)[:-1])
        cota = int(pesonm[c[0][0]]*cota/100)
    elif cota < 1:                           # en otro caso (presuponemos numérico), se entiende 0.xx como porcentaje (xx/100)
        cota = int(pesonm[c[0][0]]*cota)

    for k in [k for k in set(c[0])-{c[0][0]} if pesonm[k] >= cota]:
        yy = [i/pesonm[k] for i in c[1][k]]
        if pesonm[k] > 1000:
            leyend = u"{}    :   {:,.0f}k".format(k, pesonm[k]/1000)
        else:
            leyend = u"{}    :   {:,.0f}".format(k, pesonm[k])
        plt.plot(xx, yy, '+-', linewidth=1.0, color=paleta.next(), label=leyend)
    plt.legend(loc=2, fontsize=9)
    plt.xlabel('Hora')
    plt.ylabel(u'Proporción de operaciones sobre la máxima por hora del operador')
    plt.title(u'SMS, fraccionado por horas; ')
    titulo = u'OP, fraccionado por horas; e_NM (operadores con más de %s operaciones en alguna hora)' % cota
    titulo = titulo.replace('OP', ('%s %s-%s-%s' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8])))
    plt.title(titulo)


def pintar7e(c, *mini):
    # pintar7 extendido. Generaliza y relaja la invocación de pintar7
    # Invocación típica:
    #                    pintar7e(dglcalls141231, 5000, 0.12, 0.012)
    
    if type(c) == tuple and len(c) >= 2:           # pintar7'((dgl, m1, m2)) = pintar7'(dgl, m1, m2) (para estúpidos)
        mini = c[1:]
        c = c[0]
    
    if type(mini) == tuple and len(mini) == 1:     # pintar7'(dgl, ((m1, m2))) = pintar7'(dgl, m1, m2)
        mini = [k for k in mini[0]]
    if len(mini) != 0:                             # pintar7'(dgl, m1, m2, ...) = pintar7(dgl, m1); pintar7(dgl,m2); ...
        for k in [k for k in mini]:
            pintar7(c, k)
    else:
        pintar7(c)


def pintar(c, *m):
    # Unifica el grupo de scripts pintar_ asociados con pintardesglose
    # Cada típo de gráfico (0, 1, 2, .., 7) se especifica por su índice
    # Los gráficos tipo4 y tipo7 admiten también sus cotas como segundo argumento
    # OK versión3: adaptados a cualquier tamaño de perfil
    # 
    # Invocaciones típicas:
    #                       pintar(dgl) == pintar(dgl, 0) == pintardesglose(dgl)
    #                       pintar(dgl,1,4,6) == pintar1(dgl); pintar4(dgl); pintar6(dgl)
    #                       pintar(dgl, (4), (7, 0.25)) == pintar4(dgl); pintar7(dgl, 0.25)
    #                       pintar(dgl, 1, (4, 1000, 2000)) == pintar(dgl, 1, (4, 1000), (4, 2000))

    posibles = {0: pintardesglose, 1: pintar1, 2: pintar2, 3: pintar3, 4: pintar4, 5: pintar5, 6: pintar6, 7: pintar7}
    posiblese = {4: pintar4e, 7: pintar7e}

    if len(m) != 0:
        for n in m:
            try:
                posibles[n](c)
            except:
                if type(n) == tuple and len(n) != 0:
                    if len(n) == 1:
                        posibles[n[0]](c)
                    else:
                        posiblese[n[0]](c, n[1:])
                else:
                    print ""
    else:
        pintardesglose(c)