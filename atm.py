from random import randint
# ATM Services
class ATM:
    
    def __init__(self):
        self.Balance = 10000

    # User Account
    def UserAccount(self, Account, Mobile, Password, Rpassword):
        self.Account = Account
        self.Mobile = Mobile
        self.Password = Password
        self.Rpassword = Rpassword 
        self.Balance = self.Balance
        Uchoise = 0
        if len(str(self.Account)) == 5 :
            if len(str(self.Mobile)) == 10 :
                if len(str(self.Password)) == 6 :
                    if self.Password ==  self.Rpassword :
                        cotp = randint(100000,1000000)
                        print(f"Your six digit OTP is {cotp}.")
                        uotp = int(input("Enter Your 6 digit OTP : "))
                        if cotp == uotp :
                            
                            while Uchoise != 4:
                                Uchoise = int(input('''
                                                1. Deposite
                                                2. Withdrow
                                                3. Mini Statement
                                                4. Exit
                                                '''))
                                if Uchoise == 1:
                                    damount = int(input("Enter Deposite Amount : "))
                                    self.Balance = self.Balance + damount
                                    print(f'''
                                      Your Account is deposited by Rs. {damount} 
                                      and your current Balance is INR Rs. {self.Balance}.
                                      ''')
                            
                                elif Uchoise == 2:
                                    wamount = int(input("Enter Withrow Amount : "))
                                    if wamount > self.Balance:
                                        print("Insufficant Balance, Please enter valid amount")
                                    else :
                                        self.Balance = self.Balance - wamount
                                        print(f'''
                                            Your Account is Withrowed by Rs. {wamount} 
                                            and your current Balance is INR Rs. {self.Balance}.
                                            ''')
                                elif Uchoise == 3 :
                                    print()
                                    print(f'''
                                              -: Mini Statement :-
                                          
                                        Current Balance : {self.Balance}
                                          
                                        Deposite Amount : {damount}
                                         Withrow Amount : {wamount}
                                          
                                          ''')
                                
                                elif Uchoise == 4 :
                                    print('''
                                          Thank You for using ABC Bank ATM Services.
                                          ''')
                                    break
                                
                        else :
                            print("Your OTP is not match with Computerised OTP.")
                    else :
                        print("Password did not match. Please enter valid Password")
                else :
                    print("Enter 6 digit valid password")
            else :
                print("Enter 10 digit valid Mobile number.")
        else :
            print("Enter 5 digit Account Number.")
        
b = ATM()

while True :
    print ("Welcome to ABC Bank ATM services.")
    
    Account= int(input("Enter Your 5 digit Account Number : "))
    Mobile = int(input("Enter Your 10 digit Mobile Number : "))
    Password = int(input("Enter Your 6 digit Password : "))
    Rpassword = int(input("Re-enter 6 digit Password : "))
    b.UserAccount(Account, Mobile, Password, Rpassword)
    
