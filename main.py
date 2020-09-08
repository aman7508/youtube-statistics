import urllib
from tkinter import *
from urllib.request import *
import json

key = "AIzaSyDdtK3inh5lA5qUO6t33Rdl6qYgNI8mniI"


def channel_data():
    name = e1.get()
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + name + "&key=" + key).read()

    sub = json.loads(data)['items'][0]["statistics"]["subscriberCount"]
    total_view = json.loads(data)['items'][0]["statistics"]["viewCount"]
    total_videos = json.loads(data)['items'][0]["statistics"]["videoCount"]
    l2.config(text=sub)
    l4.config(text=total_view)
    l6.config(text=total_videos)


root = Tk()
root.geometry("800x400+200+50")
root.configure(bg="#262626")
channel_name = StringVar()
e1 = Entry(root, textvariable=channel_name)
e1.grid(row=1, column=2)
b1 = Button(root, text="CLICK",fg="black",activebackground="green", command=channel_data)
b1.grid(row=2, column=2)

l1 = Label(root, text="Total number of subscriber:", font="times 15 bold",bg="goldenrod1")
l1.grid(row=4, column=1)
l2 = Label(root, font="times 15 bold")
l2.grid(row=4, column=3)

l3 = Label(root, text="Total number of view:", font="times 15 bold",bg="red")
l3.grid(row=6, column=1)
l4 = Label(root, font="times 15 bold",bg="pink")
l4.grid(row=6, column=3)

l5 = Label(root, text="Total number of videos:", font="times 15 bold")
l5.grid(row=8, column=1)
l6 = Label(root, font="times 15 bold")
l6.grid(row=8, column=3)

root.mainloop()
