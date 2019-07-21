from core import user_table, engine

conn = engine.connect()

ins = user_table.insert()


"""new_user = ins.values(nome='Fábio',
                      idade=29,
                      senha='riodejaneiro')
"""

#conn.execute(new_user)

conn.execute(user_table.insert(),[
    {'nome':'marivaldo', 'idade':30, 'senha': 'gatinha_123'},
    {'nome': 'Jean', 'idade':18, 'senha':'ggggg'}
])
