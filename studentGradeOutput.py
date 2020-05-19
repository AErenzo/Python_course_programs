marks = []

a = []
b = []
c = []
f = []

for i in range(10):
    score = int(input('Please enter the student marks: '))
    marks.append(score)

print()
print(marks)
print()

for i in range(len(marks)):
    if marks[i] >= 80:
        a.append(marks[i])
    elif marks[i] < 80 and marks[i] > 59:
        b.append(marks[i])
    elif marks[i] < 60 and marks[i] > 39:
        c.append(marks[i])
    else:
        f.append(marks[i])
            
print(len(a), 'students have grade A')
print(len(b), 'students have grade B')
print(len(c), 'students have grade C')
print(len(f), 'students have grade F')
