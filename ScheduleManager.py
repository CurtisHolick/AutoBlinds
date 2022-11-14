from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import OrTrigger

import atexit
import time #TODO: remove?
from datetime import datetime #TODO: remove?
from DaySchedule import DaySchedule


class ScheduleManager:
    saveFile = "scheduleData.beans"
    def __init__(self): #, blindsController):  # deploy: add bc to constructor
        # self.bc = blindsController
        self.dailySchedules = self.loadSchedule()
        self.combinedTrigger = self.generateCombinedTrigger()

        print(self.combinedTrigger)

        self.scheduler = BackgroundScheduler()
        self.scheduledJob = self.scheduler.add_job(func=self.toggleBlinds, trigger=self.combinedTrigger)
        # self.scheduler.add_job(func=self.foo, trigger='cron', day_of_week='mon, thu', second='5, 20-40')
        self.scheduler.start()
        atexit.register(lambda: self.scheduler.shutdown())
        #exit = input("Waiting...") #deploy: remove


    def toggleBlinds(self):  # deploy: enable
        print("Toggling blinds")
        # self.bc.toggleBlinds()

    def saveSchedule(self):
        with open(ScheduleManager.saveFile, mode='w') as saveFile:
            for day in self.dailySchedules:
                saveFile.write(repr(day))

    def generateCombinedTrigger(self):
        cronTriggers = []
        for day in self.dailySchedules:
            hourStr = "{}, {}".format(day.openHour, day.closeHour)
            trigger = CronTrigger(day_of_week=day.weekday, hour=hourStr)
            cronTriggers.append(trigger)
        return OrTrigger(cronTriggers)

    def loadSchedule(self):
        schedules = []
        with open(ScheduleManager.saveFile, mode='r') as saveFile:
            for i in range(7):
                splitLine = saveFile.readline().rstrip('\r\n').split(",")
                print("Day schedule list:", splitLine)
                daySchedule = DaySchedule(*splitLine)
                schedules.append(daySchedule)
        return schedules

    def getDailySchedule(self, weekday):
        for day in self.dailySchedules:
            if day.weekday == weekday:
                return day

    def setDailySchedule(self, day, openTime):  # TODO: remove?
        daySchedule = self.getDailySchedule(day)
        daySchedule.openHour = openTime
        self.saveSchedule()

    def updateSchedules(self, newSchedules):
        self.scheduledJob.remove()
        self.dailySchedules = newSchedules
        self.saveSchedule()
        self.combinedTrigger = self.generateCombinedTrigger()
        self.scheduledJob = self.scheduler.add_job(func=self.toggleBlinds, trigger=self.combinedTrigger)
        if self.scheduler.state == 0:  # Scheduler is stopped
            self.scheduler.start()

        print("Schedules updated")
        print(self.combinedTrigger)

    def getTimesForTemplate(self):
        #returns dict with format:
        #{'Sunday': [8, 11],
        # 'Monday': [openHour, closeHour], etc.
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        dayTimes = dict()
        for i in range(len(self.dailySchedules)):
            day = self.dailySchedules[i]
            closeTime = str(int(day.closeHour) - 12)
            dayTimes[days[i]] = [day.openHour, closeTime]

        return dayTimes


    def __str__(self):
        outStr = ""
        for day in self.dailySchedules:
            outStr += repr(day)
        return outStr

if __name__ == '__main__':
    # from BlindsController import BlindsController
    # bc = BlindsController()
    sm = ScheduleManager()
    print("SM before")
    print(sm)

    print("Monday:")
    print(sm.getDailySchedule("mon"))

    sm.setDailySchedule("mon", 6)
    print("SM after")
    print(sm)

