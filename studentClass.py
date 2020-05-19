# student call 
class student:

    # instance variables
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    # get name function - returns the name
    def getGpa(self):
        return self.gpa
    # set name fucntion - changes name to what is passed in when calling the fucntion
    def setGpa(self, gpa):
        self.gpa = gpa
        
    # get name function - returns the name
    def getName(self):
        return self.name
    # set name fucntion - changes name to what is passed in when calling the fucntion
    def setName(self, name):
        self.name = name

# creating an instance of the stduent class, called alex - pass in town variables
# for name and gpa which are required
alex = student('Timmy', 3.5)

# get the name which was passed in when creating the instance
print(alex.getName())
# get the gpa which was passed in when creating the instance
print(alex.getGpa())
print()
print()

# within the new instance - called the set gpa function and pass in its new value
alex.setGpa(5.0)
# print the result of getGpa fucntion 
print('GPA =', alex.getGpa())
# # within the new instance - called the set name function and pass in its new value
alex.setName('Aj')
# print the result of getName fucntion 
print('Name =', alex.getName())
