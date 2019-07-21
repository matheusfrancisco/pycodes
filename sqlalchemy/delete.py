from sqlalchemy import delete
from core import user_table, engine

conn = engine.connect()

d = delete(user_table).where(user_table.c.nome == 'xico')

result = conn.execute(d)


