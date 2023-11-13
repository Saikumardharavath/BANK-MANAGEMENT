from create import insert
from read import read
from update import update
from delete import delete


obj=insert()
objread=read()
objupdate=update()
objdelete=delete()

print("------Bank management system--------")
print("for inserting the data press 1:")
print("for reading the data press 2:")
print("for updating the data press 3:")
print("for deleting thr data press 4")

opr = int(input("please enter your operation:"))

def myopr():
     print("-------for personal information press 1:")
     print("-------for bank details press 2:")
     print("--------for transaction details press 3:")
     print("--------for account details press 4:")
     sk=int(input("please select your table :"))
     if sk == 1:
          return 'personal_details'
     elif sk ==2:
          return 'bank_details'
     elif sk ==3:
          return 'transaction_details'
     elif sk ==4:
          return 'account_details'
     

if opr ==1:
    k=myopr()
    if k=='personal_details':
        cid=int(input("please enter customer id:"))
        fname=input("please enter customer fname:")
        lname=input("please enter customer lname:")
        addr=input("please enter customer addr:")
        phn=int(input("please enter customer phn:"))
        an=input("please enter customer an:")
        pan=input("please enter customer pan:")
        obj.personal_details(cid,fname,lname,addr,phn,an,pan)
    elif k=='bank_details':
        acn=int(input("please enter account number :"))
        cid=int(input('please enter customerID :'))
        ifsc= input('please enter ifsc code :')
        actype=input('please enter account type :')
        obj.bank_details(acn,cid,ifsc,actype)
    elif k=='transaction_details':
        tid=int(input("please enter transactionID :"))
        sac= int(input("please enter sender account number"))
        rac=int(input("please enter receiver account number :"))
        amount=int(input("please enter amount;"))
        method=input("please enter method :")
        obj.transaction_details(tid,sac,rac,amount,method)
    elif k=='account_details':
        acn=int(input("please enter account number :"))
        tid=int(input("please enter transactionID :"))
        amount=int(input("please enter amount :"))
        cbal=int(input("please enter closing balance"))
        tp= input("please enter transaction type :")
        obj.account_details(acn,tid,amount,cbal,tp)

if opr==2:
    s=myopr()
    cid=int(input("please enter custometID for fetching data"))
    objread.specific_info(cid,s)
    
if opr==3:
    s=myopr()
    cid=int(input("please enter customr id for fetching the data:"))
    colname=input("please enter column name :")
    newval=input("please enter the new value :")
    objupdate.myupdate(s,colname,newval,cid)

if opr==4:
    k=myopr()
    cid=int(input("please enter customerID  to delete the data:"))
    objdelete.specific_del(k,cid)





        

        
    
 


