from functools import partial
from tkinter import *
from datetime import datetime


root = Tk()
root.geometry("400x400")

currentLog = ""

def logCurrent(isStart):
    global currentLog
    time = datetime.now().strftime('%H:%M')
    print(type(time))
    if int(time[0:2]) > 12:
        currentTime = str(int(time[0:2])-12)+time[2:]+"pm"
    else:
        currentTime = time + "am"
    print(currentTime)
    if isStart:
        currentLog += currentTime + " - --:---m: " + myScreen[1].get() + "\n"
        myScreen[4].config(text=currentLog)


root.title("Title")
myScreen = [Label(root, text="Test"),
            Entry(root),
            Button(root, command=partial(logCurrent, True), text="Start"),
            Button(root, command=partial(logCurrent, False), text="End"),
            Label(root, text="")
            ]
myGrid = [myScreen[0].grid(row=0, column=0),
          myScreen[1].grid(row=1, column=0),
          myScreen[2].grid(row=2, column=0),
          myScreen[3].grid(row=2, column=1),
          myScreen[4].grid(row=3, column=0)
          ]

root.mainloop()
