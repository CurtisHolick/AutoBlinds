import sched, time, threading
import datetime
from datetime import timezone, timedelta
#from BlindsController import BlindsController


class TimeManager:
    def __init__(self, blindsController):
        self.checkInterval = 30 #Seconds between checking time
        self.bc = blindsController
        self.scheduler = sched.scheduler(time.time, time.sleep)

        self.thread = threading.Thread(target=self.scheduleSetup)
        self.thread.start()


    def scheduleSetup(self):
        self.scheduler.enter(self.checkInterval, 1, self.checkTimes, (self.scheduler,))
        self.scheduler.run()

    def checkTimes(self, sc):
        #print("Checking times")
        if self.checkOpenTime():
            print("OPEN TIME, opening blinds")
            self.bc.openBlinds()
        elif self.checkCloseTime():
            print("CLOSE TIME, closing blinds")
            self.bc.closeBlinds()
        else:
            print("Not any time, Open at:", str(self.bc.getOpenTime()), "Close at:", str(self.bc.getCloseTime()))
        self.scheduler.enter(self.checkInterval, 1, self.checkTimes, (sc,))

    def timeEquals(self, timeStr):
        actualTimeStr = datetime.datetime.now(tz=timezone(timedelta(hours=-5))).strftime("%H:%M")
        # print(actualTimeStr, actualTimeStr == timeStr)
        print("Comparing times, Actual:", actualTimeStr, "comparing to:", timeStr)
        return actualTimeStr == timeStr
        # print(actualTimeStr == timeStr)

    def checkOpenTime(self):
        if self.timeEquals(self.bc.getOpenTime()):
            return True
        else:
            return False

    def checkCloseTime(self):
        if self.timeEquals(self.bc.getCloseTime()):
            return True
        else:
            return False





    # def bar(self, sc):
    #     print("Running bar")
    #     self.s2.enter(1, 1, self.bar, (sc,))
    #
    # def foo(self, sc):
    #     print("Running foo")
    #     self.s1.enter(1, 1, self.foo, (sc,))

# def sch1():
#     tm.s1.enter(1, 1, tm.foo, (tm.s1,))
#     tm.s1.run()
#
# def sch2():
#     tm.s2.enter(1, 1, tm.bar, (tm.s2,))
#     tm.s2.run()

# if __name__ == '__main__':
#     tm = TimeManager()#BlindsController())



    # t1 = threading.Thread(target=sch1)#, args=(10,))
    # t2 = threading.Thread(target=sch2)#, args=(10,))
    # t1.start()
    # t2.start()
    # for i in range(30):
    #     print("Loop print")
    #     time.sleep(1)
    # tm.s1.enter(1, 1, tm.foo, (tm.s1,))
    # tm.s2.enter(1, 1, tm.bar, (tm.s2,))
    # tm.s1.run()
    # tm.s2.run()