class Date:
    __day = 0
    __month = 0
    __year = 0

    DM = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, d, m, y):
        self.setDay(d)
        self.setMonth(m)
        self.setYear(y)

    # set day function
    def setDay(self, day):
        try:
            if isinstance(day, int):
                if day > 0 and day <= self.DM[self.__month]:
                    self.__day = day

                elif day == 29 and self.__month == 2 and (self.__year % 400 == 0 or
                                                          (self.__year % 4 == 0 and self.__year % 100 != 0)):
                    self.__day = day

                else:
                    print('Invaid Day')
            else:
                raise Exception('Please enter an integer value')
        except Exception as e:
            print('Error Message: {}, Error Type: {}'.format(type(e), e.args))

    # set month fucntion
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


today = Date(5, 4, 2020)
print(today)





