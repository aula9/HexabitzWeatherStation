#AulaJazmati
from tkinter import *
import time
import serial
from datetime import date

today = date.today()
print("Today's date:", today)
ser = serial.Serial(        
               port='/dev/ttyUSB0',
               baudrate = 921600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )

print(ser.name)
Main_window = Tk()
Main_window.config(background = "gray86")
Main_window.title('Hexabitz Weather Station')
#Create a window with Width = 700, Height = 250, X Position = 50, Y Position = 50
Main_window.geometry('700x250+50+50')
def sensorhub():
    global t
    read = ser.read(5)
    if len(read)!= 0:
        t = read.decode("utf-8").strip()
        print(t)
        my_label.config(text = t)
        ser.flushInput()
        ser.flushOutput()

my_button = Button(Main_window,  text="Refresh", bg="gold", font=("Arial", 16), command = sensorhub)
my_label1 = Label(Main_window, text = today , font = "Helvetica 24 bold")
my_label = Label(Main_window, text = " ", fg = "white", bg = "red", font = "Helvetica 48 bold")
my_label2 = Label(Main_window, text = "Temperature (c) & Humidity (%)" , font = "Helvetica 24 bold")
my_button.pack()
my_label1.pack()
my_label2.pack()
my_label.pack(fill=BOTH, expand=1)
Main_window.mainloop()
