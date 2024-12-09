import asyncio
import aiosqlite

async def async_fetch_users(database):
    """Fetch all users from the database."""
    async with aiosqlite.connect(database) as connection:
        async with connection.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
            print("All Users:")
            for row in results:
                print(row)

async def async_fetch_older_users(database):
    """Fetch users older than 40 from the database."""
    async with aiosqlite.connect(database) as connection:
        async with connection.execute("SELECT * FROM users WHERE age > 40") as cursor:
            results = await cursor.fetchall()
            print("Users Older Than 40:")
            for row in results:
                print(row)

async def fetch_concurrently():
    """Run both queries concurrently."""
    database = "user_info.db"  
    await asyncio.gather(
        async_fetch_users(database),
        async_fetch_older_users(database)
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())

