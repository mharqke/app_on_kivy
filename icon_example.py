






import pystray
import PIL.Image 

image = PIL.Image.open("D:/3VERGIVEN/common folder/python/projects/statistic/in_process/app_on_kivy/pict.png")


def on_clicked(icon, item):
    if str(item) == "say hello":
        print("hollo world")
    elif str(item) == "Exit":
        icon.stop()
    elif str(item) == 'subitem 2':
        print('subitem 2')
    elif str(item) == 'subitem 1':
        print('subitem 1')

icon = pystray.Icon("pict", image, menu=pystray.Menu(
    pystray.MenuItem("say hello", on_clicked),
    pystray.MenuItem("Exit", on_clicked),
    pystray.MenuItem("submenu", pystray.Menu(
        pystray.MenuItem("subitem 1", on_clicked),
        pystray.MenuItem("subitem 2", on_clicked),
    ))
))



icon.run()
















































































































