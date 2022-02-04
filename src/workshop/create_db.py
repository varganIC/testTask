import psycopg2
from .database import DB_NAME, DB_USER_NAME, DB_PASSWORD, DB_HOST


class ConectionDB:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER_NAME, password=DB_PASSWORD, host=DB_HOST)
    cursor = conn.cursor()

    sql = 'TRUNCATE TABLE car_model CASCADE'
    cursor.execute(sql)
    conn.commit()

    sql = 'INSERT INTO car_model (id, brand) VALUES (%s, %s)'
    brand = [(1, 'bmw',), (2, 'mercedes',), (3, 'kia',)]
    cursor.executemany(sql, brand)
    conn.commit()

    sql = '''INSERT INTO car (driver, number, year_release, color, speed, description, owner_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    car = [
        ('yri', 234, '2020-02-10', 'blue', 340, 'some description', 1),
        ('garik', 954, '2001-02-15', 'black', 140, 'some description', 1),
        ('igor', 100, '1998-05-10', 'black', 200, 'some description', 1),
        ('vlad', 202, '2005-03-30', 'green', 90, 'some description', 2),
        ('alex', 101, '2021-06-10', 'blue', 300, 'some description', 3),
        ('misha', 201, '2018-06-20', 'red', 250, 'some description', 1),
        ('olga', 301, '2017-02-17', 'grey', 240, 'some description', 2),
        ('katy', 401, '2011-09-11', 'green', 160, 'some description', 3),
        ('philip', 501, '2012-01-19', 'grey', 225, 'some description', 1),
        ('andrey', 707, '2022-01-12', 'black', 210, 'some description', 2),

    ]
    cursor.executemany(sql, car)
    conn.commit()
    cursor.close()


