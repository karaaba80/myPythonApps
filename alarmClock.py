import datetime
import time
import subprocess
import command_parser as cp
import sys
import os
# from PyQt4.QtGui import *

def getTime():
    return str(datetime.datetime.now()).split(' ')[1].split('.')[0]

# def messageBox(message='Do you like Python?'):
#
#     a = QApplication(sys.argv)
#     messagebox = QMessageBox()
#     messagebox.setText("wait (closing automatically in {0} secondes.)".format(3))
#     messagebox.setStandardButtons(messagebox.NoButton)
#     messagebox.exec_()
#     return
    #result = messagebox.question(QWidget(), 'Message', message, QMessageBox.Ok)


def addToTime(realTime, waiting):
    rH, rM, rS = map(int, realTime.split(':'))

    # real_seconds = rM*60+rS

    tS = rS
    tM = (rM+waiting)%60
    tH = rH+int((rM+waiting)/60)

    # tH = rH+
    #
    # 15:59 +3
    return str(tH)+':'+str(tM)+':'+str(tS)


def getDiff(realTime, targetTime):
    rH,rM,rS = map(int,realTime.split(':'))
    tH, tM, tS = map(int, targetTime.split(':'))

    # if rH > tH:
    #    return -1
    #
    # if rH <= tH and rM > tM:
    return (tH-rH)*3600+(tM-rM)*60+(tS-rS)


def main_alarm(commands):
    p = cp.parser(commands, registeredInfo=
        [['-t', 'time to set(ex:12:45:00', ''],
         ['-d', 'delays(sec:def:0sec, if higher lower precision but less computation)', '*'],
         ['-msg', 'alarm message', '']]
    )

    delay = 20 if p.get('-d')=='' else int(p.get('-d'))
    message = p.get('-msg')
    targetTime = p.get('-t')

    realTime = getTime()
    diff_in_sec = getDiff(targetTime=targetTime, realTime=realTime)
    print ('target', targetTime,'real time:', realTime, 'difference in smin', round(diff_in_sec/60,2))
    while True:
        # realtime = getTime().split(':')
        # tTime = targetTime.split(':')
        # if realtime[0]==tTime[0]
        # print('target time', targetTime, 'real time:', getTime())
        realTime = getTime()
        if getDiff(targetTime=targetTime, realTime=realTime) < delay+1:
           # print('target time', targetTime, 'real time:', getTime())
        # if getTime().startswith(targetTime):
           break
        else:
           time.sleep(delay)

    message = 'time is up!' + message
    print ('time is up!',message)
    #messageBox('time is up!' + message)
    # audiofile = "C:\\Users\\f.karaaba\\Music\\Lost Highway\\Lost Highway Angelo Badalamenti - Red bats with teeth - You.webm"
    audiofile = "C:\\Users\\f.karaaba\\Music\\sounds\\Creepy-clock-chiming.mp3"
    # audiofile = "/media/karaaba/DataStorage/media/Series/StarTrekTOS/Season1/S01E27 The Alternative Factor.avi"
    subprocess.call(["vlc", '--meta-title',message,audiofile,'--gain','30'])

    exit()
    # with open(os.devnull, 'wb') as nul:
    #     subprocess.call(['mplayer', '-msglevel', 'all=-1', audiofile], stdin=nul)

def main_timer(commands):
    p = cp.parser(commands,
                  registeredInfo=
        [['-t', 'time to set wait(minute)', ''],
         #['-t', 'time to set(ex:12:45:00', ''],
         ['-d', 'delays(sec:def:0sec, if higher lower precision but less computation)', '*'],
         ['-msg', 'alarm message', '']]
    )

    delay = 20 if p.get('-d')=='' else int(p.get('-d'))
    message = p.get('-msg')
    timeToWait = int(p.get('-t'))
    realTime = getTime()
    targetTime = addToTime(realTime, timeToWait)


    #diff_in_sec = getDiff(targetTime=targetTime, realTime=realTime)
    # print ('target', targetTime,'real time:', realTime, 'difference in smin', round(diff_in_sec/60,2))
    while True:
        realTime = getTime()
        diff = getDiff(targetTime=targetTime, realTime=realTime)
        if diff < delay+1:
           break
        else:
           print('diff', diff)
           time.sleep(delay)

    message = 'time is up!' + message
    print ('time is up!',message)
    audiofile = "C:\\Users\\f.karaaba\\Music\\sounds\\Creepy-clock-chiming.mp3"
    # audiofile = "/media/karaaba/DataStorage/media/Series/StarTrekTOS/Season1/S01E27 The Alternative Factor.avi"
    subprocess.call(["vlc", '--meta-title',message,audiofile,'--gain','30'])

    exit()


if __name__ == '__main__':
    commands = [('alarm', 'set a fixed clock time'),
                ('timer', 'minutes')]

    if len(sys.argv) == 1:
        print('options are', commands)
        exit()

    inputCommand = sys.argv[1]
    commandArgs = sys.argv[1:]

    if sys.argv[1] == commands[0][0]:
        main_alarm(commandArgs)

    elif sys.argv[1] == commands[1][0]:
        main_timer(commandArgs)

    else:
        print('unknown keyword:', sys.argv[1])
