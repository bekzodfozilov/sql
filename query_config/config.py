from loader import db


def create_tables():
    try:
        db.execute("""create table if not exists filials(id integer primary key ,
name varchar(30),
latitude float,
longitude float,
city varchar(30))
""", commit=True)
        db.execute("""create table if not exists users(id integer primary key , 
user_id varchar(30), 
name varchar(30),
phone varchar(15),
city varchar(20),
language varchar(10))

""", commit=True)
        db.execute("""create table if not exists items(id integer primary key,
kategory varchar(30),
name varchar(30),
info varchar(100),
price int,
photo text)""", commit=True)
        db.execute("""create table if not exists count_items
(
    id      int
        primary key,
    user_id integer
        references users(id),
    count   integer default 1
)""", commit=True)
    except Exception as err:
        print(err)


def get_filial(city):
    try:
        list = []
        fetchall = db.execute(f"select * from filials where city = '{city}'", fetchall=True)
        for i in fetchall:
            l = [i[1], i[2], i[3], i[4]]
            list.append(l)
        return list
    except Exception as err:
        print(err)


def users():
    try:
        list = []
        fetchall = db.execute("select * from users", fetchall=True)
        for i in fetchall:
            l = [i[0], i[1], i[2], i[3], i[4], i[5]]
            list.append(l)
        return list
    except Exception as err:
        print(err)


def insert_user(user_id, name, number, language, city):
    try:
        db.execute(f"""insert into users(user_id, name, phone, language, city)
VALUES('{user_id}', '{name}', '{number}', '{language}', '{city}')""", commit=True)
    except Exception as err:
        print(err)


def cities():
    try:
        list = []
        fetchall = db.execute('select distinct city from filials', fetchall=True)
        for i in fetchall:
            list.append(i[0])
        return list
    except Exception as err:
        print(err)


def update_language(user_id, language):
    try:
        db.execute(f"""update users
        set language = '{language}'
        where user_id = '{user_id}'""", commit=True)
    except Exception as err:
        print(err)


def get_city_user(user_id):
    try:
        city = str()
        fetchone = db.execute(f"select city from users where user_id = '{user_id}'", fetchone=True)
        for i in fetchone:
            city = i
        return city
    except Exception as err:
        print(err)


def update_city(user_id, city):
    try:
        db.execute(f"""update users
        set city = '{city}'
        where user_id = '{user_id}'""", commit=True)
    except Exception as err:
        print(err)


def items():
    try:
        list = []
        fetchall = db.execute('select * from items')
        for i in fetchall:
            list.append([i[0], i[1], i[2], i[3], i[4], i[5]])
        return list
    except Exception as err:
        print(err)


def get_kategory():
    try:
        list = []
        fetchall = db.execute(f'select distinct kategory from items', fetchall=True)
        for i in fetchall:
            for j in i:
                list.append(j)
        print(list)
        return list
    except Exception as err:
        print(err)


def get_item(item_name):
    try:
        return db.execute(f"select * from items where name = '{item_name}'", fetchone=True)
    except Exception as e:
        print(e)


def update_plus_count(user_id):
    try:
        u_id = int()
        fetchone = db.execute(f"select id from users where user_id = '{user_id}'", fetchone=True)
        for i in fetchone:
            u_id = i
        db.execute(f"""update count_items
set count = count + 1
where user_id = {u_id}""", commit=True)
    except Exception as err:
        print(err)


def update_minus_count(user_id):
    try:
        u_id = int()
        fetchone = db.execute(f"select id from users where user_id = '{user_id}'", fetchone=True)
        for i in fetchone:
            u_id = i
        db.execute(f"""update count_items
        set count = count - 1
        where user_id = {u_id}""", commit=True)
    except Exception as err:
        print(err)


def update_count(user_id):
    u_id = int()
    try:
        fetchone = db.execute(f"""select id from users where user_id = '{user_id}'""", fetchone=True)
        for i in fetchone:
            u_id = i
        db.execute(f"""update count_items
set count = 1
where user_id = {u_id}""", commit=True)

    except Exception as err:
        print(err)
