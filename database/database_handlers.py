from settings import cursor
import asyncpg


async def insert_into_table(name, nickname):
    async with cursor.acquire() as conn:
        command = """INSERT INTO users (first_name, nick_name) VALUES ($1,$2) RETURNING id"""
        args = (name, nickname)
        record_id = await conn.execute(command, *args)
        return tuple(record_id)


async def select_from_table():
    command = """SELECT * FROM users WHERE nick_name = $1"""
    record_id = tuple(await cursor.fetchrow(command, 'Orel'))
    return record_id


async def update_table():
    async with cursor.acquire() as conn:
        await conn.execute('UPDATE users SET nick_name=$2 WHERE first_name=$1',
                           'Kolumb', 'Researcher')
    return True


async def delete_from_table():
    async with cursor.acquire() as conn:
        await conn.execute('DELETE FROM users *')
    return True


async def drop_id_key():
    async with cursor.acquire() as conn:
        await conn.execute('ALTER SEQUENCE users_id_seq RESTART WITH 1')
    return True