#import eventCreator
import calendar

# starting day of the cycle.
i = 3

year = 2019  # moved a year back for testing reasons

# starting dates, the program always starts with 1A days
month = 1
day = 9 # Correct starting date, should get holidays by then.

endDate = '2019-4-29'

holidayList = ['2019-1-11', '2019-9-24', '2019-9-12', '2019-10-7', '2019-10-8', '2019-10-9', '2019-10-10', '2019-10-11', '2019-11-22']

#'2018-8-23', '2018-8-27', '2018-8-28', '2018-8-29', '2018-8-30',

scheduleArray = [['TOK', 'Chemistry HL', 'Spanish HL', 'Business and Management SL '],
                 ['Study Hall', 'Mathematics HL', 'Language and Literature SL', 'Physics HL'],
                 ['Chemistry HL', 'Spanish HL', 'Business and Management SL ', 'TOK'],
                 ['Mathematics HL', 'Language and Literature SL', 'Physics HL', 'Study Hall'],
                 ['Spanish HL', 'Business and Management SL ', 'TOK', 'Chemistry HL'],
                 ['Language and Literature SL', 'Physics HL', 'Study Hall', 'Mathematics HL'],
                 ['Business and Management SL ', 'TOK', 'Chemistry HL', 'Spanish HL'],
                 ['Physics HL', 'Study Hall', 'Mathematics HL', 'Language and Literature SL']]

montueStartTime = ['8:00:00', '10:15:00', '11:50:00', '14:00:00']
montueEndTime = ['9:25:00', '11:40:00', '13:15:00', '15:20:00']

wedStartTime = ['8:00:00', '9:45:00', '10:50:00', '13:05:00']
wedEndTime = ['8:55:00', '10:40:00', '11:45:00', '14:00:00']

thuStartTime = ['8:00:00', '10:15:00', '11:50:00', '14:00:00']
thuEndTime = ['9:25:00', '11:40:00', '13:15:00', '15:20:00']

friStartTime = ['8:50:00', '10:15:00', '11:50:00', '14:00:00']
friEndTime = ['10:05:00', '11:40:00', '13:15:00', '15:20:00']

for k in range(500):  # 12 specify the number of days you want the program to run for.

    year_in = str(year)
    month_in = str(month)
    day_in = str(day)
    date = year_in + '-' + month_in + '-' + day_in

    #print('')
    #print('')
    #print(date)


    # Increasing month
    if day == 30 and month == 2 and calendar.isleap(year):  # Leap year consideration for 2020
        # print(calendar.isleap(year))
        day = 1
        month += 1
        # print('next month!  febleap')
    if day == 29 and month == 2 and not calendar.isleap(year):  # for Non-leap year februaries
        day = 1
        month += 1
        # print('next month! feb')
    if day == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
        day = 1
        month += 1
        # print('next month! small')
    if day == 32 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        day = 1
        month += 1
        # print('next month! big')

    # Increasing Year
    if month > 12:
        month = 1
        year += 1
        # print('next year!')

    if date == endDate:
        break

    for h in holidayList:
        if date == h:
            day += 1
            year_in = str(year)
            month_in = str(month)
            day_in = str(day)
            date = year_in + '-' + month_in + '-' + day_in

        # Monday
    if calendar.weekday(year, month, day) == 0:
        print('')
        print('Monday')
        for j in range(4):
            if j == 1:
                print('Advisory : 9:35:00 - 10:05:00')
                #eventCreator.main('Advisory', date, '9:35:00', '10:05:00')
            print(scheduleArray[i % 8][j] + ' : ' + montueStartTime[j] + ' - ' + montueEndTime[j])
            #eventCreator.main(scheduleArray[i % 8][j], date, montueStartTime[j], montueEndTime[j])

        # Tuesday
    if calendar.weekday(year, month, day) == 1:
        print('')
        print('Tuesday')
        for j in range(4):
            if j == 1:
                print('Advisory : 9:35:00 - 10:05:00')
                #eventCreator.main('Advisory', date, '9:35:00', '10:05:00')
            print(scheduleArray[i % 8][j] + ' : ' + montueStartTime[j] + ' - ' + montueEndTime[j])
            #eventCreator.main(scheduleArray[i % 8][j], date, montueStartTime[j], montueEndTime[j])

        #Wednesday
    if calendar.weekday(year, month, day) == 2:
        print('')
        print('Wednesday')
        for j in range(4):
            if j == 1:
                print('Assembly : 9:05:00 - 9:35:00')
                #eventCreator.main('Assembly', date, '9:05:00','9:35:00')
            if j == 3:
                print('HL Time : 11:45:00 - 12:15:00')
                #eventCreator.main('HL Time', date, '11:45:00', '12:15:00')
            print(scheduleArray[i % 8][j] + ' : ' + wedStartTime[j] + ' - ' + wedEndTime[j])
            #eventCreator.main(scheduleArray[i % 8][j], date, wedStartTime[j], wedEndTime[j])

        #Thursday
    if calendar.weekday(year, month, day) == 3:
        print('')
        print('Thursday')
        for j in range(4):
            if j == 1:
                print('HL Time : 9:25:00 - 10:05:00')
                #eventCreator.main('HL Time', date, '9:25:00', '10:05:00')
            print(scheduleArray[i % 8][j] + ' : ' + thuStartTime[j] + ' - ' + thuEndTime[j])
            #eventCreator.main(scheduleArray[i % 8][j], date, thuStartTime[j], thuEndTime[j])

        #Friday
    if calendar.weekday(year, month, day) == 4:
        print('')
        print('Friday')
        for j in range(4):
            if j == 0:
                print('Personal Learning Choices : 7:45:00 - 8:45:00')
                #eventCreator.main('Personal Learning Choices', date, '7:45:00', '8:45:00')
            print(scheduleArray[i % 8][j] + ' : ' + friStartTime[j] + ' - ' + friEndTime[j])
            #eventCreator.main(scheduleArray[i % 8][j], date, friStartTime[j], friEndTime[j])

        #Saturday
    if calendar.weekday(year, month, day) == 5:
        print('')
        print('Saturday')
        i -= 1

        #Sunday
    if calendar.weekday(year, month, day) == 6:
        print('')
        print('Sunday')
        i -= 1

    # Increasing Day
    day += 1
    i += 1
