from MotorControl import MotorControl
from TimeManager import TimeManager
import datetime
from datetime import timezone, timedelta

class BlindsController:
    saveFile = "BlindsControllerData.beans"
    def __init__(self):
        self.mc = MotorControl()
        self.loadData()

        self.tm = TimeManager(self)
        print(self.isOpen)
        print(self.openTime)
        print(self.closeTime)

    def loadData(self):
        with open(BlindsController.saveFile) as saveFile:
            self.isOpen = (saveFile.readline().rstrip('\r\n') == "True")
            self.openTime = saveFile.readline().rstrip('\r\n')
            self.closeTime = saveFile.readline().rstrip('\r\n')
            self.numTurns = int(saveFile.readline().rstrip('\r\n'))

    def saveData(self):
        with open(BlindsController.saveFile, mode='w') as saveFile:
            saveFile.write(str(self.isOpen) + '\n')
            saveFile.write(self.openTime + '\n')
            saveFile.write(self.closeTime + '\n')
            saveFile.write(str(self.numTurns) + '\n')

    def toggleBlinds(self):
        if self.isOpen:
            self.openBlinds()
        else:
            self.closeBlinds()

    def openBlinds(self):
        if not self.isOpen:
            self.isOpen = True
            self.saveData()
            print("Opening...")
            self.mc.turnForward(self.numTurns)
        else:
            print("Already opening, not opening")

    def closeBlinds(self):
        if self.isOpen:
            self.isOpen = False
            self.saveData()
            print("Closing...")
            self.mc.turnBackward(self.numTurns)
        else:
            print("Already closed, not closing")

    def setOpenTime(self, time):
        self.openTime = time
        self.saveData()

    def setCloseTime(self, time):
        self.closeTime = time
        self.saveData()

    def setNumTurns(self, numTurns):
        self.numTurns = numTurns
        self.saveData()

    def getOpenTime(self):
        return self.openTime

    def getCloseTime(self):
        return self.closeTime

    def getState(self):
        return self.isOpen

    def getNumTurns(self):
        return self.numTurns

    def timeAsString(self, time):
        hour = time.split(":")[0]
        minute = time.split(":")[1]
        newTime = ""
        if(int(hour) > 12):
            newTime = str(int(hour) - 12) + ":" + minute + " PM"
        else:
            newTime = str(hour) + ":" + minute + " AM"
        return newTime

    def getStateString(self):
        if self.isOpen:
            return "open"
        else:
            return "closed"


    def getCurrentSystemTime(self):
        actualTimeStr = datetime.datetime.now(tz=timezone(timedelta(hours=-5))).strftime("%Y-%m-%dT%H:%M")
        return actualTimeStr



if __name__ == '__main__':
    bc = BlindsController()
    print(bc.timeAsString("08:30"))
    print(bc.timeAsString("10:30"))
    print(bc.timeAsString("12:30"))
    print(bc.timeAsString("20:30"))


