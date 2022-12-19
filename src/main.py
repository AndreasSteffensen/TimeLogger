import sys
from tkinter import *
from tkinter import ttk
from enum import Enum
from csvFileWriter import CSVFILEWRITER

# class DAYS(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5

# class TIMELOGGER:
#     def __init__(self):
#         self.log = False
#         self.fileWriter = None
#         self.setupScreen()
#         self.day = DAYS.MONDAY
#         return

#     def setupScreen(self):
#         root = Tk()

#         root.title("TimeLogger")
#         root.geometry('550x400')
    

#         lbl = Label(root, text = "here you can log your time! Pres to calculate ")
#         lbl.grid(column=0, row=0)

#         lbl = Label(root, text = "Monday: starting time:")
#         lbl.grid(column=0, row=1)
#         txt = Entry(root, width=10)
#         txt.grid(column =1, row = 1)

#         lbl = Label(root, text = "Tuesday: ")
#         lbl.grid(column=0, row=2)
#         txtTue = Entry(root, width=10)
#         txtTue.grid(column =1, row = 2)
        
#         lbl = Label(root, text = "Wednesday: ")
#         lbl.grid(column=0, row=3)
#         txtWed = Entry(root, width=10)
#         txtWed.grid(column =1, row = 3)

#         lbl = Label(root, text = "Thursday: ")
#         lbl.grid(column=0, row=4)
#         txtThu = Entry(root, width=10)
#         txtThu.grid(column =1, row = 4)

#         lbl = Label(root, text = "Friday: ")
#         lbl.grid(column=0, row=5)
#         txtFri = Entry(root, width=10)
#         txtFri.grid(column =1, row = 5)

#         # function to display user text when
#         # button is clicked
#         def clicked():
#             fw = CSVFILEWRITER()

#         btn = Button(root, text = "Calculate" ,
#                     fg = "black", command=clicked)

#         btn.grid(column=2, row=0)

#         root.mainloop()

if __name__ == "__main__":
    