from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, fn, ln, ssn):
        self.__firstName = fn
        self.__lastName = ln
        self.__soicalSecNum = ssn

    def setFirstName(self, fn):
        self.__firstName = fn

    def getFirstName(self):
        return self.__firstName

    def setLastName(self, ln):
        self.__lastName = ln

    def getLastName(self):
        return self.__lastName

    def setSoicalSecNum(self, ssn):
        self.__soicalSecNum = ssn

    def getSoicalSecNum(self):
        return self.__soicalSecNum

    def checkPositive(self, value):

        if value < 0.0:
            msg = 'Attribute Value {} must be positive'.format(value)
            raise ValueError(msg)
        else:
            return value
        
    def __str__(self):
        return 'First_Name: {} Last_Name: {} Social_Security_Number: {}'.format(self.getFirstName(), self.getLastName(), self.getSoicalSecNum())

    @abstractmethod
    def earning (self):
        pass


class SalaryEmployee(Employee):

    def __init__(self, fn, ln, ssn, ws):
        super().__init__(fn, ln, ssn)
        self.__weeklySalary = ws

    def setWeeklySalary(self, ws):
        
        self.__weeklySalary = self.checkPositive(ws)

    def getWeeklySalary(self):
        return self.__weeklySalary

    def earning(self):
        return self.getWeeklySalary()

    def __str__(self):
        return 'Salaried Employee: {} \nWeekly Salary: {:.2f}'.format(super().__str__(), self.getWeeklySalary())
        


class HourlyEmployee(Employee):

    def __init__(self, fn, ln, ssn, wage, hw):
        super().__init__(fn, ln, ssn)
        self.setWage(wage)
        self.setHoursWorked(hw)

    def setWage(self, wage):
        self.__wage = self.checkPositive(wage)
        

    def getWage(self):
        return self.__wage

    def setHoursWorked(self, hw):
        if hw >= 0.0 and hw <= 168.0:
            self.__hoursWorked = hw
        else:
            raise ValueError('Hourly wage must be greater >= 0 and <= 168')    

    def getHoursWorked(self):
        return self.__hoursWorked

    def earning(self):
        if self.getHoursWorked() <= 40:
           return self.getWage() * self.getHoursWorked()
        else:
            return 40 * self.getWage() + ((self.getHoursWorked() - 40) * (self.getWage() * 1.5)) 
        

    def __str__(self):
        return 'Hourly Employee: {} \nHourly wage: {:.2f} \nHours worked: {:.2f}'.format(super().__str__(),
                                                                                     self.getWage(), self.getHoursWorked())



class CommissionEmployee(Employee):

    def __init__(self, fn, ln, ssn, sales, cr):
        super().__init__(fn, ln, ssn)
        self.setGrossSales(sales)
        self.setCommissionRate(cr)

    def setCommissionRate(self, cr):
        if cr > 0.0 and cr < 1.0:
            self.__commissionRate = cr
            return self.__commissionRate
        else:
            raise ValueError('Commission rate must be between 0.0 and 1.0')
        
    def getCommissionRate(self):
        return self.__commissionRate

    def setGrossSales(self, sales):
        self.__grossSales = self.checkPositive(sales)
        

    def getGrossSales(self):
        return self.__grossSales

    def earning(self):
        return self.getGrossSales() * self.getCommissionRate()
        

    def __str__(self):
        return 'Commission Employee: {} \n{} {:.2f} \n{} {:.2f}'.format(super().__str__(), 'Commission rate: ', self.getCommissionRate(), 'Gross Sales: ', self.getGrossSales())



# main program

sEmp = SalaryEmployee('Alex', 'Erentz', '111-11-1111', 500.00)

hEmp = HourlyEmployee('Tom', 'Bedford', '222-22-2222', 12.5, 40)

cEmp = CommissionEmployee('Jack', 'Dann', '333-33-3333', 400, 0.4)


print('sEmp is an object which extends the employee class: ', isinstance(sEmp, Employee))
print(sEmp)

print()

print('hEmp is an object which extends the employee class: ', isinstance(hEmp, Employee))
print(hEmp)

print()

print('cEmp is a subclass of employee class: ', issubclass(CommissionEmployee, Employee))
print(cEmp)
 
print()

employees = [sEmp, hEmp, cEmp]

for i in employees:
    print(i.earning())
