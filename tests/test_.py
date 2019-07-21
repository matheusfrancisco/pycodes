# Matheus Francisco Batista Machado
# 1. Nota será igual a soma da multiplicação dos pesos pelos seus atributos
# 2. Caso o candidato tenha escrito mais de 10 artigos, então o peso de artigo sobe para 2
# 3. Caso o candidato zere em algum atributo então a nota final dele será 0
# 
# Pesos:
# xp: 5
# cursos: 2
# artigos: 1

# ranking.py
def calcular_pesos(candidato):
  pesos ={'xp':5, 'cursos':2, 'artigos':1}
  
  if candidato.get('artigos') > 10:
    pesos['artigos'] = 2
  
  return pesos
	

def calcula_nota(candidato):
  #return 8
  pesos = calcular_pesos(candidato)
  nota = 0
  for i in candidato:
    if candidato[atributo] == 0:
    	return 0
    nota += pesos[atributo] * candidato[atributo]
      
	return nota

# test_ranking.py
candidato_base = {
  'xp': 1,
  'cursos': 1,
  'artigos': 1
}


def test_deve_retornar_8_quando_todos_atributos_forem_1():
  assert calcula_nota(candidato_base) == 8

def test_peso_de_artigos_deve_ser_dois_caso_tenhas_mais_de_10_artigos():
  candidato = dict(candidato_base)
  candidato['artigos'] =11
  # candidato.update({'artigos': 11})
  assert calcula_nota(candidato) == 29 

def test_candidato_tenha_algum_atributo_zero():
  candidato = dict(candidato_base)
  candidato['xp'] = 0
  assert calculo_nota(candidato) == 0
