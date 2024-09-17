import sqlite3
from db import  queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAIL)
    db.commit()


async def sql_insert_products(name_product, size, price, product_id, photo):
    cursor.execute(queries.INSERT_PRODUCTS_QUERY, (
        name_product,
        size,
        price,
        product_id,
        photo
    ))
    db.commit()

async def insert_products_detail(productid, category, info_product):
    cursor.execute(queries.INSERT_PRODUCTS_DETAIL, (productid, category, info_product))
    db.commit()