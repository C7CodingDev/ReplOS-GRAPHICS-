adl = [9,6,7,3]
wl = [0.3,0.02,0.01]
DESC = 'ReplOS is a OS-Like System made out of python and tkinter. Its beta and has a theme similar to windows 95 or 98 enjoy! #tkinter #python #tk #graphics |photo by unsplash! bg image coming soon. OVER 100 LINES OF CODE' #OVER100LINESOFCODE'#description that appers in the OS info 
####IMPORT AND SCREEN CONFIG####
from tkinter import messagebox
import turtle,os,random,tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
####LOADING SCREEN####
import time
for i in range(3):
 ws = Tk()
 def step():
    for i in range(37):
        ws.update_idletasks()
        pb1['value'] += random.choice(adl)
        time.sleep(random.choice(wl))
        
    pb1.destroy()
    ws.destroy()
 pb1 = Progressbar(ws, orient=HORIZONTAL, length=379, mode='determinate')

 pb1.pack(expand=True)
 step()
####MAIN####
screen = turtle.Screen() #DO NOT EDIT THIS! THIS RENDERS THE ALSO RENDERS!
alex = turtle.Turtle()  #DO NOT EDIT THIS! THIS WILL BE USED FOR FUTURE UPDATES!!!
####SETTINGS####
SYSTEM_LOCK = False #if system is locked
UNLOCKABLE = True #if the user can unlock the system from the lock
PHOTOVIEWER_ALLOWED = True #if the photoviewer is allowed
OS_ID = 9623684842 #The id for the OS version
version = 'v.1.6' #OS Version
build = 1222021 #LastUpdated [optional: if the OS was updated 5 hours later you can add .2 or somthing  like that]
DOWNLOADING_ALLOWED = True #If the user can download games [discluding chatbot because it is BUILT IN]
CALCULATOR_ALLOWED = True #I put this feture because I dont want people using the calculator for school tests
####DO NOT EDIT ON_GITHUB HOWEVER IN LINES WHEN YOU ADD CODE LINES CHANGE IT TO THE  NEW LINE AMOUNT!####
ON_GITHUB = True
LINES = 141
####DO NOT EDIT BELOW THIS UNLESS YOU KNOW HOW TOO!!#### 
####LOCK CONFIG####
if SYSTEM_LOCK == True:
  if UNLOCKABLE == True:
   lock=messagebox.askyesno("LOCK_ERROR403","The Locked Setting has been enabled. Set SYSTEM_LOCK to False to unlock. Or click yes to unlock in commandline")
   if lock == True:
     unlockm=screen.textinput('CommandLine','Unlock by putting in UNLOCK in the CommandLine')
     if unlockm == 'UNLOCK':
      messagebox.showinfo('UNLOCK','unlocked! you may continue')
   if lock == False:
     messagebox.showerror('LOCK DETECTED ','Click ok to unlock')
  if UNLOCKABLE == False:
    messagebox.showerror('You Cannot Unlock','You cannot unlock this because UNLOCKABLE has been set to False.')
    exit('unlockable was set to false')
####LOGIN DO NOT EDIT UNLESS YOU KNOW HOW TOO####
code = os.environ['passcode']
seto=int(screen.numinput('Set','set password to:'))
code = seto
del(seto)
loginpass=int(screen.numinput('Login','Password'))
if loginpass == code:
  ####SYSTEM AFTER CORRECT PASSWORD ENTERED [basicly the OS]####
  screen.bgcolor('light blue')
  ####COMMANDLINE####
  while True:
    run=screen.textinput('Run','Open/Run:')
    ####commandslist###
    if run == 'cmds':
      messagebox._show('AppId=CmdsAppViewer948255','Commands: photoviewer -- views a pic  | logout -- logs out| game -- chat bot game| OSinfo -- more info about the os | Download -- download more games!| calculator - calculator','question','okcancel')
      ####photoviewer####
    if run == 'photoviewer':
      if PHOTOVIEWER_ALLOWED == True:
       messagebox.showinfo('imageviewer','picture: infoicon.png')
      if PHOTOVIEWER_ALLOWED == False:
       messagebox.showwarning('403 - access denied','access was denied due to setting PHOTOVIEWER_ALLOWED set to False')
       ####logout####
    if run == 'logout':
      lo=int(screen.numinput('Login','Password'))
      if lo == code:
       screen.bgcolor('light blue')
      else:
       messagebox.showerror('wrongpasscode','error wrong password: '+str(lo))
    if run == 'game':
      ####CHAT BOT GAME####
      cbq_Name = screen.textinput('ChatBot','Whats Your Name?')
      messagebox.showinfo('ChatBot - Result1','Hello '+cbq_Name)
      screen.textinput('Chat Bot','How Are You doing '+cbq_Name+'?')
      messagebox.showinfo('ChatBot - Result2','Thats GREAT!')
      screen.textinput('Chat Bot','whats your fav animal '+cbq_Name+'?')
      messagebox.showinfo('ChatBot - Result3','Thats Intresting!')
      screen.textinput('Chat Bot','whats your fav food? '+cbq_Name+'?')
      messagebox.showinfo('ChatBot - Result4','Ok! Thats cool')
      ####OS INFO####
    if run == 'OSinfo':
     messagebox.showinfo('Version','Version: '+version)
     messagebox.showinfo('OSid','OS id:'+str(OS_ID))
     messagebox.showinfo('desc','description: '+DESC)
     ####100 LINES MARK WHOOHOO!!!####
     messagebox.showinfo('build','build: '+str(build))
     messagebox.showinfo('Github','On Github: '+str(ON_GITHUB))
     messagebox.showinfo('Lines',' Fun Fact: There are '+str(LINES)+' Of code!')
    ####DOWNLOADING####
    if run == 'Download':
      if DOWNLOADING_ALLOWED == True:
        dwnld=screen.textinput('download','Download: [DL for download list]')
        if dwnld == 'DL':
          
          ####FakeBsod####
          messagebox.showinfo('app9128768586','FakeBsod')
        if dwnld == 'FakeBsod':
         screen.bgcolor('blue')
         time.sleep(3)
         screen.bgcolor('light blue')
      if DOWNLOADING_ALLOWED == False:  
       messagebox.showerror('403','ACCESS DENIED. DOWNLOADING SET TO False.')
       ####CALCULATOR####
    if run == 'calculator':
      if CALCULATOR_ALLOWED == True:
       num1 = int(screen.numinput('Calculator','Number1:'))
       num2 = int(screen.numinput('Calculator','Number2'))
       oper = screen.textinput('Calculator','Operator')
       if oper == '+':
         calcresult = str(num1+num2)
         messagebox.showinfo('CalculatorResult','Your Awnser Is:'+str(calcresult))
       if oper == '-':
         calcresult = str(num1-num2)
         messagebox.showinfo('CalculatorResult','Your awnser is:'+str(calcresult))
       if oper == '*':
         calcresult = str(num1*num2)
         messagebox.showinfo('CalculatorResult','Your awnser is '+str(calcresult))
       if oper == '/':
         calcresult = str(num1/num2)
         messagebox.showinfo('CalculatorResult','Result: '+str(calcresult))
      if CALCULATOR_ALLOWED == False:
        messagebox.showerror('403','403: Calculator access denied in settings.')
####DO NOT DELETE OR EDIT. NOT EVEN IF YOU KNOW HOW TOO!!!!####
else:
  messagebox.showerror('wrongpasscode','error wrong password: '+str(loginpass))
####CODE END###
