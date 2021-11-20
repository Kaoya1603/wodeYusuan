import sqlite3

categories = ['продукты питания',
              'непродовольственные товары',
              'коммунальные платежи',
              'транспорт',
              'питомцы',
              'образование',
              'развлечения',
              'медицина',
              'спорт',
              'хобби']

conn = sqlite3.connect('wode_huafei.db')

with conn:
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS zhonglei(
       id INTEGER PRIMARY KEY,
       title TEXT UNIQUE NOT NULL);
    ''')
    for i in range(len(categories)):
        cur.execute('INSERT INTO zhonglei(title) VALUES(?);', [categories[i]])

    cur.execute('''CREATE TABLE IF NOT EXISTS huafei(
       дата TEXT,
       категория TEXT NOT NULL,
       сумма FLOAT);
    ''')
    conn.commit()
