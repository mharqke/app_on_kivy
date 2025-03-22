

import os
import sys
import time
import pystray
import datetime 
import threading
import subprocess
import tkinter as tk
from PIL import Image, ImageDraw
from pystray import MenuItem, Icon



STAT_FREQUENCY = 10 * 60
DIFF_TIME = 1000

class Statistic():
    # i.e.
    # temp_file = "t_only_stat.txt"
    # main_file = "m_only_stat.txt"
    # logs_file = "logs.txt"
    temp_file = ""
    main_file = ""
    logs_file = ""

    def __init__(self, temp_file, main_file, logs_file):
        self.temp_file = temp_file
        self.main_file = main_file
        self.logs_file = logs_file


    def write_to_logs(self, info):
        print("lf: ", self.logs_file)
        if os.path.exists(self.logs_file):
            f = open(self.logs_file, "a")
            f.write(str(datetime.datetime.now())[:-7] + ':' + info + '\n')
            f.close()
        else:
            f = open(self.logs_file, "w")
            f.write("logs for \"only_time_stat.py\"\n")
            f.write(str(datetime.datetime.now())[:-7] + ':' + info + '\n')
            f.close()

    
    def compareTime(tm1, tm2):

            def transferTime(line):
                try:
                    ln = line.split(';')[1]
                    sum = int(ln[11:13]) * 3600 + int(ln[14:16]) * 60 + int(ln[17:20])
                    ans = [sum, int(ln[5:7] + ln[8:10])] #[summ, day]
                    return ans
                except:
                    return -1
            tm1 = transferTime(tm1)
            tm2 = transferTime(tm2)
            
            if tm1 == -1 or tm2 == -1:
                return True
            
            if tm1[1] == tm2[1]:
                diff = tm2[0] - tm1[0]
            elif tm2[1] - tm1[1] == 1:
                diff = 86400 - tm1[0] + tm2[0]
            else:
                return True
            if diff > DIFF_TIME:
                return True
            return False
    

    def rem_temp_file(self, temp, main): #write data from temporary file to main file
        if os.path.exists(temp):
            DataNow = self.returnDataNow()
            # for example
            # DataNow = 0;2024-12-25 01:05:17;2024-12-25 01:05:17,
            
            list_from_temp = [x for x in open(temp)]
            if len(list_from_temp):
                last = list_from_temp[-1]
                # for example
                # last = "24;2024-12-25 01:00:43;2024-12-25 01:01:07"
                if Statistic.compareTime(last, DataNow):
                    f = open(main, "a")
                    f.write(last)
                    f.close()
                    os.remove(temp)
                    self.write_to_logs("start a new session")
                else:
                    f = open(temp, "a")
                    # DataNow = last[:last.find(';')] + DataNow[int(DataNow[DataNow.find(';'):])] 
                    f.write(DataNow)
                    f.write('\n')
                    f.close() 
                    self.tmr_begin = int(time.time()) - int(last[:last.find(';')]) - STAT_FREQUENCY
                    self.date_begin = last.split(';')[1]
                    self.write_to_logs("last session was continued")
            else:
                os.remove(temp)
                self.write_to_logs("t_only_stat.txt is bad")


    def get_apps(list): #return array of running apps
        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if line.rstrip():
                try:
                    temp = line.decode().rstrip()
                    if temp != '-----------' and temp != 'Description':
                        list.add(temp)
                except:
                    pass
        return list


    def begin(self):

        self.tmr_begin = int(time.time()) 
        self.date_begin = str(datetime.datetime.now())[:-7]
        self.apps_list = set()
        Statistic.rem_temp_file(self, self.temp_file, self.main_file)


    def returnDataNow(self):

        line = str(int(time.time()) - self.tmr_begin) + ';'
        line += self.date_begin + ';'
        line += str(datetime.datetime.now())[:-7]
        # self.apps_list = Statistic.get_apps(self.apps_list)
        # for app in self.apps_list:
        #     line += app + ','
        return line
        

    def on_request_close(self, *args): 
        # only for Statistic
        #code here runs when you try to close window
        #but in normal situation this shouldn't happen 
        f = open(f'{self.temp_file}', "a")
        f.write(Statistic.returnDataNow(self))
        f.write('\n')
        f.close()
        self.write_to_logs("was manualy closed")
        


    def update(self):
        f = open(f'{self.temp_file}', "a")
        f.write(Statistic.returnDataNow(self))
        f.write('\n')
        f.close()





uwu = Statistic("t_only_stat.txt", "m_only_stat.txt", "logs.txt")
uwu.begin()
uwu.update()


def infinite_loop():
    while 'meow':
        uwu.update()
        time.sleep(STAT_FREQUENCY)


def on_exit(icon, item):
    uwu.on_request_close()
    icon.stop()
    window.after(0, window.deiconify)
    window.quit()


def show_window(icon, item):
    window.after(0, window.deiconify)


def withdraw_window():
    window.withdraw()


image = Image.open("D:/3VERGIVEN/common folder/python/projects/statistic/app_on_kivy/pict.png")


icon = Icon("test_icon", image, "My Tray Icon", menu=pystray.Menu(
    MenuItem('Show', show_window),
    MenuItem("Exit", on_exit)
))


threading.Thread(target=infinite_loop, daemon=True).start()


icon.run_detached()

def show_stat():
    print("1test220325")

def open_setting():
    print("2test220325")

window = tk.Tk()
window.title("Welcome")
window.geometry('180x200')
window.protocol('WM_DELETE_WINDOW', withdraw_window)

button1 = tk.Button(window, 
    text="show stat",
    command=show_stat
)
button1.pack(padx=40, pady=25)

button2 = tk.Button(window, 
    text="show setting",
    command=open_setting
)
button2.pack(padx=40, pady=25)

window.withdraw()
window.mainloop()






























































































































































































































































































































