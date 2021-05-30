from tkinter import *
import time
import datetime
from pynput.keyboard import Key, Controller
import pynput\
    .mouse
keyboard = Controller()
mouse = pynput.mouse.Controller()

scrollInt = 1

def scr():
    global scrollInt
    scrollInt = scrollInt + 1

def rightClick():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    inputter+1

def cztertrzy():
    for i in range(0, 43):
        mouse.scroll(0, -1)
        time.sleep(0.6)
    scr()

def wejdz():
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    mouse.position = (350, 350)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)

def startMe():
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    time.sleep(1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    mouse.position = (350, 350)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    time.sleep(2)
    #cztertrzy()
    for i in range (0, 75):
        mouse.scroll(0,-1)
        time.sleep(0.2)
    for i in range (0, scrollInt):
        mouse.scroll(0,-1)
        time.sleep(0.5)
    time.sleep(0.5)

    scr()
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(8)
    keyboard.press('p')
    keyboard.release('p')
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(10)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)

def lol():
    mouse.position = (160, 780)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

lol()
#wejdz()
time.sleep(1)
for i in range(0,212):
    startMe()


