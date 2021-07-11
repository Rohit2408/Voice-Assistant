import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Rohit!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Rohit!")

    else:
        speak("Good Evening Rohit!")

    Name = ("Raven 1 point o")
    speak("I am your assistant")
    speak(Name)

def address():
    speak("How can I help you, Sir.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to recoognise your voice.")
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('Your email id', 'your email password')
    server.sendmail('Senders mail id', to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishme()
    address()

    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching in wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go...")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("Here you go...")
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            speak("Here you go...")
            webbrowser.open("instagram.com")

        elif 'open flipkart' in query:
            speak("Here you go...")
            webbrowser.open("flipkart.com")

        elif 'open amazon' in query:
            speak("Here you go...")
            webbrowser.open("amazon.com")

        elif 'play music' in query or 'play song' in query:
            speak("Here you go...")
            music = "C:\\Music"
            songs = os.listdir(music)
            print(songs)
            random = os.startfile(os.path.join(music, songs[1]))

        elif 'time' in query:
            strttime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strttime}")

        elif 'send a mail' in query:
            try:
                speak("What should I mail?")
                content = takecommand()
                speak("Whom should i send?")
                to = input()
                sendmail(to, content)
                speak("Your mail has been sent")
            except Exception as e:
                print(e)
                speak("I am not able to send this mail")

        elif 'how are you' in query:
            speak("I am fine, what about you?")
            if 'good' in query or 'fine' in query:
                speak("Pleased to know that")

            else:
                pass

        elif "change my name to" in query:
            query = query.replace("Change my name to", "")
            Name = query

        elif 'change name' in query:
            speak("What would you like to call me")
            Name = takecommand()
            speak("Thanks for naming me")

        elif 'whats your name' in query or 'what is your name' in query:
            speak("I am")
            speak(Name)
            print("I am ", Name)

        elif 'exit' in query:
            speak("Thank you for the conversation")
            exit()

        elif 'who made you' or 'who created you' in query:
            speak("I am created by Rohit.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'calculate' in query:
            app_id = "LRGWK5-E5VL4GTTAH"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'who am i' in query:
            speak("A human... maybe")

        elif 'who are you' in query:
            speak("I am your virtual assistant")

        elif 'news' in query:
            def get_category():
                print(
                    "Pease select category of news\n1- Business\n2- Entertainment\n3- Health\n4- Science\n5- Sport\n6- Technology")
                category = int(input("Your Input"))
                if category < 1 or category > 6:
                    speak("Please select a valid Category from List")
                    get_category()
                return category


            def get_news(category):
                if category == 1:
                    category = "business"
                elif category == 2:
                    category = "entertainment"
                elif category == 3:
                    category = "health"
                elif category == 4:
                    category = "science"
                elif category == 5:
                    category = "sport"
                else:
                    category = "Technology"
                API_KEY = "2141b2ccd45543bb891ea29b95d40ca1"
                api_url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"
                speak(f"Please wait while I load the {category} headlines for you")
                top_news = rq.get(api_url).text
                news_json = json.loads(top_news)
                for x in news_json["articles"]:
                    speak(f"{x['title']}")
                    userinp = input("Press Y/N")
                    if userinp == "y" or userinp == "Y":
                        speak(x["description"])
                    else:
                        speak("Thank you for listening")
                        break
                category = get_category()
                get_news(category)

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown' in query:
            speak("Your device will shut down in a sec")
            subprocess.call('shutdown / p /f')

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'my location' in query:
            location = query
            speak("You are being located")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif 'take a picture' or 'take a photo' or 'click a photo':
            ec.capture(0, "Raven Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure you save all your work before signing-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Raven.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'Raven' in query:
            wishme()
            speak("Raven at your service")
            speak(Name)

        elif 'weather' in query:
            api_key = "0ccf4d9c7c30b20269a20552ea6f7fb2"
            base_url = "https://openweathermap.org/current"
            speak("City Name")
            print("City Name: ")
            city_name = takecommand()
            complete_url = base_url + "appid = " + api_key + "&q = " + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temp = y["temp"]
                current_pressure = y["pressure"]
                current_humid = y["humid"]
                z = x["weather"]
                weather_desc = z[0]["description"]
                print("Temperature(in kelvin) = " + str(current_temp) + "\n Atmostpheric Pressure(in hpa unit) = " + str(current_pressure) + "\n Humidity = " + str(current_humid) + "\n Description = " + str(weather_desc))
            else:
                speak("City not found!")

        elif "send message" in query:
            account_sid = "AC86b277c8bfdbadcccf64de5cd287734c"
            auth_token = "19364908bbc7fe5a0d6776e9c28a6deb"
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body = takecommand(),
                    From = "Sender No",
                    to = "Receiver's No"
                )
            print(message.sid)

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you")
            speak(Name)

