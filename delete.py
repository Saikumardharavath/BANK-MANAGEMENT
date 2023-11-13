# install library mqsql-connector-python
import mysql.connector

#creating connection
class delete:
    def __init__(self):
        self.conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sai@8466035932',
            database='bank'
            )
        
    def specific_del(self,table_name,cid):
        cur=self.conn.cursor()
        cur.execute(f"delete from {table_name} where customerID={cid}")
        self.conn.commit()
        print("------data has been deleted sucessfully------")