print("\n\n\n\n\n")
from tkinter import *
import sys
import time
global count
count =0
class stopwatch():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')        
    def start(self):
        global count
        count=0
        self.timer()   
    def stop(self):
        global count
        count=1
    def close(self):
        self.root.destroy()
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer)     
    def __init__(self):
        self.root=Tk()
        self.root.title("counttimer")
        self.root.geometry("650x250")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.bt1 = Button(self.root,text="start",command=self.start,bg=("green"))
        self.bt3 = Button(self.root,text="Resume",command=self.start,bg=("green"))
        self.bt2 = Button(self.root,text="Pause",command=self.stop,bg=("red"))
        self.bt4 = Button(self.root,text="Reset",command=self.reset,bg=("orange"))
        self.bt5 = Button(self.root, text="Exit", command=self.close,bg=("yellow"))
        self.lb.place(x=230,y=10)
        self.bt1.place(x=120,y=100)
        self.bt2.place(x=220,y=100)
        self.bt3.place(x=320,y=100)
        self.bt4.place(x=420,y=100)
        self.bt5.place(x=520,y=100)

        self.root.configure(bg='white')
        self.root.mainloop()
a=stopwatch()   


'''
from tkinter import *
window = Tk()
window.title("COUNTDOWN TIMER")
mainloop() # desplaying the window
        def reset():
                def pause():
                def resume():
                def exit():


import time
global count

s = 0
m = 0
h = 0

class countdown():
        ''' '''
        def __int__(self,starttime = 0 ,endtime = 0,elapsedtime = 0):
                self.__starttime = starttime
                self.__endtime = endtime
                self.__elapsedtime = elapsedtime
        ''' '''
        def start(self):
                #self.__starttime = time.clock()
                #print("calling timer")
                #global count
                #count = 0
                #tt = time.fromtimestamp(count)
                #cstart = tt.strftime("%H : %M : %S")
                print("cstart")

        def stop(self):
                #self.start
                print("calling stop")


s = countdown()
#a = input(" 1 - start \t  2 - stop \t\n 3 - reset \t 4 - pause  \t 5 - resume  \n : ")
s.start()
'''
'''
import time
import datetime
from time import sleep
import keyboard # Create class that acts as a countdown
running = True
nowtime = 0
a = True
b= True
def count(h,m,s):
        # Calculate the total number of seconds
        total_seconds = h * 3600 + m * 60 + s
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
                
        while running == True:
                timer = datetime.timedelta(seconds = total_seconds)
                print(timer, end="\r")
                print("1 - stop \t2 - reset \t3 - pause  \t4 - resume : ")
                import os
                # Clearing the Screen
                os.system('cls')
                # Delays the program one second
                sleep(1)
                nowtime = timer
                if keyboard.is_pressed("1"):
                        if running == True:
                                print("end-time : ",timer)
                                running == False
                                break
                elif keyboard.is_pressed("2"):
                        if running == True:
                                running ==False
                                print("Restarting :")
                                countdown()
                elif keyboard.is_pressed("3"):
                        if running == True:
                                running == False
                                nowtime = timer
                                countresume()
                                break
                elif keyboard.is_pressed("4"):
                        if running == True:
                                countpause(nowtime)
                                
                                
                
                #Reduces total time by one second
                total_seconds += 1
        print(" The timer stopped")
                                                
                                

def countresume():
        if running == True:
                print("resume-time : ")
                sleep(7)
                if input == "":
                        sleep(5)
                        if keyboard.is_pressed("4"):
                           print("hi")
                else:
                        sleep
                        
                        
                       
                
def countdown():
        h ,m ,s = 0,0,0
        s = count(int(h), int(m), int(s))
# Inputs for hours, minutes, seconds on timer
countdown()


'''
'''
# NEW CODE 
while running == True:
    print("hello")
    sleep(1)
    
        
            if running 
        else:
            running = True\
'''


