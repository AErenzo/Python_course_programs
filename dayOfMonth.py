mOy = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


month = int(input('What month of the year is it? (1 - 12) '))
day = int(input('what day of the month is it? (1 - 31) '))

if month == 1:
    print('Its the', day, 'of Januaray')
elif month == 2:
     print('Its the', day, 'of Feburary')
elif month == 3:
     print('Its the', day, 'of March')
elif month == 4:
     print('Its the', day, 'of April')
elif month == 5:
     print('Its the', day, 'of May')
elif month == 6:
     print('Its the', day, 'of June')
elif month == 7:
     print('Its the', day, 'of July')
elif month == 8:
     print('Its the', day, 'of August')
elif month == 9:
     print('Its the', day, 'of September')
elif month == 10:
     print('Its the', day, 'of October')
elif month ==11:
     print('Its the', day, 'of Novermber')
elif month == 12:
     print('Its the', day, 'of December')
else:
     print('Invalid input. Please enter a number between 1-12')


sumDate = 0 # this can be asisgned to days to reduce amount of code

for i in range(month - 1):
    sumDate = mOy[i] + sumDate

print('The total number of days till this date hase been', sumDate + day)
