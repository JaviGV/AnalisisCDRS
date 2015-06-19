def pintar1g(c, n=1, s=False):
    # Opciones:     n::integer _ número de curvas destacadas (por defecto 1)
    #               s::boolean _ curva suelo/cero (por defecto False)
    size = len(c[1][c[0][0]])
    xx = range(size)
    rr = [i*size/24 for i in range(25)]
    reloj = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00']
    metodo = c[0][0][0][5:]
    fecha = c[0][0][1]
    paleta = piccolore(len(c[0]), blue=True)

    fig = plt.figure(figsize=(18, 8), dpi=80)
    if s:
        plt.plot(xx, [0]*size, 'o-', linewidth=2.5, color=paleta.next())
    plt.xlim(rr[0]-1, rr[24])
    plt.xticks([x-0.5 for x in rr], reloj)
    if len(c[0]) < n:
        n = len(c[0])
    for i in range(n):
        plt.plot(xx, c[1][c[0][i]], 'o-', linewidth=2.5, color=paleta.next(), label=c[0][i])
    for k in (set(c[0])-{c[0][i] for i in range(n)}):
        plt.plot(xx, c[1][k], '+-', linewidth=1.0, color=paleta.next(), label=k)
    plt.legend(loc=2, fontsize=8)
    plt.xlabel('Hora')
    plt.ylabel('# operaciones')
    plt.title(u'%s %s-%s-%s, fraccionado por horas' % (metodo.upper(), fecha[0:4], fecha[4:6], fecha[6:8]))
