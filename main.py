from tkinter import *
import time
import threading
import math
root = Tk()

root.title("Cookie Clicker")
root.geometry('500x300')


outputText = StringVar()
cookieCounter = IntVar()
cookies = 0
cInterval = 1
upgrade1Add = 100
upgrade2Add = 500
upgrade3Add = 1000
upgrade1PriceLabel = IntVar()
upgrade1PriceLabel.set(upgrade1Add)
upgrade2PriceLabel = IntVar()
upgrade2PriceLabel.set(upgrade2Add)
upgrade3PriceLabel = IntVar()
upgrade3PriceLabel.set(upgrade3Add)

def click():
  global cookieCounter
  global cInterval
  global cookies
  
  cookies = cookies + cInterval
  cookieCounter.set(math.floor(cookies))

def upgrade1():
  global cookieCounter
  global cookies
  global upgrade1Add
  global cInterval
  
  if cookieCounter.get() < upgrade1Add:
    outputText.set("not enough cookies")
  elif cookieCounter.get() >= upgrade1Add:  
    cInterval = cInterval + .5
    cookies = cookies - (upgrade1Add)
    upgrade1Add = upgrade1Add * 1.2
    upgrade1PriceLabel.set(math.floor(upgrade1Add))
    cookieCounter.set(math.floor(cookies))

CPS = 0
cpsDisplay = IntVar()

def upgrade2():
  global cookieCounter
  global cookies
  global upgrade2Add
  global cInterval
  global CPS
  if cookieCounter.get() < upgrade2Add:
    outputText.set("not enough cookies")
  elif cookieCounter.get() >= upgrade2Add:
    
    cookies = cookies - upgrade2Add
    upgrade2Add = upgrade2Add * 1.5
    CPS = CPS + 1
    upgrade2PriceLabel.set(upgrade2Add)
    cpsDisplay.set(CPS)
  print("cookie")
    
def upgrade3():
  global cookieCounter
  global cookies
  global upgrade2Add
  global cInterval
  global CPS
  global upgrade3Add
  if cookieCounter.get() < upgrade3Add:
    outputText.set("not enough cookies")
  elif cookieCounter.get() >= upgrade3Add:
    
    cookies = cookies - upgrade3Add
    upgrade3Add = upgrade3Add * 1.5
    CPS = CPS + 10
    upgrade3PriceLabel.set(upgrade2Add)
    cpsDisplay.set(CPS)
  print("cookie")

def cps():
  global cookieCounter
  global cookies
  global upgrade2Add
  global CPS
  global cpsDisplay
  
  threading.Timer(1.0, cps).start()
  
  cookies = cookies + CPS
  cpsDisplay.set(CPS)
  cookieCounter.set(cookies)
  outputText.set("")

label1=Label(root, bg="white", width=20, textvariable = cookieCounter)
label1.place(x = 10, y = 10)

output = Label(root, bg = "gray", width = 20, height = 10, textvariable = outputText)
output.place(x = 10, y = 35)

cookie = Button(root, width = 10, height = 4, text = "cookie", command = lambda: click())
cookie.place(x = 180, y = 10)

upgrade1btn = Button(root, bg = "blanched almond",text = "UPGRADE", width = 10, height = 1, command = lambda: upgrade1())
upgrade1btn.place(x = 180, y = 100)
upgrade1Price = Label(root, bg = "blanched almond", width = 20, height = 1, textvariable = upgrade1PriceLabel)
upgrade1Price.place(x = 300, y = 100)

upgrade2btn = Button(root,bg="cyan",text = "UPGRADE",width=10,height=1,command=lambda: upgrade2())
upgrade2btn.place(x=180,y=140)
upgrade2Price = Label(root,bg="cyan",width=20,height=1,textvariable=upgrade2PriceLabel)
upgrade2Price.place(x=300,y=140)

upgrade3btn = Button(root,bg="blue",text = "UPGRADE",width=10,height=1,command=lambda: upgrade3())
upgrade3btn.place(x=180,y=180)
upgrade3Price = Label(root,bg="blue",width=20,height=1,textvariable=upgrade3PriceLabel)
upgrade3Price.place(x=300,y=180)

cpsLabel = Label (root, bg = "brown", width = 20, height = 1, textvariable = cpsDisplay)
cpsLabel.place(x = 10, y = 35)

curtime = ''
clock = Label()
clock.pack()

def tick():
    global curtime
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clock.config(text=curtime)
    clock.after(200, tick)
    #clock.after(200, cookieCounter.set(cookies + 1))

tick()
  
cps()

root.mainloop()