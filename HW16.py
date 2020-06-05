import sqlite3


conn = sqlite3.connect('tabl.db')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты

with conn:
    cur = conn.cursor()
    # создаем таблицы
    cur.execute('''CREATE TABLE  competition
                (competition_id INTEGER PRIMARY KEY,
                competition_name TEXT,
                world_record INTEGER,
                set_date DATE)''')
    cur.execute("INSERT INTO competition VALUES(1, 'Hockey', 12, 2019-12-23)")
    cur.execute("INSERT INTO competition VALUES(2, 'Basketball', 10, 1995-12-23)")
    cur.execute("INSERT INTO competition VALUES(3, 'Boxing', 5, 1998-10-14)")

    cur.execute('''CREATE TABLE  sportsman
                    (sportsman_id INTEGER PRIMARY KEY,
                    sportsman_name TEXT,
                    rank INTEGER,
                    year_of_birth INTEGER,
                    personal_record INTEGER,
                    country text)''')
    cur.execute("INSERT INTO sportsman VALUES(1, 'Арсений Попов', 5, 1980, 4, 'Russia')")
    cur.execute("INSERT INTO sportsman VALUES(2, 'Константин Евдокимов', 3, 1980, 5, 'Russia')")
    cur.execute("INSERT INTO sportsman VALUES(3, 'Аарон Тейлор', 4, 1965, 4, 'USA')")

    cur.execute('''CREATE TABLE  resulted
                    (competition_id INTEGER REFERENCES competition(competition_id),
                    sportsman_id INTEGER REFERENCES sportsman(sportsman_id),
                    resulte INTEGER,
                    city TEXT,
                    hold_date INTEGER )''')
    cur.execute("INSERT INTO resulted VALUES(1, 1, 3, 'Los Angeles', 2019-06-23)")
    cur.execute("INSERT INTO resulted VALUES(3, 2, 4, 'Los Angeles', 2018-06-23)")
    cur.execute("INSERT INTO resulted VALUES(2, 3, 6, 'Los Angeles', 2017-06-23)")
    cur.execute("INSERT INTO resulted VALUES(2, 3, 10, 'Москва', 2017-06-23)")
    # получаем список таблиц
    cur.execute('SELECT name from sqlite_master where type= "table"')
    print(cur.fetchall())



# получаем данные из таблицы sportsman
print("Данные о спортсменах:")
sql = "SELECT * FROM sportsman"
cur.execute(sql)

# наименование и мировые результаты
print("Наименование и мировые результаты:")
cur.execute("SELECT competition_name, world_record FROM competition")

# получаем имена спортсменов, родившихся в 1980году из таблицы sportsman
print("Имена спортсменов, которые родились в 1980 году:")
sql = "SELECT sportsman_name FROM sportsman WHERE year_of_birth=1980"
cur.execute(sql)

# получаем результаты по всем соревнованиям,
# установленные 12-05-2010 или 15-05-2010
print("Результаты по всем соревнованиям, установленные 2019-06-23 или 2017-06-23:")
sql = "SELECT competition_id, resulte FROM resulted WHERE hold_date=2019-06-23 or hold_date=2017-06-23"
cur.execute(sql)

# получаем дату проведения всех соревнований,
# проводившихся в Москве и полученные на них результаты равны 10 секунд.n
print("Даты проведения всех соревнований, "
      "проводившихся в Москве и полученные на них результаты равны 10 секунд:")
sql = "SELECT hold_date FROM resulted WHERE city='Москва' and resulte=10"
cur.execute(sql)

# получаем имена спортсменов, у которых персональный рекорд менее 25
print("Имена спортсменов, у которых персональный рекорд менее 25:")
sql = "SELECT sportsman_name FROM sportsman WHERE personal_record<10"
cur.execute(sql)

print(cur.fetchall())
