import mysql.connector as connector

class LoginHelper:

    def __init__(self) :
        self.con = connector.connect(host = 'localhost',port='3306',user='root',password='#Vishnu697#',database ='record')
        
        query = 'create table if not exists login_Patient(emailId varchar(200) primary key, firstName varchar(200) ,password varchar(200))'

        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self,emailId,firstName,password):
        query = "insert into login_Patient values('{}','{}','{}')".format(emailId,firstName,password)

        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to db")
        
    def fetch_user(self,emailId):
        query = "select * from login_Patient where emailId = '{}'".format(emailId)

        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("EmailId:", row[0])
            print("firstName:", row[1])
            print("password:", row[2])
            return row

    def delete_user(self,emailId):
        query = "delete from login_Patient where emailId = '{}'".format(emailId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update_user(self,emailId,new_firstName,new_password):
        query = "update login_Patient set firstName ='{}',password='{}' where emailId = {}".format(new_firstName,new_password, emailId)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


class LoginDoctor:
    
    def __init__(self) :
        self.con = connector.connect(host = 'localhost',port='3306',user='root',password='#Vishnu697#',database ='record')
        
        query = 'create table if not exists login_Doctor(emailId varchar(200) primary key, firstName varchar(200) ,password varchar(200))'

        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self,emailId,firstName,password):
        query = "insert into login_Doctor values('{}','{}','{}')".format(emailId,firstName,password)

        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to db")
        
    def fetch_user(self,emailId):
        query = "select * from login_Doctor where emailId = '{}'".format(emailId)

        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("EmailId:", row[0])
            print("firstName:", row[1])
            print("password:", row[2])
            return row

    def delete_user(self,emailId):
        query = "delete from login_Doctor where emailId = '{}'".format(emailId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update_user(self,emailId,new_firstName,new_password):
        query = "update login_Doctor set firstName ='{}',password='{}' where emailId = {}".format(new_firstName,new_password, emailId)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


if __name__ == '__main__':

    cur = LoginHelper()
    # cur.update_user(1111,"k","l","m","n")
    # cur.insert_user("vishnutiwari7796@gmail.com","Vishnu Tiwari","#Vishnu697#")
    # cur.delete_user("vishnutiwari7796@gmail.com")

    doc = LoginDoctor()

    row = cur.fetch_user("vk@gmail.com")
    print(row)

    row = doc.fetch_user("vk@gmail.com")
    print(row)

    # cur.delete_user('vk@gmail.com')
    doc.delete_user('vk@gmail.com')
    
    row = cur.fetch_user("vk@gmail.com")
    print(row)

    row = doc.fetch_user("vk@gmail.com")
    print(row)
