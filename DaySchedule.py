class DaySchedule:
    def __init__(self, weekday, openHour, closeHour):
        self.weekday = weekday
        self.openHour = openHour
        self.closeHour = closeHour

    def __str__(self):
        return "Day: {} | Open: {} | Close: {}".format(self.weekday, self.openHour, self.closeHour)

    def __repr__(self):
        return "{},{},{}\n".format(self.weekday, self.openHour, self.closeHour)