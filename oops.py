#atm project with oops concepts

class Atm:
    
    def __init__(self):
        
        self.pin=4300
        self.balance=20000
        self.menu()
        
        
    
    def menu(self):
        print('''
         what would you like your option
             1.deposite
             
             2.withdrall
             
             3.balance check
             
             4.exit
        ''')
             
        option=int(input("enter a your option:"))
              
        if option==1:
            self.deposite_balance()
        elif option==2:
            self.withdrall_balance()
            
        elif option==3:
            self.check_balance()
        elif option==4:
                sys.exit()
        
    

    def deposite_balance(self):
        opt=int(input("enter a pin number:"))
        if opt==self.pin:
            input_balance=int(input("enter a your deposite amount:"))
            self.balance=self.balance+input_balance
            print("*" *50)
            print(f"your deposite amount is Rs.{input_balance}")
            print(f"your total amount is Rs.{self.balance}")
            print("*" *50)
            
        else:
            print("enter your wrong pin number")
            
        self.menu()    
            
            
    def withdrall_balance(self):
        opt=int(input("enter a pin number:"))
        if opt==self.pin:
            input_withd=int(input("enter a your withdrall amount:"))
            if input_withd <= self.balance:
                self.balance = self.balance- input_withd
                print("*" *50)
                print(f"your withdrall amount Rs.{input_withd}")
                print(f"your balance is Rs.{self.balance}")
                print("*" *50)
                
            else:
                print("your amount is too much")
                
                
        else:
            print("your pin number is wrong number")
            
        self.menu()    

    def check_balance(self):
        opt=int(input("enter a pin number:"))
        print("*" *50)
        print(f"your balance is Rs.{self.balance}")
        print("*" *50)
        self.menu()
        
    

        

        

        


        
            

obj=Atm()  
