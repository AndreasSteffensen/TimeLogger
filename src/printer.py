import datetime
import csv


def getWeek():
    return datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day).isocalendar()[1]

def getDate():
    return str(datetime.datetime.now().day) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().year)

def getHour():
    return datetime.datetime.now().hour

def getMin():
    return datetime.datetime.now().minute

def getUser():
    return " Andreas Steffensen"

def getClockTime(hour, min):
    if min >= 0 and min < 15:
        min = 0
    elif min > 15 and min < 45:
        hour += 0.5
    elif min > 45 and min <= 59:
        hour += 1
    return hour

def getFileName():
    return str(getWeek()) + "-log.csv"

def createFile():
    with open(getFileName(), 'x' , newline='') as file:
        writer = csv.writer(file)
        writer.writerow([" Date", " Time of check-in", " User", " Time of check-out", " Total"])

def writeToFile():
    with open(getFileName(), 'a' , newline='') as file:
        writer = csv.writer(file)
        if getHour() < 10:
            row = log(True)
        else:
            row = log(False)
        writer.writerow(row)

def log(start):
    date = getDate()
    timeIn = getClockTime(getHour(),getMin())
    user = getUser()
    if start:
        timeOut = timeIn
    else:
        timeOut = getClockTime(getHour(),getMin())

    total = timeOut - timeIn
    return [date, timeIn, user, timeOut, total]

def checkOutLog(): 
    

def readFromFile():
    weekday = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day).weekday()
    with open(getFileName(), 'r', newline='') as file: 
        reader = csv.reader(file)
        reader.__next__()
        for _ in range(weekday):
            reader.__next__()
        row = reader.__next__()
        return row[1] 

def printHello():
    print("Hello today is: ")
    writeToFile()
    print(readFromFile())

if __name__ == "__main__":
    printHello()