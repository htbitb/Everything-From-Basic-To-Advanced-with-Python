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

    def delete_data(self):
        student_id = input("Enter Student's ID to be deleted: ")
        
        
        cur = self.con.cursor()
        cur.execute(f"select * from students;")
        student = cur.fetchone()
        
        if student:
            print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}, Address: {student[4]}")
            choice = input("Are you sure you want to delete? (Y/N): ")
            if choice.lower() == "y":
                cur.execute(f"delete from students where studentid=%s;", (student_id))
                print("Deletion completed")
            else:
                print("Deletion cancelled")
        else:
            print("There is no student to be deleted")
        self.con.commit()
        self.con.close()
        
    def updating_data(self):
        student_id = input("Enter Student's ID to be updated: ")
        fields = {
            "1": ("name", "Enter the new name"),
            "2": ("age", "Enter new age"),
            "3": ("email", "Enter new email"),
            "4": ("address", "Enter new address")
        }
        
        for key in fields:
            print(f"{key}: {fields[key][1]}")
        
        chossing_data = input("Enter the field you want to update: ")
        valueChange = input("Enter new value: " )
        cur = self.con.cursor()
        if(chossing_data == 2):
            cur.execute(f"update students set {fields[f'{chossing_data}'][0]}={valueChange} where studentid ='{student_id}'  ")
        else:
            cur.execute(f"update students set {fields[f'{chossing_data}'][0]}='{valueChange}' where studentid ='{student_id}'  ")
        self.con.commit()
        self.con.close()
