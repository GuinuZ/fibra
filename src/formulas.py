#

def primeira_pureza(caldo_pol,caldo_brix):
    resultado = 100*caldo_pol/caldo_brix

    return resultado


def pol_bagaco(leitura_pol_bagaco,umidade_bagaco,pureza_caldo):
    pol = leitura_pol_bagaco*52*(1000+umidade_bagaco)/(20000-leitura_pol_bagaco*52*100/pureza_caldo)

    return pol


def brix_bagaco(pol,pureza):
    brix = 100 * pol/pureza

    return brix

def fibra(bagaco_umidade,bagaco_brix):
    fibra = 100 - bagaco_umidade - bagaco_brix

    return fibra


def analises(pol_caldo,brix_caldo,leitura_pol_bagaco,bagaco_umidade):

    analise = []

    pureza = primeira_pureza(pol_caldo,brix_caldo)
    analise.append(pureza)
    p_bagaco = pol_bagaco(leitura_pol_bagaco,bagaco_umidade,pureza)
    analise.append(p_bagaco)
    b_bagaco = brix_bagaco(p_bagaco,pureza)
    analise.append(b_bagaco)
    v_fibra= fibra(bagaco_umidade, b_bagaco)
    analise.append(v_fibra)
    analise.append(bagaco_umidade)

    resultados = [ round(value, 2) for value in analise]

    return resultados

