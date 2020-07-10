import subprocess
from datetime import datetime
import os
import caffeine
import osascript

hour = input("Hour: ")
minute = input("Minute: ")
sleep = input("Display Sleep?:" )


def sleep_computer():
    os.system('pmset displaysleepnow')
    caffeine.on(display=False)


if sleep == "j":
    sleep_computer()

if sleep == "n":
    current_time = datetime.now()
    if 0 <= int(current_time.strftime("%H")) <= 3:
        print("Gehe bitte bald schlafen")
    else:
        print("ok!")


current_time = datetime.now()


while True:

    current_time = datetime.now()
    if (current_time.strftime("%H") == hour) and (current_time.strftime("%M") == minute):
        osascript.osascript("set volume output volume 100")
        subprocess.call(
            ["afplay", "Your Song (Complete Path).mp3"])
        applescript = """
        display dialog "Good morning. Hope you slept well" ¬
        with title "Wake up timer" ¬
        buttons {"OK"}
        """
        subprocess.call("osascript -e '{}'".format(applescript), shell=True)
