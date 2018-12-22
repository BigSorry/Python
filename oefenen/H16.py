import datetime
class Time:
    def __init__(self, second, minute, hour):
        self.second = second
        self.minute = minute
        self.hour = hour
def timeToInt(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
def intToTime(second):
    hoursRemaning = second % 3600
    hours = int(second / 3600)
    minutes = int(hoursRemaning / 60)
    seconds = hoursRemaning % 60
    return Time(seconds, minutes, hours)
def mulTime(time, factor):
    seconds = timeToInt(time)
    newTime = intToTime(seconds * factor)
    return newTime
def race(finishingTime, distance):
    finishingTimeSeconds = timeToInt(finishingTime)
    return  finishingTimeSeconds / distance
def birthday(born):
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if born.year + age < today.year:
        nextBirthday = datetime.date(born.year + age + 1, born.month, born.day)
        return abs(today - nextBirthday)
    else:
        nextBirthday = datetime.date(born.year + age, born.month, born.day)
        todayNextYear = datetime.date(today.year + 1, today.month, today.day)
        return abs(nextBirthday - todayNextYear)
def DoubleDay(bornYoung, bornOld):
    bornYoungBirthday = birthday(bornYoung).days
    today = datetime.date.today()
    ageYoung = 0
    if bornYoungBirthday < 365:
        ageYoung = today.year - bornYoung.year
    ageOld = today.year - bornOld.year - ((today.month, today.day) < (bornOld.month, bornOld.day))
    if ageOld / ageYoung ==  2:
        return True
    else:
        return False

bornDate = datetime.date(2012, 6, 10)
bornDate2 = datetime.date(2007, 2, 5)
days = birthday(bornDate)
print(days.days)
print(DoubleDay(bornDate, bornDate2))