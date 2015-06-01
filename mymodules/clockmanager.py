from mymodules.clock import Clock


class ClockManager:
    """ the ClockManger class handles reading and writing to the time format configuration file,
    creating a clock object, and switching the clock object's time format (12hr or 24hr) setting
    """
    def __init__(self, timeConfigFile=''):
        self.__timeConfigFile = timeConfigFile

    def setTimeConfigFile(self, clockConfigFile):
        self.__timeConfigFile = clockConfigFile

    def getTimeConfigFile(self):
        return self.__timeConfigFile


# gets the user's previous time format setting from the configuration file
# defaults to 12hr time if the file either doesn't exist or is blank
    def readTimeConfig(self):
        try:
            with open(self.__timeConfigFile, 'r') as f:
                timeConfig = int(f.readline())
                return timeConfig
        except:
            timeConfig = 12
            return timeConfig


# writes to the configuration file to save the user's time format setting
    def writeTimeConfig(self, clock):
        timeConfig = str(clock.getTimeFormat())
        with open(self.__timeConfigFile, 'w') as f:
            f.write(timeConfig)


    def createClock(self):
        return Clock(self.readTimeConfig())


    # switches the time format display (12hr to/from 24hr)
    def switchTimeFormat(self, clock):
        clock.changeTimeFormat()
        self.writeTimeConfig(clock)
        clock.ClockDisplay()
        clock.TimeLabel()
        clock.ButtonLabel()

