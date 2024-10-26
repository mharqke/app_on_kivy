



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





print('hello world')





























































































































































































































































