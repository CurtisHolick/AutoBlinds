from flask import Flask, render_template, request, redirect, url_for
from ScheduleManager import ScheduleManager
from DaySchedule import DaySchedule

app = Flask(__name__)

sm = ScheduleManager()
#depoly: diff with app.py

@app.route('/')
def index():
    return render_template("index.html", blindsState="open",
                           openTime="8:00 AM",
                           closeTime="10:00 PM")



@app.route('/settings')
def settings():
    return render_template("settings.html", openTime="08:00",
                           closeTime="20:00",
                           numTurns=15,
                           systemTime="2022-02-25T12:20")

@app.route("/toggleBlinds", methods=["POST"])
def toggleBlinds():
    return redirect(url_for('settings'))
    # return settings()
    # return render_template("settings.html", openTime="8:00",
    #                        closeTime="20:00",
    #                        numTurns=15,
    #                        systemTime="2022-02-25T12:20")

#deploy: add to main app file
@app.route("/schedule")
def schedule():
    dayTimes = sm.getTimesForTemplate()
    return render_template("schedule.html", dayTimes=dayTimes)

#deploy: add to main app file
@app.route("/saveSchedule", methods=["POST"])
def saveSchedule():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    abbrDays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

    newDaySchedules = []
    for i in range(len(days)):
        dayStr = abbrDays[i]
        openTime = request.form["{}OpenTimeInput".format(days[i])]
        closeTime = request.form["{}CloseTimeInput".format(days[i])]
        closeTime = str(int(closeTime) + 12)
        day = DaySchedule(dayStr, openTime, closeTime)
        newDaySchedules.append(day)

    sm.updateSchedules(newDaySchedules)

    return redirect(url_for('schedule'))




if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8091)
