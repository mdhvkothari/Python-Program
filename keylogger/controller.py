#controlling mouse
#listing to mouse
#controlling keyboard
#listing to keyboard
from pynput.mouse import Controller
from pynput.keyboard import Controller

def mouseController():
    mouse = Controller()
    mouse.position=(100,200)

mouseController()

def keyboardController():
    keyboard = Controller()
    keyboard.type('hello')


keyboardController()
