import winsound
import random
import time
import datetime
import keyboard

from tkinter import *

begin = datetime.datetime.now()
print ("Current date and time: ")
print (begin.strftime("%Y-%m-%d %H:%M:%S"))
beginwrite = (begin.strftime("%Y-%m-%d %H:%M:%S"))

f = open("Work_time.txt", "a")
f.write('Begin time: '+beginwrite+ '\n')
f.close()

# class MyWindow:
#     def __init__(self, win):
#         self.btn=Button(window, text="This is Button Start widget", fg='blue',command=self.start)
#         self.btn.place(x=80, y=100)
#         self.lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
#         self.lbl.place(x=60, y=50)
#         self.txtfld=Entry(window, text="This is Entry Widget", bd=5)
#         self.txtfld.place(x=80, y=150)
#     def start(self):
#         probability=120

#         while 1:

#             l = random.randint(0,probability)
#             print(l)
#             if l<=1:
#                 winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
#                 probability=120
#                 self.txtfld.delete(0, 'end')
#                 self.txtfld.insert(END, str(probability))
#                 time.sleep(10)
#             else:
#                 probability-=1
#             print(probability)
#             time.sleep(1)
#     def add(self):
#         self.t3.delete(0, 'end')

#         num1=int(self.t1.get())
#         num2=int(self.t2.get())

#         result=num1+num2
#         self.t3.insert(END, str(result))
#     def sub(self, event):
#         self.t3.delete(0, 'end')

#         num1=int(self.t1.get())
#         num2=int(self.t2.get())

#         result=num1-num2
#         self.t3.insert(END, str(result))

# window=Tk()
# mywin=MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()

# probability=120
starttime = time.time()
boolarray =[]

for i in range(1800):
    boolarray.append(0)

for a in range(30):
    index = random.randint(0,1800-1)
    boolarray[index]=1

while len(boolarray)>0:
    newtime = time.time()
    l = random.randint(0,len(boolarray)-1)
    print(boolarray[l]) 
    seconds =(newtime-starttime)
    
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print("Elapsed Time: %d:%02d:%02d" % (hour, minutes, seconds))

    
    if boolarray[l]==1:
        winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
        time.sleep(10)
        winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
        time.sleep(50)

    del boolarray[l]
    print(len(boolarray))
    if (keyboard.is_pressed("a") and keyboard.is_pressed("s") and keyboard.is_pressed("d") and keyboard.is_pressed("f")):
        break
    time.sleep(1)
    
end = datetime.datetime.now()
print ("Current date and time: ")
print (end.strftime("%Y-%m-%d %H:%M:%S"))
endwrite = end.strftime("%Y-%m-%d %H:%M:%S")

winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
time.sleep(1)
winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
time.sleep(1)
winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
time.sleep(1)

f = open("Work_time.txt", "a")
f.write('End time: '+endwrite+ '\n')
f.close()