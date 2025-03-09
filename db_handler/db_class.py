#import asyncio
#import asyncpg
#
#async def connect_db():
#    conn = await asyncpg.connect(
#        host="10.0.2.255",  # Например, 192.168.1.100
#        port=5432,
#        user="dimar",
#        password="huinux",
#        database="mydatabase"
#    )
#    return conn

import asyncpg
import asyncio
import os

class PostgresHandler:
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(self.dsn)

    async def connect_db():
        conn = await asyncpg.connect(
            host="10.0.2.15",
            port=5432,
            user="dimar",
            password="huinux",
            database="mydatabase"
        )
        print("✅ Connected to database")
        await conn.close()

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as conn:
            await conn.execute(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def close(self):
        await self.pool.close()

# Инициализация
pg_db = PostgresHandler(os.getenv("PG_LINK"))

async def main():
    await pg_db.connect()
    await pg_db.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT)")
    await pg_db.execute("INSERT INTO users (name) VALUES ($1)", "Alice")
    users = await pg_db.fetch("SELECT * FROM users")
    print(users)
    await pg_db.close()


asyncio.run(main())