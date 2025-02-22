import datetime, time, subprocess, os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *
from random import randint
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Config.set('kivy', 'exit_on_escape', '0')
Builder.load_file('back.kv')

STAT_FREQUENCY = 480
DIFF_TIME = 1000


class Cell(Widget):
    colors = [(0, 120, 150, 1), (0, 128, 0, 1), (150, 86, 0, 1),(200, 0 ,200, 1)]
    columns = [['', ()], ['', ()], ['', ()], ['', ()], ['', ()], ['', ()]]
    def time(self, c, r):
        def b(r):
            done = []
            now = str(datetime.datetime.now())[11:19]
            now = now.replace(':', '', 2)
            for num in now:
                done.append(bin(int(num))[2:].zfill(4))
            return done[r]
        if b(r) != self.columns[r][0]:
            self.columns[r][0] = b(r)
            temp_color = (self.colors[randint(0, len(self.colors)-1)])
            while temp_color == self.columns[r][1] or temp_color == self.columns[r-1][1]:
                temp_color = (self.colors[randint(0, len(self.colors)-1)])
            self.columns[r][1] = temp_color
        if int(b(r)[c]):
            self.color = self.columns[r][1]           
        else:
            self.color = (1,1,1,1/20)

class Statistic(Widget):
    temp_file = "temp_stat.txt"
    main_file = "main_stat.txt"

    
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
            DataNow = Statistic.returnDataNow(self)
            # for example
            # DataNow = 0;2024-12-25 01:05:17;2024-12-25 01:05:17;a,p,p,s,
            try:
                last = [x for x in open(temp)][-2]
                # for example
                # last = "24;2024-12-25 01:00:43;2024-12-25 01:01:07;a,p,p,s,"
                if Statistic.compareTime(last, DataNow):
                    print(0)
                    f = open(main, "a")
                    f.write(last)
                    f.close()
                    os.remove(temp)
                else:
                    print(1)
                    f = open(temp, "a")
                    # DataNow = last[:last.find(';')] + DataNow[int(DataNow[DataNow.find(';'):])] 
                    f.write(DataNow)
                    f.write('\n')
                    f.close() 
                    self.tmr_begin = int(time.time()) - int(last[:last.find(';')]) - STAT_FREQUENCY
                    self.date_begin = last.split(';')[1]
                
            except:
                print(2)
                os.remove(temp)


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

        Window.bind(on_request_close=self.on_request_close)
        Statistic.rem_temp_file(self, self.temp_file, self.main_file)
        

    def returnDataNow(self):

        line = ''
        line += str(int(time.time()) - self.tmr_begin) + ';'
        line += self.date_begin + ';'
        line += str(datetime.datetime.now())[:-7] + ';'
        self.apps_list = Statistic.get_apps(self.apps_list)
        for app in self.apps_list:
            line += app + ','
        return line
        

    def on_request_close(self, *args): #code here runs when you try to close window
        
        f = open(f'{self.temp_file}', "a")
        f.write(Statistic.returnDataNow(self))
        f.write('\n')
        f.close()
        return False


    def update(self, dt):  #code here run (in loop?)

        f = open(f'{self.temp_file}', "a")
        f.write(Statistic.returnDataNow(self))
        f.write('\n')
        f.close()




