import asyncpg
import asyncio

async def connect_db():
    try:
        dsn = "postgresql://dimar:huinux@10.0.2.15:5432/mydatabase"
        conn = await asyncpg.connect(dsn)
        print("✅ success")
        await conn.close()
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")

asyncio.run(connect_db())