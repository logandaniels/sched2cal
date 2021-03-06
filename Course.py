class Course:
    
    def setTitle(self, title):
        self.title = title
    def setTimes(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
    def setLocation(self, location):
        self.location = location
    def setSectionType(self, sectionType):
        self.sectionType = sectionType
    def setDays(self, days):
        self.days = days
    def setStartDate(self, date):
        self.startDate = date
    def setEndDate(self, date):
        self.endDate = date

    def getTitle(self):
        return self.title + " - " + self.sectionType
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    def getLocation(self):
        return self.location
    def getSectionType(self):
        return self.sectionType
    def getDays(self):
        return self.days    
    def getStartDate(self):
        return self.startDate
    def getEndDate(self):
        return self.endDate


    def __str__(self):
        return ', '.join([self.title, self.sectionType, self.days,
         self.startTime, self.endTime, self.location])
