CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_PRODUCTS_DETAIL='''
CREATE TABLE IF NOT EXISTS products_details(
id INTEGER PRIMARY KEY AUTOINCREMENT,
PRODUCT_ID INTEGER,
CATEGORY VARCHAR(255),
INFO_PRODUCT TEXT
)'''

INSERT_INTO_PRODUCT_DETAIL='''
INSERT INTO products_details (product_id, category, info_product) VALUES (?,?,?)'''