

class CSVFILEWRITER:
    def __init__(self):
        self.path = "./Log/logfile.txt"
        self.fieldnames = ['Day', 'Date', 'Starting time', 'Ending time', 'Total']
        self.writeToFile()

    def writeToFile(self):
        f = open(self.path, 'a',  encoding='UTF8', newline='')
        writer = csv.DictWriter(f, fieldnames=self.fieldnames)
        writer.writeheader()
        writer.writerow(testday)

    def getTimestamp(self):
        return "_"+ str(datetime.datetime.now().day) + "-" + str(datetime.datetime.now().month)+ "-" + str(datetime.datetime.now().year) + "--" + str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute)
