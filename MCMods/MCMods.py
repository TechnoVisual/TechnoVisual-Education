#!/usr/bin/python3

# Setup our modules
from tkinter import *
from tkinter import messagebox
import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image, ImageTk
import microbit
import threading
import sys

# create the instance of Tk for our window
root = Tk()
# set our Minecraft connection variable as global
mc = None
tkcontrols = []

# make some global string variables so that we can alter the text
connectText = StringVar()
connectText.set("Not Connected")
connectButText = StringVar()
connectButText.set("Connect")
inputBox = None
microBitCheck = IntVar()
exitMB = False

optionsCombo = StringVar(root)

def client_exit():
    exit()

def change_dropdown(*args):
    global mc, inputBox
    if(optionsCombo.get() == "Make Block"):
        inputBox.delete(1.0, END)
        inputBox.insert(END,"pos = mc.player.getTilePos()\nmc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)")
    if(optionsCombo.get() == "Make TNT"):
        inputBox.delete(1.0, END)
        inputBox.insert(END,"pos = mc.player.getTilePos()\nmc.setBlock(pos.x+3, pos.y, pos.z, block.TNT.id, 1)")
    if(optionsCombo.get() == "Flatten Area"):
        inputBox.delete(1.0, END)
        inputBox.insert(END,"pos = mc.player.getTilePos()\nmc.setBlocks(pos.x-10, pos.y-1, pos.z-10, pos.x+10, pos.y+10, pos.z+10, block.AIR.id)")
    if(optionsCombo.get() == "Teleport"):
        inputBox.delete(1.0, END)
        inputBox.insert(END,"pos = mc.player.getPos()\nmc.player.setPos(pos.x, pos.y+20, pos.z)")
    if(optionsCombo.get() == "Chat"):
        inputBox.delete(1.0, END)
        inputBox.insert(END,'pos = mc.postToChat("Hello Minecraft")')

def clicked():
    global connectText,connectButText, mc
    if connectText.get() == "Not Connected":
        mc = minecraft.Minecraft.create()
        connectText.set("Connected")
        connectButText.set("Disconnect")
        mc.postToChat("Mindcraft Mods Connected")
    else:
        mc.postToChat("Mindcraft Mods Disconnected")
        mc = None
        connectText.set("Not Connected")
        connectButText.set("Connect")

def runclicked():
    global inputBox,mc
    if(mc == None):
        messagebox.showerror("Not Connected", "There is no connection to the Minecraft Game. Press the Connect button to make a connection.")
    else:
        code = inputBox.get(1.0,END)
        try:
            exec(code)
        except:
            messagebox.showerror("Error", "There is an error in your code. Please check and try again.")

def setupInterface(root):
    global optionsCombo,inputBox,microBitCheck
    root.title("Minecraft Modding")
    backpng = Image.open("images/ModBackground.png")
    backimg = ImageTk.PhotoImage(backpng)
    backlbl = Label(root,image=backimg)
    backlbl.image = backimg
    backlbl.place(x=0,y=0)
    choices = { 'Make Block','Teleport','Flatten Area','Make TNT','Chat'}
    optionsCombo.set('Click to select') # set the default option
    pum1 = popupMenu = OptionMenu(root, optionsCombo, *choices, command=change_dropdown)
    lbl1 = Label(root, text="Choose Action")
    lbl1.place(x=20,y=130)
    pum1.place(x=20,y=150)
    lbl2 = Label(root, textvariable=connectText)
    lbl2.place(x=180,y=50)
    but1 = Button(root, textvariable=connectButText, command=clicked)
    but1.place(x=180,y=20)
    lbl3 = Label(root, justify=LEFT, text="import mcpi.minecraft as minecraft\nimport mcpi.block as block\nmc = minecraft.Minecraft.create()")
    lbl3.place(x=180,y=103)
    inputBox = Text(root, width=85, height=9)
    inputBox.place(x=180,y=150)
    inputBox.insert(END,"")
    runbut = Button(root, text="Run Code", command=runclicked)
    runbut.place(x=20,y=250)
    mbCheck = Checkbutton(root, text="action with micro:bit", variable=microBitCheck)
    mbCheck.place(x=20,y=220)

def microbitLoop():
    while True:
        if(exitMB == True):
            sys.exit()
        if(microbit.button_a.was_pressed() and microBitCheck.get() == 1):
            runclicked()
        microbit.sleep(200)

setupInterface(root)        

root.geometry("800x300+0+0")

mbThread = threading.Thread(target=microbitLoop)
mbThread.start()

root.mainloop()

exitMB = True
    
