



# import pythoncom
# context = pythoncom.CreateBindCtx(0)

# running_coms = pythoncom.GetRunningObjectTable()

# monikiers = running_coms.EnumRunning()

# for monikier in monikiers:

#     print('-'*100)
          
#     print(monikier.GetDisplayName(context, monikier))


# import datetime, time
# # print(int(time.time())-11)
# def b(i, j):
#     done = []
#     now = str(datetime.datetime.now())[11:19]
#     now = now.replace(':', '', 2)
#     for num in now:
#         done.append(bin(int(num))[2:].zfill(4))
#     return done[i][j]
# for i in range(4):
#     for j in range(6):
#         print(b(j, i) + '(' + f'{i}, {j}' + ')', end=' ')
#     print('\n')
# import datetime



# def b(r, c):
#     done = []
#     now = str(datetime.datetime.now())[11:19]
#     now = now.replace(':', '', 2)
#     for num in now:
#         done.append(bin(int(num))[2:].zfill(4))
#     return [done[c], done]

# print(b(1, 2))




# stable
    # def b(r, c):
    #     done = []
    #     now = str(datetime.datetime.now())[11:19]
    #     now = now.replace(':', '', 2)
    #     for num in now:
    #         done.append(bin(int(num))[2:].zfill(4))
    #     return [int(done[c][r]), done]




# import subprocess, time, keyboard as kb
# cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# list = set()
# tmr = time.time() - 120
# while 'cat':
#     if time.time() - tmr > 100:
#         for line in proc.stdout:
#             if line.rstrip():
#                 try:
#                     temp = line.decode().rstrip()
#                     if temp != '-----------' and temp != 'Description':
#                         list.add(temp)
#                 except:
#                     pass
#         tmr =  time.time()
#     if kb.is_pressed("F18"):
#         f = open('statistik.txt', 'a')
#         for i in list:
#             f.write(i)
#             f.write(';')
#         f.close
#         break


# from kivy.config import Config
# Config.set('kivy', 'exit_on_escape', '0')

# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.popup import Popup
# from kivy.core.window import Window


# class ChildApp(App):

#     def build(self):
#         Window.bind(on_request_close=self.on_request_close)
#         return Label(text='hehehe')

#     def on_request_close(self, *args):
#         print('stop')
#         return False



# if __name__ == '__main__':
#     ChildApp().run()
# import datetime
# print(str(datetime.datetime.now())[:-7])


# import time
# from datetime import datetime
# tmr = time.time()
# # time.sleep()
# f = open("heh.txt", "a")
# f.write(str(int(time.time() - tmr))+".")
# f.write(datetime.today().strftime('%d-%m-%Y') + '\n')
# f.close()

# import time
# import random
# from datetime import datetime
# for i in range(1):
#     now = datetime.now()
#     f = open("heh.txt", "a")
#     f.write(str(now)[:-7] + '\n')
#     f.close()







# import time, asyncio
# async def f1():
#     print('f11')
#     await asyncio.sleep(3)
#     print('f12')
#     return 'f1_done'
# async def f2():
#     print('f21')
#     await asyncio.sleep(2)
#     print('f22')
#     return 'f2_done'
# async def main():
#     tmr_start = time.time()
    
#     # batch = asyncio.gather(f1(), f2())
#     # t1, t2 = await batch
#     f1_task = asyncio.create_task(f1)
#     f2_task = asyncio.create_task(f2)
#     t1 = await f1_task
#     t2 = await f2_task

#     print(t1)
#     print(t2)
#     tmr_end = time.time()
#     print(int(tmr_end - tmr_start))
    
# if __name__ == "__main__":
#     asyncio.run(main())
# import threading, subprocess, keyboard as kb, sys, time



# list = set()
# def get_apps(list):
#     for _ in range(4):
#         cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
#         proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#         for line in proc.stdout:
#             if line.rstrip():
#                 try:
#                     temp = line.decode().rstrip()
#                     if temp != '-----------' and temp != 'Description':
#                         list.add(temp)
#                 except:
#                     pass
#         print(list)
#         time.sleep(5)

# def f1():
#     f = open('uwu.txt', 'a')
#     f.write('adfsjkl;')
#     f.close()
#     for i in range(100000):
#         # print(f'_{int(i/100)}')
#         print(i)
# def f2():
#     for i in range(100000):
#         if i > 40000:
#             sys.exit()
#             print('\n')
#             break
#         print(f'_{int(i/100)}\r', end='')
# def f3():
#     if kb.is_pressed("F18"):
#         sys.exit()
# thread2 = threading.Thread(target=f1)
# thread = threading.Thread(target=get_apps(list))
# thread2.start()
# thread.start()

