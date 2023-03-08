user="mouni"
password="mouni123"
User_name=input('Enter the UserName:')
print(User_name.upper(),"Thank You for giving Username")
pass_word=input('Enter the PassWord:')
Amount=1000
if user==User_name and pass_word==password:
    s='''
   1.Credit
   2.Debit
   3.Mini Statement
   4.Exit
'''
    print(s)
    while True:
        option=int(input("Enter the Choice:"))
        if option==1:
            credit_amount=int(input("Enter the Amount:"))
            print("After Credit ", credit_amount+Amount)
        elif option==2:
            debit_amount=int(input("Enter the Amount:"))
            print("After Debit ", Amount-debit_amount)
        elif option==3:
            print("Mini statement",Amount)
        elif option==4:
            break