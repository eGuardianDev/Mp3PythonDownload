import tkinter as tk
from tkinter import *
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable
import os
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox 


root = Tk()
root.title("Youtube mp3 donwloader")


Lb = Listbox(root)
Lb.pack()

def add():
 r = requests.get(urlBox.get())
 urlBox.delete(0,END);
 soup = BeautifulSoup(r.text)
 
 link = soup.find_all(name="title")[0]
 title = str(link)
 title = title.replace("<title>","")
 title = title.replace("</title>","")
 List.append(str(urlBox.get()))
 print(title)
 Lb.insert(0,title)

List =[]
def delete():
    #delete from Listbox
    selection = Lb.curselection()
    print(len(List));
    print(selection[0]);
    List.pop(len(List) -1 - selection[0]);
    Lb.delete(selection)
    #delete from list
    #value = eval(list_of_fruit.get(selection))
    #fruit.remove(value)'

def Download():
 count =0
 print("Downloading: ")
 for i in range (len(List)):
  try:   
     yt = YouTube(List[i])
     if yt.check_availability() == False:
      print("error")
      return 1
  except VideoUnavailable:
     print(f'Video is unavaialable, skipping.')
     return 2
  except:
     print("Error occured when reading video url")
     return 3
  else: 
     print(yt.title)
     video = yt.streams.filter(only_audio=True).first()
     destination = '.'
     out_file = video.download(output_path=destination)
     
     base, ext = os.path.splitext(out_file)
     new_file = base + '.mp3'
     os.rename(out_file, new_file)
     print(yt.title + " has been successfully downloaded.")
     count +=1
 return count
 
w = Label(root, text='Youtube mp3 downlaoder')
w.pack()


Label(root, text='url').pack()
urlBox = Entry(root)
urlBox.pack()

button = Button(root, text='Add', width=25, command=add)
button.pack() 
button = Button(root, text='Remove', width=25, command=delete)
button.pack() 

def MessageBoxDownload():
 answer= messagebox.askquestion("Are you sure?", "Are you sure you want to start downloading all the songs?") 
 print("Downloading - you selected: ", answer)
 if(answer == "yes"):
   print(List);
   count = Download()
   print("done..");
   if(count > 0):
    message ="Downloaded {0} mp3 files".format(count);
    messagebox.showinfo("Done.", message)
   else: 
    messagebox.showerror("Fail.", "For some reason, none of the videos were downloaded")
button = Button(root, text='Download All', width=25, command=MessageBoxDownload)
button.pack() 


button = Button(root, text='Exit', width=25, command=root.destroy)
button.pack() 



root.mainloop()


