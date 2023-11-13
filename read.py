# install library mqsql-connector-python
import mysql.connector

#creating connection
class read:
    def __init__(self):
        self.conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sai@8466035932',
            database='bank'
            )
    
    def specific_info(self,customer_id,table_name):
        cur=self.conn.cursor()
        if table_name=='personal_details' or table_name=='bank_details':
            cur.execute(f"select * from {table_name} where customerID={customer_id}")
            print(cur.fetchall())

        if table_name=='transaction_details':
            print("test1")
            cur.execute(f'''select * from transaction_details where transactionID in 
                (select transactionID from account_details where account_number in
                (select account_number from bank_details where customerID={customer_id}));''')
            print(cur.fetchall())

    


        


    
