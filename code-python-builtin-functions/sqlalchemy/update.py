from sqlalchemy import update
from core import user_table, engine


conn = engine.connect()

u = update(user_table).where(user_table.c.nome == 'Fábio')

u = u.values(nome='xico')

result = conn.execute(u)
