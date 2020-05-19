class Account:

    __accNumber = 0

    __balance = 0

    def __init__(self, accNumber, balance):
        self.setAccNumber(accNumber)
        self.setBalance(balance)

    def getAccNumber(self):
        return self.__accNumber
    
    def getBalance(self):
        return self.__balance

    def setBalance(self, amount):
        try:
            if isinstance(amount, int) and amount >= 0:
                self.__balance = amount
            else:
                raise Exception ("Amount being set to balance must be 0 or greater and only containing numerical values")
        except Exception as e:
            print(e.args)
            
    def setAccNumber(self, accNumber):
        try:
            if len(accNumber) == 8 and accNumber.isdigit():
                self.__accNumber = accNumber
            else:
                raise Exception ('Account number must be 8 digits long')
        except Exception as e:
            print('Error Type: {}, Error Message: {}'.format(type(e), e.args))

    def Credit(self, amount):
        try:
            if amount > 0:
                self.__balance += amount
            else:
                raise Exception ('Credt amount must be greater than 0')
        except Exception as e:
            print('Error Type: {}, Error Message: {}'.format(type(e), e.args))

    def Debit(self, amount):
        try:
            if self.__balance < amount:
                raise Exception ('Transaction declined - amount exceeds your balance')
            else:
                self.__balance -= amount
        except Exception as e:
            print('Error Type: {}, Error Message: {}'.format(type(e), e.args))  

            
    def __str__(self):
        return ("Account Number: {}, Balance: {}").format(self.getAccNumber(), self.getBalance())



#object of class

a1 = Account(65489658, -300)

print(a1)
print()
print('Account Number:', a1.getAccNumber())
print()
print('Balance:', a1.getBalance())
print()
a1.setBalance(1500)
print('Balance:', a1.getBalance())
print()
a1.Credit(0)
print('Balance:', a1.getBalance())
print()
a1.Debit(50)
print('Balance:', a1.getBalance())
a1.Debit(5000)

    
        