class BinaryClock(Widget):
    tmr_label = time.time()
    # create objects
    cell1 = ObjectProperty(None)
    cell2 = ObjectProperty(None)
    cell3 = ObjectProperty(None)
    cell4 = ObjectProperty(None)
    cell5 = ObjectProperty(None)
    cell6 = ObjectProperty(None)
    cell7 = ObjectProperty(None)
    cell8 = ObjectProperty(None)
    cell9 = ObjectProperty(None)
    cell10 = ObjectProperty(None)
    cell11 = ObjectProperty(None)
    cell12 = ObjectProperty(None)
    cell13 = ObjectProperty(None)
    cell14 = ObjectProperty(None)
    cell15 = ObjectProperty(None)
    cell16 = ObjectProperty(None)
    cell17 = ObjectProperty(None)
    cell18 = ObjectProperty(None)
    cell19 = ObjectProperty(None)
    cell20 = ObjectProperty(None)


    def begin(self): #code here run once

        Window.size = (300, 400)
        x = Window.size[0]/2
        y = Window.size[1]/2
        m = min(Window.size)
        xt = m/10
        yt = m/10
        self.cell1.pos = (x-xt*3,  y-yt*1.5)
        self.cell2.pos = (x-xt*2,  y-yt*1.5)
        self.cell3.pos = (x-xt,    y-yt*1.5)
        self.cell4.pos = (x,       y-yt*1.5)
        self.cell5.pos = (x+xt,    y-yt*1.5)
        self.cell6.pos = (x+xt*2,  y-yt*1.5)
        self.cell7.pos = (x-xt*3,   y-yt/2)
        self.cell8.pos = (x-xt*2,   y-yt/2)
        self.cell9.pos = (x-xt,     y-yt/2)
        self.cell10.pos = (x,       y-yt/2)
        self.cell11.pos = (x+xt,    y-yt/2)
        self.cell12.pos = (x+xt*2,  y-yt/2)
        self.cell13.pos = (x-xt*2, y+yt/2)
        self.cell14.pos = (x-xt,   y+yt/2)
        self.cell15.pos = (x,      y+yt/2)
        self.cell16.pos = (x+xt,   y+yt/2)
        self.cell17.pos = (x+xt*2, y+yt/2)
        self.cell18.pos = (x-xt*2,  y+yt*1.5)
        self.cell19.pos = (x,       y+yt*1.5)
        self.cell20.pos = (x+xt*2,  y+yt*1.5)
        xt-=3
        yt-=3
        # update all objects
        self.cell1.size = (xt, yt)
        self.cell2.size = (xt, yt)
        self.cell3.size = (xt, yt)
        self.cell4.size = (xt, yt)
        self.cell5.size = (xt, yt)
        self.cell6.size = (xt, yt)
        self.cell7.size = (xt, yt)
        self.cell8.size = (xt, yt)
        self.cell9.size = (xt, yt)
        self.cell10.size = (xt, yt)
        self.cell11.size = (xt, yt)
        self.cell12.size = (xt, yt)
        self.cell13.size = (xt, yt)
        self.cell14.size = (xt, yt)
        self.cell15.size = (xt, yt)
        self.cell16.size = (xt, yt)
        self.cell17.size = (xt, yt)
        self.cell18.size = (xt, yt)
        self.cell19.size = (xt, yt)
        self.cell20.size = (xt, yt)
        self.cell1.time(3,0)
        self.cell2.time(3,1)
        self.cell3.time(3,2)
        self.cell4.time(3,3)
        self.cell5.time(3,4)
        self.cell6.time(3,5)
        self.cell7.time(2,0)
        self.cell8.time(2,1)
        self.cell9.time(2,2)
        self.cell10.time(2,3)
        self.cell11.time(2,4)
        self.cell12.time(2,5)
        self.cell13.time(1,1)
        self.cell14.time(1,2)
        self.cell15.time(1,3)
        self.cell16.time(1,4)
        self.cell17.time(1,5)
        self.cell18.time(0,1)
        self.cell19.time(0,3)
        self.cell20.time(0,5)


    def update(self, dt):  #code here run (in loop?)

        x = Window.size[0]/2
        y = Window.size[1]/2
        m = min(Window.size)
        xt = m/10
        yt = m/10
        self.cell1.pos = (x-xt*3,   y-yt*1.5)
        self.cell2.pos = (x-xt*2,   y-yt*1.5)
        self.cell3.pos = (x-xt,    y-yt*1.5)
        self.cell4.pos = (x,       y-yt*1.5)
        self.cell5.pos = (x+xt,    y-yt*1.5)
        self.cell6.pos = (x+xt*2,   y-yt*1.5)
        self.cell7.pos = (x-xt*3,  y-yt/2)
        self.cell8.pos = (x-xt*2,  y-yt/2)
        self.cell9.pos = (x-xt,   y-yt/2)
        self.cell10.pos = (x,     y-yt/2)
        self.cell11.pos = (x+xt,  y-yt/2)
        self.cell12.pos = (x+xt*2, y-yt/2)
        self.cell13.pos = (x-xt*2,   y+yt/2)
        self.cell14.pos = (x-xt,    y+yt/2)
        self.cell15.pos = (x,       y+yt/2)
        self.cell16.pos = (x+xt,    y+yt/2)
        self.cell17.pos = (x+xt*2,   y+yt/2)
        self.cell18.pos = (x-xt*2,  y+yt*1.5)
        self.cell19.pos = (x,      y+yt*1.5)
        self.cell20.pos = (x+xt*2,  y+yt*1.5)
        xt-=3
        yt-=3
        # update all objects
        self.cell1.size = (xt, yt)
        self.cell2.size = (xt, yt)
        self.cell3.size = (xt, yt)
        self.cell4.size = (xt, yt)
        self.cell5.size = (xt, yt)
        self.cell6.size = (xt, yt)
        self.cell7.size = (xt, yt)
        self.cell8.size = (xt, yt)
        self.cell9.size = (xt, yt)
        self.cell10.size = (xt, yt)
        self.cell11.size = (xt, yt)
        self.cell12.size = (xt, yt)
        self.cell13.size = (xt, yt)
        self.cell14.size = (xt, yt)
        self.cell15.size = (xt, yt)
        self.cell16.size = (xt, yt)
        self.cell17.size = (xt, yt)
        self.cell18.size = (xt, yt)
        self.cell19.size = (xt, yt)
        self.cell20.size = (xt, yt)
        self.cell1.time(3,0)
        self.cell2.time(3,1)
        self.cell3.time(3,2)
        self.cell4.time(3,3)
        self.cell5.time(3,4)
        self.cell6.time(3,5)
        self.cell7.time(2,0)
        self.cell8.time(2,1)
        self.cell9.time(2,2)
        self.cell10.time(2,3)
        self.cell11.time(2,4)
        self.cell12.time(2,5)
        self.cell13.time(1,1)
        self.cell14.time(1,2)
        self.cell15.time(1,3)
        self.cell16.time(1,4)
        self.cell17.time(1,5)
        self.cell18.time(0,1)
        self.cell19.time(0,3)
        self.cell20.time(0,5)

class ClockApp(App):


    def __init__(self):
        super().__init__()
        self.label = Label(text=str(int(time.time() - BinaryClock.tmr_label))) # show time


    def build(self):
        box = BoxLayout(orientation='vertical') #layout, which consist other objects
        clock = BinaryClock() #binary clock
        clock.begin()
        box.add_widget(clock) #put clock in box
        stat = Statistic()
        stat.begin()
        box.add_widget(stat)
        box.add_widget(self.label) #put label in box
        Clock.schedule_interval(clock.update, 1)
        Clock.schedule_interval(stat.update, STAT_FREQUENCY)
        Clock.schedule_interval(self.update_time, 1)
        return box
    

    def update_time(self, dt): 
        tm = time.time() - BinaryClock.tmr_label #how many seconds have passed since start
        text = str(int(tm//3600)).zfill(2) + ' : ' + str(int((tm%3600)//60)).zfill(2) + ' : ' + str(int(tm%60)).zfill(2)
        self.label.text = text


if __name__ == '__main__':
    ClockApp().run()

































