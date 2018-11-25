import Constants
import datetime


# Starts a log file and documents time & date
def logGameTime():
    p = open(Constants.PILLAR_LOG_PATH, "a")
    f = open(Constants.EVENT_LOG_PATH, "a")

    p.write( str(datetime.datetime.now()) + '\n')
    f.write( str(datetime.datetime.now()) + '\n')


# Logs game events
def logEvents(event):
    f = open(Constants.EVENT_LOG_PATH, "a")
    f.write(str(event))
    f.write('\n')


# Writes to play_data files if play state completed properly
def manageLogs(out_state):

    if(out_state == Constants.MENU_STATE):
        logGameTime()

        event_log = open(Constants.EVENT_LOG_PATH, "r")
        event_data = open(Constants.EVENT_DATA_PATH, "a")
        event_data.write(event_log.read())

        pillar_log = open(Constants.PILLAR_LOG_PATH, "r")
        pillar_data = open(Constants.PILLAR_DATA_PATH, "a")
        pillar_data.write(pillar_log.read())

    open(Constants.EVENT_LOG_PATH, 'w').close()
    open(Constants.PILLAR_LOG_PATH, 'w').close()