class Date:
    __day = 0
    __month = 0
    __year = 0

    days_in_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, y, m, d):
        self.setYear(y)
        self.setMonth(m)
        self.setDay(d)
        

        
    #set day function
    def setDay(self, day):
        
        try:
            if isinstance(day, int):
                
                if day > 0 and day <= self.days_in_month[self.__month]:
                    self.__day = day
            
                elif day == 29 and self.__month == 2 and (self.__year % 400 == 0 or (self.__year % 4 == 0 and self.__year % 100 != 0)):
                    self.__day = day
                    
                else:
                    print('Invaid Day - check leap year')
            else:
                raise Exception('Please enter an integer value')
        except Exception as e:
            print('Error Message: {}, Error Type: {}'.format(type(e), e.args))
            


    #set month fucntion
    def setMonth(self, month):
        try:
            if isinstance(month, int):
                if month <= 12 and month > 0:
                    self.__month = month
                else:
                    print('Invalid Month')
            else:
                raise Exception('Invalid data type -  please enter a integer value')
        except Exception as e:
             print('Error Message: {}, Error Type: {}'.format(type(e), e.args))




    # set year function
    def setYear(self, year):
        try:
            if isinstance(year, int):
                if year <= 2020 and year >= 1909:
                    self.__year = year
                else:
                    print('Invalid Year - time travller!')
            else:
                raise Exception('Invalid Data Type')
        except Exception as e:
            print('Error Message: {}, Error Type: {}'.format(type(e), e.args))




    # get day
    def getDay(self):
        return self.__day
    # get month
    def getMonth(self):
        return self.__month
    # get year
    def getYear(self):
        return self.__year

    def __str__(self):
        return '{:0>2d}//{:0>2d}//{} '.format(self.getDay(), self.getMonth(), self.getYear())


'''
today = Date(2020, 1, 20)
print(today)

d1 = Date(2020, 2, 29)
print(d1)

d2 = Date(2019, 2, 29)
print(d2)
'''


class student:

    __name = 0
    __gpa = 0
    __birthDate = 0
    __enrollDate = 0
    

    def __init__(self, n, g, b, e):
        self.setName(n)
        self.setGpa(g)
        self.setBirthDate(b)
        self.setEnrollDate(e)

    def getGpa(self):
        return self.__gpa

    def setGpa(self, gpa):
        try:
            if gpa > 0.0 and gpa <= 4.0:
                self.__gpa = gpa
            else:
                print('GPA measurements out of range')
        except Exception as e:
            print('Error Message: {}, Error Type: {}'.format(type(e), e.args))
            
    def getName(self):
        return self.__name
    
    def setName(self, name):
        try:
            if name.isalpha and len(name) > 0:
                self.__name = name
            else:
                print('Invalid name')
        except Exception as e:
            print('Error Message: {}, Error Type: {}'.format(type(e), e.args))

    def getBirthDate(self):
        return self.birthDate
    
    def setBirthDate(self, birthDate):
        self.__birthDate = birthDate

        

    def getEnrollDate(self):
        return self.enrollDate
    
    def setEnrollDate(self, enrollDate):
        self.__enrollDate = enrollDate

        

    def __str__(self):
        return 'Name: {}, GPA: {}, Date of Birth: {}, Enrollment Date: {}'.format(self.getName(), self.getGpa(), self.__birthDate, self.__enrollDate)


bDate = Date(1995, 3, 5)

print(bDate)

eDate = Date(2015, 9, 17)

print(eDate)

Alex = student('Alex', 3.5, bDate, eDate)

print(Alex)
