import psycopg2

class Pgadmin:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        
        
    def create_table(self):
        cur = self.con.cursor()
        cur.execute("create table students(studentId serial PRIMARY KEY, name text, age int, email text, address text);")
        self.con.commit()
        self.con.close()

    def insert_data(self):
        name = str(input("Enter name: "))
        age = int(input("Enter age: "))
        email = str(input("Enter email: "))
        address = str(input("Enter address: "))
        cur = self.con.cursor()
        cur.execute(f"insert into students (name, age, email, address) values ('{name}', {age}, '{email}', '{address}');")
        self.con.commit()
        self.con.close()

    def updating_data():
        student_id = input("Enter Student's ID to be updated: ")
        con = psycopg2.connect(dbname="studentdb", user='admin', password='admin123', host='localhost', port='5432')
        cur = con.cursor()
        cur.execute(f"update students set ")
        con.commit()
        con.close()

pjt = Pgadmin('studentdb', 'admin', 'admin123', 'localhost', 5432)
pjt.insert_data()