from flask import Flask, render_template, request, redirect
from BlindsController import BlindsController
from ScheduleManager import ScheduleManager
import os

app = Flask(__name__)
bc = BlindsController()
#deploy: add sm back in
# sm = ScheduleManager(bc)


@app.route('/')
def index():
    return render_template("index.html", blindsState=bc.getStateString(),
                           openTime=bc.timeAsString(bc.getOpenTime()),
                           closeTime=bc.timeAsString(bc.getCloseTime()))


@app.route('/toggleBlinds', methods=['POST'])
def toggleBlinds():
    if bc.getState():
        bc.closeBlinds()
    else:
        bc.openBlinds()
    return render_template("index.html", blindsState=bc.getStateString(),
                           openTime=bc.timeAsString(bc.getOpenTime()),
                           closeTime=bc.timeAsString(bc.getCloseTime()))


@app.route('/settings')
def settings():
    return render_template("settings.html", openTime=bc.getOpenTime(),
                           closeTime=bc.getCloseTime(),
                           numTurns=bc.getNumTurns(),
                           systemTime=bc.getCurrentSystemTime())


@app.route('/saveSettings', methods=["POST"])
def saveSettings():
    newOpenTime = request.form['openTime']
    bc.setOpenTime(newOpenTime)
    newCloseTime = request.form['closeTime']
    bc.setCloseTime(newCloseTime)
    newNumTurns = int(float(request.form['numTurns']))
    bc.setNumTurns(newNumTurns)
    return settings()


@app.route('/saveTime', methods=["POST"])
def saveTime():
    newSysTime = request.form['systemTime']
    print(newSysTime)
    date = newSysTime.split("T")[0]
    time = newSysTime.split("T")[1] + ":00"
    newFormattedSysTime = date + " " + time
    print("Formatted:", newFormattedSysTime)
    os.system('sudo date -s {}'.format(newFormattedSysTime))


    return settings()


if __name__ == '__main__':
        # app.run(host='0.0.0.0', port=8091)
    app.run()

