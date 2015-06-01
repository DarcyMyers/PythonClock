import time

class Clock:
    """ the Clock class handles setting the time label, the clock display,
    and the button label based on the current time format setting (12hr or 24hr)

    """
    def __init__(self, timeFormat):
        self.__timeFormat = timeFormat
        self.__timeLabel = ''
        self.__clockDisplay = ''
        self.__buttonLabel = ''

    # getters
    def getTimeFormat(self):
        return self.__timeFormat
    def getTimeLabel(self):
        return self.__timeLabel
    def getClockDisplay(self):
        return self.__clockDisplay
    def getButtonLabel(self):
        return self.__buttonLabel

    # setters
    def setTimeFormat(self, timeFormat):
        self.__timeFormat = timeFormat
    def setTimeLabel(self, timeLabel):
        self.__timeLabel = timeLabel
    def setClockDisplay(self, clockDisplay):
        self.__clockDisplay = clockDisplay
    def setButtonLabel(self, buttonLabel):
        self.__buttonLabel = buttonLabel


    # sets the time label text (displayed after the time display)
    def TimeLabel(self):
        if self.getTimeFormat() == 24:
            self.__timeLabel = '24 hour Format \n(Local Time)'
        else:
            if time.localtime().tm_hour <= 11:
                self.__timeLabel = 'A.M. \n(Local Time)'
            else:
                self.__timeLabel = 'P.M. \n(Local Time)'
        return self.__timeLabel


    # sets the clock display text
    def ClockDisplay(self):
        if self.__timeFormat == 24:
            self.__clockDisplay = '%H:%M:%S'
        else:
            self.__clockDisplay = '%I:%M:%S'
        return self.__clockDisplay


    # sets the button label for switching the time format
    def ButtonLabel(self):
        if self.getTimeFormat() == 12:
            self.__buttonLabel = "Change to 24hr Format"
        else:
            self.__buttonLabel = "Change to 12hr Format"
        return self.__buttonLabel


    # updates the clock object's time format
    def changeTimeFormat(self):
        if self.getTimeFormat() == 12:
            self.setTimeFormat(24)
        else:
            self.setTimeFormat(12)
