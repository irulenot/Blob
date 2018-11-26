import Constants


def logPillarData(self):
    f = open(Constants.LOG_PATH, "a")
    f.write(str(self.__dict__['image']) + ',')
    f.write(str(self.__dict__['rect']) + ',')
    f.write(str(self.__dict__['boundary_left']) + ',')
    f.write(str(self.__dict__['boundary_right']) + ',')
    f.write(str(self.__dict__['change_x']))
    f.write('\n')


# Logs game events
def logEvents(event):
    f = open(Constants.LOG_PATH, "a")
    f.write(str(event))
    f.write('\n')


# Writes to play_data files if play state completed properly
def finishLog(out_state):
    if (out_state == Constants.MENU_STATE):
        log_file = open(Constants.LOG_PATH, "r")
        play_data_file = open(Constants.PLAY_DATA_PATH, "a")
        play_data_file.write(log_file.read() + '\n\n')

    clearLog()


def clearLog():
    open(Constants.LOG_PATH, 'w').close()
