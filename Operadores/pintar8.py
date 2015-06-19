def pintar8(c, re=True, s=True, labelpp='', labelpm='', leg=False):
    # Opciones:     labelpp::string _ etiqueta perfil particular (el positivo)
    #               labelpm::string _ etiqueta perfil medio (el minus, respecto al que se compara)
    #               s::boolean _ curva suelo/cero (por defecto True)
    #               re::boolean _ rellenado (por defecto True)
    if len(c[0]) != 1:
        return False
    else:
        size = len(c[1][c[0][0]])
        xx = range(size)
        rr = [i*size/24 for i in range(25)]
        reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
                 '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                 '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
        metodo = c[0][0][0][5:]
        fecha = c[0][0][1]
        fig = plt.figure(figsize=(18, 8), dpi=80)
        if s:
            plt.plot(xx, [0]*size, 'o-', linewidth=2.5, color='black')
        plt.xlim(rr[0]-1, rr[24])
        plt.xticks([x-0.5 for x in rr], reloj)
        plt.plot(xx, c[1][c[0][0]], 'o-', linewidth=2.5, color='red', label=c[0][0])
        if leg:
            plt.legend(loc=2, fontsize=8)
        if re:
            plt.fill_between(xx, c[1][c[0][0]], [0]*24, color='blue')
        plt.xlabel('Hora')
        plt.ylabel('# operaciones')
        plt.title(u'%s %s-%s-%s, fraccionado por horas' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))
        fig.text(0.8, 0.8, labelpp)        # Modificar parametros si se requiere cambiar localización
        fig.text(0.8, 0.04, labelpm)
