# install library mqsql-connector-python
import mysql.connector

#creating connection
class update:
    def __init__(self):
        self.conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sai@8466035932',
            database='bank'
            )
    def myupdate(self,table_name,column_name,new_value,cid):
        cur=self.conn.cursor()
        if new_value.isnumeric():
            print('test1')
            cur.execute(f"update {table_name},set{column_name}={int(new_value)} where customerid={cid}")

        else:
            print('test2')
            cur.execute(f"update {table_name} set {column_name}='{new_value}' where customerid={cid}")
        self.conn.commit()
        print("---updated sucessfully-------")

