# Importing Tkinter Module
from tkinter import *
from PIL import ImageTk, Image  
from playsound import playsound
import pyttsx3
from gtts import gTTS
import subprocess


playsound("welcome.mp3")

root = Tk()

#Init Tkinter GUI

def app():
        root.title('PyAngela - Bishnudev Khutia')
        root.geometry('800x480')
        root.resizable(False, False)
        root.configure(background='lightpink')

# Adding Fonts, Images and Texts

def userInterface():
    Font_tuple = ("Comic Sans MS", 15, "bold")
    head_Text = Label(root, text='Welcome to PyAngela',bg='lightpink', fg='black',font=('Arial 24')).pack(fill="x")
    user_label = Label(root,image=water_img)
    child_Text = Label(root, text='Type something below !',font=Font_tuple,bg='lightpink',fg='black').place(x=290,y=270)
    user_label.place(x=320,y=60)
    main_Button = Button(root, text='Convert', fg='black',bg='pink', command = text2speech).place(x=380,y=360)
    play_Button = Button(root, text='Reset', fg='black',bg='pink', command = Reset_App).place(x=387,y=400)
    down_Button = Button(root, text='Download',fg='black',bg='pink', command = down_Audio).place(x=375,y=440)

water_img = ImageTk.PhotoImage(Image.open("thumb.png"))
E = Entry(root,width=50)
E.focus_force()
E.pack(side = TOP, ipadx = 30, ipady = 6)
E.pack(anchor = CENTER)
E.place(x=255,y=325)

# Text to Speech Funtion Working

def text2speech():
    global entry
    entry = E.get()
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 2.7)
    engine.setProperty('voice', voices[1].id)
    # engine.say(entry)
    # engine.runAndWait()
    saveAudio()

# Saving the text as a audio file in local machine

def saveAudio():
    new_text = entry
    language = 'en'
    myobj = gTTS(text=new_text, lang=language, slow=False)
    myobj.save("new.mp3")

# Reset the App
def Reset_App():
    # root.destroy()
    E.delete(0, END)
    
# Open the download audio folder

def down_Audio():
    subprocess.Popen(r'explorer /select,"C:\Users\Bishnudev\Dropbox\PC\Desktop\Pyangela\Downloads"')
    # In the subprocess.Popen Function just go to your Tkinter Code directory, copy the path and paste here

#Calling the GUI Function to start the server

app()
userInterface()

# Main Server
root.mainloop()


# Author : Bishnudev Khutia
# Category : Open-Source
# Credit : You have to give me credit XD :)