# def n1():
#     # for i in range(50):
#     #     print('n')
#     #     time.sleep(0.2)
#     print(11)
#     time.sleep(2)
#     print(12)
# def n2():
#     # for i in range(20):
#     #     print(i)
#     #     time.sleep(0.5)
#     print(21)
#     time.sleep(3)
#     print(22)
# thread1 = threading.Thread(target=n1)
# thread2 = threading.Thread(target=n2)
# thread1.start()
# thread2.start()



# for i in range(10):
#     print(str(i) + '\r', end='')
#     time.sleep(0.1)



# startfile
# import os
# def startfile(filename):
#   try:
#     os.startfile(filename)
#   except:
#     print(1)
# startfile('D:\delete')





# print('hello world')





# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.clock import Clock
# from datetime import datetime

# class TimeApp(App):
#     def build(self):
#         self.time_label = Label(text=datetime.now().strftime('%H:%M:%S'))
#         Clock.schedule_interval(self.update_time, 1)
#         return self.time_label

#     def update_time(self, dt):
#         self.time_label.text = datetime.now().strftime('%H:%M:%S')

# if __name__ == '__main__':
#     TimeApp().run()





'''

import serial, time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

arduino = serial.Serial(port='COM5',   baudrate=115200, timeout=.1)

# def send_to_com_port(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data

# while True:
# num = input("Enter a number: ")
# value = send_to_com_port(num)
# print(value)



class MyApp(App):
    flag = False
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Press me!', font_size=24)
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)
        return self.layout


    def on_button_press(self, instance):
        arduino.write(bytes(str(int(self.flag)), 'utf-8'))
        self.flag = not self.flag



if __name__ == '__main__':
    MyApp().run()
# print(int(not 1))
'''






# import random 
# s = [random.randint(1, 40) for _ in range(10)]
# max = 1
# pre_max = 0 
# for i in s:
#     if i > max:
#         pre_max = max
#         max = i
# print(sort(s), '\n', max, pre_max)




# def transferTime(line):
#     ln = line.split()[1]
#     sum = int(ln[0:2]) * 3600 + int(ln[3:5]) * 60 + int(ln[6:8])
#     ans = [sum, ln[-2:]]
#     return ans


# def compareTime(tm1, tm2):
#     if tm1[1] == tm2[1]:
#         diff = tm2[0] - tm1[0]
#     else:
#         diff = 86400 - tm1[0] + tm2[0]
#     if diff > 900:
#         return False
#     return True

# line = '465;2024-12-23 20:12:42;2024-12-23 20:20:27;Windows Explorer,Telegram Desktop,Visual Studio Code,Firefox,Python,Setup/Uninstall,'

# print(transferTime(line))

 
# tm1 = '79;2024-12-23 23:59:59;2024-12-25 00:04:42;Setup/Uninstall,'
# tm2 = '79;2024-12-25 00:00:01;2024-12-25 00:04:42;Setup/Uninstall,'

# print(n[n.find(';', n.find(';')+1):])

# print(n.split(';')[1])


# DIFF_TIME = 100

# def compareTime(tm1, tm2):

#         def transferTime(line):
#             try:
#                 ln = line.split(';')[1]
#                 sum = int(ln[11:13]) * 3600 + int(ln[14:16]) * 60 + int(ln[17:20])
#                 ans = [sum, int(ln[5:7] + ln[8:10])] #summ and day
#                 return ans
#             except:
#                  return -1
#         tm1 = transferTime(tm1)
#         tm2 = transferTime(tm2)
        
#         if tm1 == -1 or tm2 == -1:
#              return True
        
#         if tm1[1] == tm2[1]:
#             diff = tm2[0] - tm1[0]
#         elif tm2[1] - tm1[1] == 1:
#             diff = 86400 - tm1[0] + tm2[0]
#         else:
#             return True
#         if diff > DIFF_TIME:
#             return True
#         return False

# print(compareTime(tm1, tm2))





# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from pystray import Icon, Menu, MenuItem
# import PIL.Image 

# class MyApp(App):
#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         label = Label(text='Hello, world!')
#         button = Button(text='Click me!')
#         layout.add_widget(label)
#         layout.add_widget(button)
#         return layout

#     def on_start(self):
#         menu = Menu(
#             MenuItem('Show/Hide', self.toggle_visibility),
#             MenuItem('Exit', self.stop)
#         )
#         icon = Icon('My App', menu=menu)
#         image = PIL.Image.open("D:/3VERGIVEN/common folder/python/projects/statistic/in_process/app_on_kivy\pict.png")

#         icon.run()

#     def toggle_visibility(self):
#         self.root.opacity = 1 if self.root.opacity == 0 else 0

#     def stop(self):
#         icon.stop()
#         App.get_running_app().stop()

# if __name__ == '__main__':
#     MyApp().run()




# if 1:
#   print(1)
# if 2:
#   print(2)
# if 0:
#   print(0)

# if 1:
#   print(1)
# else:
#   print(2)



# a = "mega_delete.txt"

# f = open(a, "a")
# f.write("hehehe")
# f.close()
import datetime
# print(datetime.datetime.now())




















































































































































































