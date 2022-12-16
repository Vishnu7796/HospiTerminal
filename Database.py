import mysql.connector as connector

class DBHelper:

    def __init__(self) :
        self.con = connector.connect(host = 'localhost',port='3306',user='root',password='#yourpassword#',database ='record')
        
        query = 'create table if not exists Patient(userId int auto_increment primary key,userName varchar(200), Diagnosis varchar(200),Symptoms varchar(200) ,Prescription varchar(200))'

        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self,username,Diagnosis,Symptoms,Prescription):
        query = "insert into Patient(userName,Diagnosis,Symptoms,Prescription) values('{}','{}','{}','{}')".format(username,Diagnosis,Symptoms,Prescription)
        
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to db")
        
    def fetch_user(self,userName):
        query = "select * from Patient where userName = '{}'".format(userName)
        cur = self.con.cursor()
        cur.execute(query)
        patient = []

        for row in cur:
            # print("UserId:",row[0])
            # print("Username:",row[0])
            # print("Diagnosis:",row[1])
            # print("Symptoms:",row[2])
            # print("Prescription:",row[3])
            patient.append(row)

        return patient

    def delete_user(self,userName):
        query = "delete from Patient where userName= '{}'".format(userName)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update_user(self,userId,NewUserName,NewDiagnosis,NewSymptoms,NewPrescription):
        query = "update Patient set userName ='{}',Diagnosis='{}',Symptoms='{}',Prescription='{}' where userId = {}".format(NewUserName,NewDiagnosis,NewSymptoms,NewPrescription,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


class tempHelper:
    
    def __init__(self) :
        self.con = connector.connect(host = 'localhost',port='3306',user='root',password='#yourpassword#',database ='record')
        
        query = 'create table if not exists Temp(pat_email varchar(200) primary key, Doc_email varchar(200), Pat_Name varchar(200),Symptoms varchar(200))'

        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self,pat_email,Pat_Name,Symptoms,Doc_email):

        query = "insert into Temp(pat_email,Doc_email,Pat_Name,Symptoms) values('{}','{}','{}','{}')".format(pat_email,Doc_email,Pat_Name,Symptoms)

        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to db")
        
    def fetch_user(self,Doc_email):
        query = "select * from Temp where Doc_email = '{}'".format(Doc_email)
        cur = self.con.cursor()
        cur.execute(query)
        patient = []
        flag = False

        for row in cur:
            if flag == False:
                patient.append(row)


        query = "select * from Temp where Doc_email = 'default'"
        cur = self.con.cursor()
        cur.execute(query)

        for row in cur:
            if flag == False:
                patient.append(row)

        return patient

    def delete_user(self,pat_email):
        query = "delete from Temp where pat_email= '{}'".format(pat_email)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update_user(self,userId,NewUserName,NewDiagnosis,NewSymptoms,NewPrescription):
        query = "update Patient set userName ='{}',Diagnosis='{}',Symptoms='{}',Prescription='{}' where userId = {}".format(NewUserName,NewDiagnosis,NewSymptoms,NewPrescription,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


if __name__ == '__main__':
    
    cur = tempHelper()
    # cur.insert_user('vkk@gmail.com','vishnu','fever','vk@gmail.com')
    row = cur.fetch_user('vk@gmail.com')
    print(row)
    
