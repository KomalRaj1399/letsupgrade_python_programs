from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('700x200')
root.title('Youtube Video Downloader')


Label_1=Label(root,text="Paste The Youtube Link Here", font=("bold",20),)
Label_1.place(x=140,y=20)


mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140, y=80)

#https://www.youtube.com/watch?v=ALZHF5UqnU4

def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
   # if not os.path.exists('C:\Users\dell\Desktop\AUDIO PLATFORMS'):
    #   os.makedirs('C:\Users\dell\Desktop\AUDIO PLATFORMS')
    ytvideo.download(r'C:\Users\dell\Desktop\AUDIO PLATFORMS') 

Button(root,text="Download Video", width=20, bg='green',fg="white", command=downloadVideo).place(x=280, y=110)

root.mainloop()
