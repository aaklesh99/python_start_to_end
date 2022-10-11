from  pygame import mixer
import datetime
from time import time
def musicOnLoop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    # mixer.stop()
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("MyLog.txt", "a") as f:
        f.write(f"{msg} { datetime.datetime.now() }")


if __name__ == '__main__':
    # musicOnLoop('water.mp3',"stop")
    init_water = time()
    init_eye = time()
    init_exercise = time()
    waterexec = 5
    eyeexec= 10
    bodyexec =15

    while True:
        if time() - init_water > waterexec:
            print("Water drinking time, Enter drank to stop")
            musicOnLoop('water.mp3', "drank")
            init_water = time()
            log_now("Drank water at")
        if time() - init_eye > bodyexec:
            print("Eye exercise time, Enter eyedone to stop")
            musicOnLoop('water.mp3', "eyedone")
            init_water = time()
            log_now("Eye exercise done  at")
        if time() - init_exercise > bodyexec:
            print("Body exercise time, Enter donephy to stop")
            musicOnLoop('water.mp3', "donephy")
            init_water = time()
            log_now("Physical exercise done  at")
