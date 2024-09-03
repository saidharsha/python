# pyttsx3: Text-to-speech library for converting text to speech
import pyttsx3

# speech_recognition: Library for performing speech recognition
import speech_recognition as sr

# datetime: Module for working with dates and times
import datetime

# wikipedia: Library for accessing and searching Wikipedia content
import wikipedia

# webbrowser: Module for opening and displaying web pages
import webbrowser

# os: Module for interacting with the operating system
import os

# subprocess: Module for spawning new processes, also used as sp
import subprocess as sp

# pywhatkit: Library for automating WhatsApp messages and other tasks
import pywhatkit as kit

# psutil: Library for retrieving information on system utilization (CPU, memory, disks, network, sensors)
import psutil

# requests: Library for making HTTP requests
from requests import get

# pyjokes: Library for retrieving programming-related jokes
import pyjokes

# time: Module for working with time-related functions
import time

# sys: Module providing access to some variables used or maintained by the interpreter and functions that interact with the interpreter
import sys

# pyautogui: Library for programmatically controlling the mouse and keyboard
import pyautogui

# Speak function will pronounce the string which is passed to it
print("Initializing kiki")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Initializing kiki....")
master = "Sai Dharshan"

# Function to take user command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=8, phrase_time_limit=8)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            speak("I'm sorry, Say that again please:")
            return "None"
        
        # Check if the recognized query is "None"
        if query.lower() == "none":
            speak("I couldn't understand your command. Please try again.")
            return takeCommand()  # Ask the user to repeat the command
        elif 'no thanks' in query.lower():
            speak("Alright, stopping the command recognition.")
            sys.exit()
        else:
            return query

# Function for wishing as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if 0 <= hour < 12:
        speak("Good morning.." + master)
    elif 12 <= hour < 18:
        speak("Good afternoon.." + master)
    else:
        speak("Good evening.." + master)
    speak("I am kiki. version 2.0, how may I assist you sir")

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

# The main program starts here...
while True:
    wishMe()
    query = takeCommand()

    # Logic for executing tasks as per the query
    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        query = query.replace("who is", "")
        query = query.replace("may I know", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
    elif 'youtube' in query.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif 'open facebook' in query.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif 'open google' in query.lower():
        speak("What should I search in Google?")
        search_query = takeCommand().lower()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif 'open snapchat' in query.lower():
        webbrowser.open("snapchat.com")
        speak("Opening Snapchat")
    elif 'open twitter' in query.lower():
        webbrowser.open("twitter.com")
        speak("Opening Twitter")
    elif 'open whatsapp' in query.lower():
        webbrowser.open("whatsapp.com")
        speak("Opening WhatsApp")
    elif 'open bookmyshow' in query.lower():
        webbrowser.open("bookmyshow.com")
        speak("Opening BookMyShow")
    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\rayaa\\Downloads\\songs"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
        speak("Playing songs")
    elif 'play movie' in query.lower():
        movies_dir = "D:\\movies"
        movies = os.listdir(movies_dir)
        print(movies)
        os.startfile(os.path.join(movies_dir, movies[0]))
        speak("Playing movie")
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print({strTime})
        speak(f"{master} the time is {strTime}")
    elif 'open code' in query.lower():
        codepath = "C:\\Users\\rayaa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening Visual Studio Code")
        os.startfile(codepath)
    elif 'open notepad' in query.lower():
        path = "C:\\Windows\\System32\\notepad.exe"
        os.startfile(path)
    elif 'open command prompt' in query.lower():
        os.system("start cmd")
        speak("Opening Command Prompt")
    elif 'open image' in query.lower():
        from PIL import Image
        img = Image.open("C:\\Users\\rayaa\\Pictures\\OIP.jpg")
        speak("Opening image")
        img.show()
    elif 'message' in query.lower():
        kit.sendwhatmsg("+(number)", "Hi", 2, 47, True, 5)
    elif 'battery percentage' in query.lower():
        batteryinformation = psutil.sensors_battery()
        print("The Battery percentage of the system = ", batteryinformation.percent)
        if batteryinformation.power_plugged == True:
            print("The battery of the system is Charging!!!")
        elif batteryinformation.power_plugged == False:
            print("The battery of the system is NOT Charging/Discharging")
    elif 'camera' in query.lower():
        open_camera()
    elif 'joke' in query.lower():
        My_joke = pyjokes.get_joke(language="en", category="all")
        print(My_joke)
        speak(My_joke)
    elif 'documentation' in query.lower():
        os.startfile("C:\\Users\\rayaa\\Documents\\Template.docx")
    elif 'volume up' in query.lower():
        pyautogui.press("volumeup")
    elif 'volume down' in query.lower():
        pyautogui.press("volumedown")
    elif 'volume mute' in query.lower():
        pyautogui.press("volumemute")
    elif 'volume unmute' in query.lower():
        pyautogui.press("volumeunmute")
    elif 'open google' in query.lower():
        speak("What should I search in Google?")
        cm = takeCommand().lower()
        webbrowser.open(f"{cm}")
    elif 'carryminati' in query.lower():
        kit.playonyt("carryminati")
    elif 'no thanks' in query.lower():
        speak("Thanks for using me")
        sys.exit()
    elif 'shut down the system' in query.lower():
        os.system("shutdown /s /t s")
    elif 'restart the system' in query.lower():
        os.system("shutdown /r /t s")
    elif 'close notepad' in query.lower():
        speak("Okay sir, closing Notepad")
        os.system("taskkill /f /ie notepad.exe")
    elif 'switch window' in query.lower():
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")
    elif 'desktop' in query.lower():
        pyautogui.keyDown("start")
        pyautogui.press("D")
        time.sleep(1)
        pyautogui.keyUp("D")

    speak("Sir, do you have any other work?")
    query = takeCommand()