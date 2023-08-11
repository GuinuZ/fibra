import converter
import json

#valores teste 1.40,1.93,2.94,53.84
valores = []

p_caldo = float(input("Insira a leitura da Pol do Caldo: "))
valores.append(p_caldo)
b_caldo = float(input("Insira a leitura do Brix do Caldo: "))
valores.append(b_caldo)
l_P_bagaco = float(input("Insira a leitura da Pol do Bagaço: "))
valores.append(l_P_bagaco)
b_umidade = float(input("Insira a umidade do bagaço: "))
valores.append(b_umidade)



final = converter.lista_resultados(valores)

json_final = json.dumps(final, indent = 4)

print(json_final)
