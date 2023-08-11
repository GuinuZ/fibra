import formulas


def lista_resultados(lista):
     resultados = formulas.analises(lista[0],lista[1],lista[2],lista[3])
     schema = {'Pureza': resultados[0], 'Pol': resultados[1], 'Brix': resultados[2], 'Fibra': resultados[3], 'Umidade': resultados[4]}

     return schema


