import ntpath
import pyttsx3  # pip install pyttsx3
import pyaudio  # pip install pyaudio
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib   #pip install smtplib
import pywhatkit as kit #pip install pywhatkit
import sys
from requests import get #pip install requests
import tkinter as tk  #pip install tkinter
import re
from PIL import Image, ImageTk, ImageSequence
import tkinter.scrolledtext as tkscrolled
import subprocess
import psutil #pip install psutil
import openai #pip install openaiselect * from assistant_history;
import time
import threading
import requests
import json
import calendar
import random
import ctypes
import mysql.connector
from datetime import datetime
import pyautogui

openai.api_key = "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" #openai api key


# connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devang@123",
    database="myassistantdb"
)

# voice from os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)
 

#email id dictionary content id
email_id = {
  "devang": "devangmagare@gmail.com",
  "deepak": "deepakchoudhary20010909@gmail.com",
  "john": "ben10friend14@gmail.com"
  }

user_name = "Devang"
bot_name = "One For All"

#create GUI for Voice assistant
class VoiceAssistantGUI:
    def __init__(self):
        # Create the main window
        self.conversation = ""  
        self.exMode = False 

        self.root = tk.Tk()
        self.root.title("ONE.FOR.ALL")
        self.root.geometry("1200x800")
        self.root.configure(bg='#F29989') # Set the background color to dark gray
        
        # Create the logo image
        logo_image = Image.open("D:\Python project\Assistant\OFA.png")
        logo_image = logo_image.resize((30, 30), Image.Palette.ADAPTIVE)
        self.logo = ImageTk.PhotoImage(logo_image)

        logo_image2 = Image.open("D:\Python project\Assistant\Mic.png")
        logo_image2 = logo_image2.resize((30, 30), Image.Palette.ADAPTIVE)
        self.logo2 = ImageTk.PhotoImage(logo_image2)

        
        
        # Create the title label
        self.title_label = tk.Label(self.root, text="ONE.FOR.ALL", font=("Helvetica", 20), fg="#FFFFFF", bg="#F29989")#2C2C2C UPAR VALE TEXT KA BG
        self.title_label.pack(side=tk.TOP, pady=10)
        
        # Create the voice assistant image
        assistant_image = Image.open("D:\Python project\Assistant\OFA.png")
        assistant_image = assistant_image.resize((500, 300), Image.Palette.ADAPTIVE)
        self.assistant = ImageTk.PhotoImage(assistant_image)
        self.assistant_label = tk.Label(self.root, image=self.assistant, bg="#FFFFFF")#2C2C2C LPGO BORDER
        self.assistant_label.pack(side=tk.TOP, padx=20, pady=10)
        
        # Create the text area
        self.text_area = tkscrolled.ScrolledText(self.root, height=10, width=50, font=("Helvetica", 14), fg="#000000", bg="#FFFFFF", insertbackground="#FFFFFF")#2C2C2C
        self.text_area.pack(side=tk.TOP, padx=10, pady=10)
        
        
        # Create the speak button
        self.button = tk.Button(self.root, text="Speak", font=("Helvetica", 14), fg="#FFFFFF", bg="#318C28", activebackground="#000080", activeforeground="#318C28", command=self.on_button_click, image=self.logo2, compound=tk.LEFT)#318C28
        self.button.pack(side=tk.TOP, padx=10, pady=10)
        
        # Start the main loop
        self.root.mainloop()
    
    def on_button_click(self):
        # Get the text from the entry box
        
        # self.playgif()
        self.speakMain()
        
        
        
    def responebox(self, value):
        self.text_area.insert(tk.END,f"{value}\n")
        self.text_area.update_idletasks()
        self.text_area.see("end")

    def playgif(self):
        global img
        img = Image.open("D:\Python project\Assistant\voice_assistant2.gif")
        print("play")

        lbl = tk.Label(self.root)
        lbl.place(x=0, y=0)
        for img2 in ImageSequence.Iterator(img):
            img2 = ImageTk.PhotoImage(img2)
            self.assistant_label.config(image = img2)
            time.sleep(0.02)
            self.root.update()

        download_thread = threading.Thread(target=self.playgif(), name="Downloader")
        download_thread.start()

    def wishMe(self):
        # Get the current time
        self.now = datetime.now()

        # Get the hour from the current time
        self.hour = self.now.hour

        # Determine the appropriate greeting based on the hour
        if self.hour < 12:
            greeting = "Good morning!"
        elif self.hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"

        # Print the greeting
        self.speak2(f"{greeting}! My name is OneForAll. How can I assist you today?")


    def speak(self,audio):
        sql = "INSERT INTO assistant_history (command, timestamp, response) VALUES (%s, %s, %s)"
        values = (self.command, self.timestamp, audio)
        self.cursor.execute(sql, values)
        db.commit()
        self.responebox(audio)
        engine.say(audio)
        engine.runAndWait()
        return

    def speak2(self,audio):
        self.responebox(audio)
        engine.say(audio)
        engine.runAndWait()
        return


    def takeCommand(self):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            self.responebox("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.responebox("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            self.responebox("User said: "+query)

        except Exception as e:
            # print(e)
            print("Say that again please...")
            self.responebox("Say that again please...")
            return "None"
        return query


    def sendEmail(self,to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('oneforallplusultra999@gmail.com', 'sjfmoitturekhook')
        server.sendmail('oneforallplusultra999l@gmail.com', to, content)
        server.close()

    def note(self,text):
        print("inside note()")
        date = datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)

        subprocess.Popen(["notepad.exe", file_name])

    def chatgptmode(self,user_input):

        prompt = user_name+":"+user_input + "\n"+bot_name+":"
        self.conversation += prompt

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=self.conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str =response_str.split(
            user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

        self.conversation+= response_str +"\n"
        

        engine.say(response_str)
        engine.runAndWait()
        return response_str

    def speakMain(self):
        self.wishMe()

        while True:
            
            if self.exMode != True :
                print(f"inside normal Mode {self.exMode}")
                query = self.takeCommand().lower()

                # create a cursor object to interact with the database
                self.cursor = db.cursor()

                # create table if it doesn't exist
                self.cursor.execute("CREATE TABLE IF NOT EXISTS assistant_history (id INT AUTO_INCREMENT PRIMARY KEY, command VARCHAR(255), timestamp DATETIME, response varchar(5000))")

                

                # get current timestamp
                self.timestamp = datetime.now()

                # commit changes to database
                

                # print confirmation message

                print(query)

                # insert command and timestamp into database
                

                # get command from virtual assistant
                self.command = query

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    self.speak("Searching Wikipedia...")

                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    self.speak("According to Wikipedia")

                    print(results)
                    self.speak(results)

                elif 'make a note' in query:
                    self.speak("What would you like me to write down?")
                    note_text = self.takeCommand()
                    print(f"note_text: {note_text}")
                    self.note(note_text)
                    self.speak("I have made a note of that.")

                elif 'remember this' in query:
                    self.speak("What would you like me to write down?")
                    note_text = self.takeCommand()
                    print(f"note_text: {note_text}")
                    self.note(note_text)
                    self.speak("I have made a note of that.")

                elif 'extreme mode' in query:  #Exterme mode for voice assistant
                    self.exMode = True
                    self.speak("Extreme Mode ON")
                    self.speak("What Would you like to ask the Powerfull AI")
                    data = self.takeCommand()
                    value = self.chatgptmode(data)
                    self.speak(value)

                elif "news" in query:
                    url = (
                        "http://newsapi.org/v2/top-headlines?"
                        "country=in&"
                        "apiKey=fdceb1c0af4b4815a0504c2077658343"
                    )

                    try:
                        response = requests.get(url)
                    except:
                        self.speak("Please check your connection")

                    news = json.loads(response.text)

                    for index, new in enumerate(news["articles"]):
                        print(index)
                        if(index == 1):
                            break
                        print(str(new["title"]), "\n")
                        self.speak(str(new["title"]))
                        engine.runAndWait()

                        print(str(new["description"]), "\n")
                        self.speak(str(new["description"]))
                        engine.runAndWait()
                        time.sleep(2)

                elif 'battery' in query:
                    print("inside battery")
                    battery=psutil.sensors_battery()
                    percentage=battery.percent
                    self.speak('Our current battery status is '+str(percentage)+" percent")

                elif 'how much power' in query:
                    print("inside battery")
                    battery=psutil.sensors_battery()
                    percentage=battery.percent
                    self.speak('Our current battery status is '+str(percentage)+" percent")

                elif 'who are you' in query:
                    self.speak("I am OneForAll")

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                
                elif 'open whatsapp' in query:
                    webbrowser.open("https://web.whatsapp.com/")

                elif 'open notepad' in query:
                    npath= "C:\\Windows\\notepad.exe"
                    os.startfile(npath)

                elif 'open excel' in query:
                    npath= "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    os.startfile(npath)

                elif 'open word' in query:
                    npath= "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    os.startfile(npath)

                elif 'IP address' in query:
                    ip=get("https\\api.ipify.org").text
                    self.speak(f"your ip address is {ip}")#

                elif 'open command prompt' in query:
                    os.system("start cmd")

                elif 'show database' in query:
                    # Open the Start menu
                    pyautogui.press('win')
                    time.sleep(1)

                    # Type "cmd" to search for the Command Prompt
                    pyautogui.write('cmd')
                    time.sleep(1)

                    # Press Enter to launch the Command Prompt
                    pyautogui.press('enter')
                    time.sleep(1)

                    # Wait for the Command Prompt window to open
                    time.sleep(3)

                    # Move the mouse to the specified coordinates
                    pyautogui.moveTo(100, 100, duration=1)

                    # Right-click to open the context menu
                    pyautogui.rightClick()


                    # Press the "p" key to select "Paste"
                    pyautogui.write('mysql -u root -p')
                    pyautogui.press('enter')

                    # Press Enter to execute the command
                    pyautogui.write('Devang@123')
                    pyautogui.press('enter')

                    time.sleep(1)
                    pyautogui.write('show databases;')
                    pyautogui.press('enter')

                    time.sleep(1)
                    pyautogui.write('use myassistantdb;')
                    pyautogui.press('enter')

                    time.sleep(1)
                    pyautogui.write('select * from assistant_history;')
                    pyautogui.press('enter')

                elif 'send message' in query:
                    kit.sendwhatmsg("+918010362954","this is test message") #

                elif 'open google' in query:
                    self.speak("sir what should i search on google")
                    cm=self.takeCommand().lower()
                    webbrowser.open(f"{cm}")

                elif 'play on youtube' in query:
                    self.speak("sir what should i play")
                    cm=self.takeCommand().lower()
                    kit.playonyt(f"{cm}")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")

                elif ' time' in query:
                    strTime = datetime.now().strftime("%H:%M:%S")
                    self.speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\A_R_COMPUTERS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif'change wallpaper'in query:
                    print('changing wallpaper...')
                    self.speak('changing wallpaper...')
                    img = r"C:\Users\A_R_COMPUTERS\OneDrive\Desktop\wallpaper"
                    list_img = os.listdir(img)
                    imgChoice = random.choice(list_img)
                    randomImg = os.path.join(img, imgChoice)
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                    self.speak("Background changed successfully")

                elif 'send an email to' in query: #
                    try:

                        query_len = len(query)
                        data = query[17:query_len]
                        self.speak("What should I say?")
                        content = self.takeCommand()
                        to = email_id[data]
                        self.sendEmail(to, content)
                        self.speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        self.speak("I am not able to send this email")

                elif "now quit" in query:
                    self.speak("Thanks for using me and have a good day sir")
                    sys.exit()

                elif "terminate yourself" in query:
                    self.speak("Thanks for using me and have a good day sir")
                    sys.exit()
            elif self.exMode == True:
                print(f"inside extreme Mode {self.exMode}")
                data = self.takeCommand()
                if('normal mode' in data):
                    self.exMode = False
                    self.responebox("Switching to Normal Mode")
                    self.speak("Switching to Normal Mode")
                elif "now quit" in query:
                    self.speak("Thanks for using me and have a good day sir")
                    sys.exit()
                else:
                    value = self.chatgptmode(data)
                    self.speak(value)

                
       
if __name__ == "__main__":
    gui = VoiceAssistantGUI()