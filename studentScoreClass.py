class StudentScore:

    def __init__(self, math, english, science):
        self.math = math
        self.english = english
        self.science = science

    def getMath(self):
        return self.math
    def getEnglish(self):
        return self.english
    def getScience(self):
        return self.science

    def getAvg(self):
        return (self.math + self.english + self.science) / 3

    def getMax(self):
        return max(self.math, self.english, self.science)

s1 = StudentScore(60, 59, 75)

print('maths -', s1.getMath())
print('English', s1.getEnglish())
print('Science', s1.getScience())
print('Average score -', s1.getAvg())
print('Max score -', s1.getMax())


