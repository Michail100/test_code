import asyncio
import asyncpg
import logging

db_host = 'localhost'
db_user = 'postgres'
db_password = 'root'
db_name = 'postgres'

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def create_db():
    connection: asyncpg.Connection = await asyncpg.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )

    async def create_table():
        await connection.execute(
                """CREATE TABLE IF NOT EXISTS users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL);"""
            )
    await create_table()
    logging.info('Table has been created')
    await connection.close()


async def create_pool():
    return await asyncpg.create_pool(
        host=db_host,
        user=db_user,
        password=db_password
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
