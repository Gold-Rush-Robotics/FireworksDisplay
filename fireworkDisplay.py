import time
import os
import sys
import playsound

with open("check.txt", "r+") as f:
    if(not f.readline()):
        f.write("RUN")
        os.system("lxterminal --geometry=80x48 --command='python3 fireworkDisplay.py'")
    else:
        class bcolors:
            ENDC = '\033[0m'
            GREEN = '\033[0;32m'
            GOLD = '\033[1;33m'


        text_files = []
        files_exist = True
        folder_name = 'fireworks'
        num_found = 0
        startTime = round(time.time())
        endTime = startTime + 4.9
        goldRushASCII = ["░█▀▀░█▀█░█░░░█▀▄░", "░█▀▄░█░█░█▀▀░█░█░", "░█▀▄░█▀█░█▀▄░█▀█░▀█▀░▀█▀░█▀▀░█▀▀",
                         "░█░█░█░█░█░░░█░█░", "░█▀▄░█░█░▀▀█░█▀█░", "░█▀▄░█░█░█▀▄░█░█░░█░░░█░░█░░░▀▀█",
                         "░▀▀▀░▀▀▀░▀▀▀░▀▀░░", "░▀░▀░▀▀▀░▀▀▀░▀░▀░", "░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀"]

        while files_exist:
            file_name = folder_name + "/" + str(num_found) + ".txt"

            if os.path.isfile(file_name):
                f = open(file_name, "r")
                page = ""
                
                text_files.append(''.join(f.readlines()[5:]))
                num_found += 1
            else:
                files_exist = False

        while True:
            playsound.playsound("fireworkDisplay.mp3", False)
            for text_file in text_files:
                os.system("clear")
                print(text_file)
                for i in [0, 3, 6]:
                    print(
                        f"{bcolors.GREEN}{goldRushASCII[i]}{bcolors.ENDC} {bcolors.GOLD}{goldRushASCII[i + 1]}{bcolors.ENDC} {bcolors.GREEN}{goldRushASCII[i + 2]}{bcolors.ENDC}")

                if(round(time.time()) > endTime):
                    open("check.txt", "w")
                    sys.exit(0)

                time.sleep(.05)

        

