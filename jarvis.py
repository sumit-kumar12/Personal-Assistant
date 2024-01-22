
from ast import Continue
import datetime
from http import server
from operator import contains
import random

import pyttsx3                      #pip install pyttsx3
import speech_recognition as sr     #pip install speechrecognition
import wikipedia                    #pip install wikipedia
import webbrowser
import os
import smtplib                      #pip install smtp
import openai

openai.api_key = "enter API key open AI "


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good Morning!")
    elif hour >= 12 and hour <=18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour <=20:
        speak("Good Evening!")
    else:
        speak("Good Night")
        
    speak("I am Jarvis Sir. Please tell me, How can I help you ")
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 0.7
        r.energy_threshold = 150
        audio = r.listen(source)
        
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')  # type: ignore
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarviscreatedbysumit@gmail.com','jarvis123456789')
    server.sendmail('jarviscreatedbysumit@gmail.com', to, content)
    server.close()
    
    
def chat(user_input):
    messages = []

    # Set the system message to initialize the chatbot with a name
    system_msg = "You are a chatbot named Jarvis . Your goal is to assist users with their queries."
    messages.append({"role": "system", "content": system_msg})
    messages.append({"role": "user", "content": user_input})
    
    while True:
        try:
        
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
            
            assistant_reply = response["choices"][0]["message"]["content"] # type: ignore
            messages.append({"role": "assistant", "content": assistant_reply})
        except Exception:
                continue
            
        return assistant_reply
    

def clear_terminal():
    # Check the operating system
    if os.name == 'posix':  # Linux and macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')
    else:
        # Unsupported operating system
        print("Unsupported operating system")

        
        

    
    
   


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower() # type: ignore
        
        # Logic for excuting task based on Query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open github' in query:
            webbrowser.open("github.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\New folder (2)\\song'
            songs = os.listdir(music_dir)
            print(f"{songs} + \n")
            
            count = 0
            for i in songs:
                count += 1
            n = random.randrange(0, count-1)
            os.startfile(os.path.join(music_dir, songs[n]))
            
        elif 'play song' in query:
            music_dir = 'D:\\New folder (2)\\song'
            songs = os.listdir(music_dir)
            print(f"{songs} + \n")
            
            count = 0
            for i in songs:
                count += 1
            n = random.randrange(0, count-1)
            os.startfile(os.path.join(music_dir, songs[n]))
            
        elif 'play the song' in query:
            music_dir = 'D:\\New folder (2)\\song'
            songs = os.listdir(music_dir)
            print(f"{songs} + \n")
            
            count = 0
            for i in songs:
                count += 1
            n = random.randrange(0, count-1)
            os.startfile(os.path.join(music_dir, songs[n]))
            
        elif 'time' in query:
            steTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {steTime}")
            print(f"{steTime} \n")
            
        elif 'open code' in query:
            codepath = "C:\\Users\\sumit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open vs code' in query:
            codepath = "C:\\Users\\sumit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open visual studio' in query:
            codepath = "C:\\Users\\sumit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()

                speak("Tell me email where you want to send")
                
                to = takeCommand().lower() # type: ignore
                to = to.replace(" ", "") # type: ignore
                print(to)
                sendEmail(to, content)
                speak("Email has been send!")
            
            except Exception as e:
                print(e)
                
                speak("Sorry Sir, I am not abel to send email at this moment")
                
        else:
            if query == " " or "":
                continue
            else:
                user_input = query
                reply = chat(user_input)
                if "hello" in query:
                    print ("Jarvis: " + reply +"\n")
                    speak(reply)
                    
                elif reply == "Hello! How can I assist you today?" :
                    continue
                else:
                    print ("Jarvis: " + reply +"\n")
                    speak(reply)
                    
                    
        clear_terminal()