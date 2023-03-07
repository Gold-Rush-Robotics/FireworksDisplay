import time
import os
import sys
import playsound


cols = os.system('tput cols')
rows = os.system('tput lines')
print(cols, rows)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=48, cols=80))


class bcolors:
    ENDC = '\033[0m'
    GREEN = '\033[0;32m'
    GOLD = '\033[1;33m'


text_files = []
files_exist = True
folder_name = 'fireworks'
num_found = 0
startTime = round(time.time())
endTime = startTime + 5
goldRushASCII = ["░█▀▀░█▀█░█░░░█▀▄░", "░█▀▄░█░█░█▀▀░█░█░", "░█▀▄░█▀█░█▀▄░█▀█░▀█▀░▀█▀░█▀▀░█▀▀",
                 "░█░█░█░█░█░░░█░█░", "░█▀▄░█░█░▀▀█░█▀█░", "░█▀▄░█░█░█▀▄░█░█░░█░░░█░░█░░░▀▀█",
                 "░▀▀▀░▀▀▀░▀▀▀░▀▀░░", "░▀░▀░▀▀▀░▀▀▀░▀░▀░", "░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀"]

while files_exist:
    file_name = folder_name + "/" + str(num_found) + ".txt"

    if os.path.isfile(file_name):
        f = open(file_name, "r")
        text_files.append(f.read())
        num_found += 1
    else:
        files_exist = False

while round(time.time()) < endTime:
    playsound.playsound("fireworkDisplay.mp3")
    for text_file in text_files:
        for i in [0, 3, 6]:
            print(
                f"{bcolors.GREEN}{goldRushASCII[i]}{bcolors.ENDC} {bcolors.GOLD}{goldRushASCII[i + 1]}{bcolors.ENDC} {bcolors.GREEN}{goldRushASCII[i + 2]}{bcolors.ENDC}")

        print(text_file)

        time.sleep(.05)
