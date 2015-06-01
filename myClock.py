"""
==============================================================
TKinter Digital Clock
==============================================================
- Displays/Toggles 12 hour or 24 hour display.
- Records the 12 hour or 24 hour setting in a configuration file for use when re-opened.
"""

from tkinter import *
import time
from mymodules.clockmanager import ClockManager

# initialize the clock object
# if a config file exists the clock is initialized with the time format in the config file
myClockManager = ClockManager('clockConfig.dat')
c = myClockManager.createClock()


# the ticking() function handles the updating and formating of the time display
def ticking():
    # update the time display and time label from the clock object's ClockDisplay() method()
    # these both depend on the time format (24hr or 12hr)
    myTime = time.strftime(c.ClockDisplay())
    myTimeLabel = (c.TimeLabel())
    # display the date
    myDate = time.strftime('%A, %B %d, %Y')

    # format the time and time label text
    clock.create_image(0, 0, anchor=NW, image=bgImage)
    clock.create_text(50, 75, text=myTime, font=('times', 50, 'bold'), fill='white', anchor=NW)
    clock.create_text(310, 120, text=myTimeLabel, font=('times', 12, 'bold'), fill='white', anchor=NW)

    #format the date text
    clock.create_text(50, 50, text=myDate, font=('times', 20, 'bold'), fill='white', anchor=SW)

    # using the tkinter after() method to update (call) the tick function every 100 milliseconds
    clock.after(100, ticking)


# this function switches the time format when the user clicks the switch time format button
def toggleTimeFormat():
    # calls the clock object's switchTimeFormat() method to switch the clockDisplay and the TimeLabel
    myClockManager.switchTimeFormat(c)
    # re-sets the button text
    buttonText.set(c.ButtonLabel())
    # updates the button's text
    root.update_idletasks()


# tkinter layout
root = Tk()

# using a tkinter canvas in order to overlay the clock's text on an image
clock = Canvas(root)

# setting a background image for the clock canvas
bgImage = PhotoImage(file="daisyAnt2.GIF")
clock.img = bgImage

# using a LabelFrame so that the image shows when the button is packed
frame = LabelFrame(clock).pack(padx=215, pady=120)

# setting the initial button text for the tkinter Button textvariable option
# this requires making the button text a StringVar() object then using the StringVar object's
#  set() method to set the button text to the output of the clock object's ButtonLabel() method
buttonText = StringVar()
buttonText.set(c.ButtonLabel())

# configuring and packing the time format toggle button
switchTimeFormatButton = Button(clock, textvariable=buttonText, command=toggleTimeFormat).pack(padx=10, pady=10, anchor=SE)

# packing everything in the clock canvas
clock.pack(expand=YES, fill='both')

# calling the ticking function to update the clock's time, display, and format
ticking()

# the mainloop for running the tkinter gui
root.mainloop()
