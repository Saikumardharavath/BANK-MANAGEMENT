# install library mqsql-connector-python
import mysql.connector

#creating connection
class insert:
    def __init__(self):
        self.conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sai@8466035932',
            database='bank'
            )
    def personal_details(self,cid,fname,lname,addr,phn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{addr}',{phn},'{an}','{pan}')")
        self.conn.commit()
        print("----------personal informatin has been saved sucessfully-----------:")

    def bank_details(self,acn,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("---------bank_details has been sucessfully saved-------------:")

    def transaction_details(self,tid,sac,rac,amount,method):
        cur=self.conn.cursor()
        cur.execute(f"insert into transaction_details values({tid},{sac},{rac},{amount},'{method}')")
        self.conn.commit()
        print("-----------transaction_details has been saved sucessfully-------")

    def account_details(self,acn,tid,amount,cbal,tp):
        cur=self.conn.cursor()
        cur.execute(f"insert into account_details values({acn},{tid},{amount},{cbal},'{tp}')")
        self.conn.commit()
        print("-------account_details has been saved sucessfully-----")


