import eventCreator
import calendar
import datetime

holidayList = ['2021-03-29', '2021-04-02', '2021-05-03', '2021-05-04', '2021-05-05', '2021-05-06'
, '2021-05-07' , '2021-05-14', '2021-05-26']

subjectDictionary = {
"Electronics Engineering": ["9:00:00", "9:00:00", "9:00:00", "0", "12:00:00"],
"Engineering Mathematics 2": ["16:00:00", "10:00:00", "11:00:00", "16:00:00", "0"],
"Engineering Chemistry": ["11:00:00", "11:00:00", "16:00:00", "12:00:00", "0"],
"Engineering Workshop": ["0", "0", "0", "0", "9:00:00"],
"Communication Skills": ["10:00:00", "0", "12:00:00", "0", "16:00:00"],
"Material Science and Engineering": ["0", "13:00:00", "0", "14:00:00", "14:00:00"],
"Communication Skills Lab": ["0", "12:00:00","0","0","0"],
"Engineering Chemistry Lab": ["0", "0","0","0","11:00:00",],
"Electrical Engineering Lab": ["0", "0","0","10:00:00","0"]}

weekDayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

startDate = datetime.date(2021,5,21)
endDate = datetime.date(2021,6,18)
delta = datetime.timedelta(days=1)
classLenght = datetime.timedelta(hours=1)

while startDate <= endDate:
#Holiday checker
    for h in holidayList:
        holiday = datetime.datetime.strptime(h, '%Y-%m-%d').date()
        if startDate == holiday:
            startDate += delta

    for day in weekDayList:
        if calendar.day_name[startDate.weekday()] == day:
            print('\n' + day + " " +str(startDate))
            for subject in subjectDictionary.keys():
                timing = subjectDictionary[subject][weekDayList.index(day)]
                if timing != "0":
                    subjectStartTime = datetime.datetime.strptime(timing, '%H:%M:%S')
                    subjectEndTime = (subjectStartTime + classLenght).time()
                    subjectStartTime = datetime.datetime.strptime(timing, '%H:%M:%S').time()
                    print(subject + " : " + str(subjectStartTime)+ ' ' + str(subjectEndTime)+ "\n")
                    eventCreator.main( subject, str(startDate), str(subjectStartTime), str(subjectEndTime))
    startDate += delta
