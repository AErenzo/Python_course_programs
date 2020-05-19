def timesTables():
    tt = int(input('Please enter the timetable you would like to veiw: '))

    for i in range(1, 11):
        print(tt, 'x', i, '=', tt*i)
timesTables()
