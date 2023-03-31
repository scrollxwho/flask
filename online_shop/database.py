import sqlite3
connect = sqlite3.connect("store.db")
cursor = connect.cursor()

with open("script.sql", encoding="utf-8") as file:
    cursor.executescript(file.read())


get_sql_request = "INSERT INTO products (name, price, describe) VALUES (?, ?, ?)"

list_products = [
    # ['Lacoste', 2100, 'Рубашка'],
    # ['Adidas', 1500, 'Кроссовки'],
    # ['Nike', 2500, 'Футболка'],
    # ['Puma', 1800, 'Брюки'],
    # ['Calvin Klein', 3000, 'Джинсы'],
    # ['H&M', 700, 'Футболка'],
    # ['Zara', 900, 'Блузка'],
    # ['Levi’s', 2200, 'Шорты'],
    # ['Tommy Hilfiger', 4000, 'Рубашка'],
    # ['Gucci', 9000, 'Кошелек'],
    # ['Prada', 15000, 'Сумка'],
    # ['Chanel', 20000, 'Платье'],
    # ['Armani', 5000, 'Свитер'],
    # ['Hugo Boss', 3500, 'Костюм'],
    # ['Ralph Lauren', 2500, 'Футболка'],
    # ['Zegna', 6000, 'Рубашка'],
    # ['Balenciaga', 12000, 'Кроссовки'],
    # ['C.P Company', 13000, 'Шапка'],
    # ['Burberry', 9000, 'Пальто'],
    # ['Fendi', 14000, 'Сумка'],
    # ['Louis Vuitton', 25000, 'Кошелек'],
    # ['Dior', 19000, 'Сумка'],
    # ['Givenchy', 13000, 'Юбка'],
    # ['Versace', 7500, 'Футболка'],
    # ['GAP', 1200, 'Шорты'],
    # ['Guess', 1800, 'Рубашка'],
    # ['Tom Ford', 10000, 'Пальто'],
    # ['Moncler', 15000, 'Куртка'],
    # ['Mango', 1500, 'Блузка'],
    # ['Massimo Dutti', 1800, 'Свитер'],
    # ['Pull & Bear', 800, 'Футболка'],
    # ['Stradivarius', 1000, 'Кофта'],
    # ['Bershka', 700, 'Джинсы'],
    # ['Oysho', 1000, 'Пижама'],
    # ['Victoria’s Secret', 2000, 'Нижнее белье'],
    # ['Hermes', 12000, 'Шарф'],
    # ['Cartier', 25000, 'Часы'],
    # ['Rolex', 50000, 'Часы'],
    # ['Bulgari', 15000, 'Подвеска'],
    # ['Tiffany & Co', 10000, 'Кольцо'],
    # ['Chopard', 20000, 'Браслет'],
    # ['Piaget', 30000, 'Часы'],
    # ['Harry Winston', 50000, 'Кольцо'],
    # ['Graff', 75000, 'Кольцо'],
    # ['Mikimoto', 20000, 'Жемчуг'],
    # ['Asprey', 15000, 'Футляр для часов'],
    # ['Gucci', 8000, 'Кошелек'],
    # ['Louis Vuitton', 15000, 'Сумка'],
    # ['Prada', 12000, 'Очки'],
    # ['Versace', 10000, 'Ремень']
]


cursor.executemany(get_sql_request, list_products)

# cursor.execute('select * from products where id==(?)', [1])
cursor.execute('select * from products')
get_items = cursor.fetchall()


connect.commit()

for item in get_items:
    print(item)