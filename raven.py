import random
import time
import winsound
import cv2
import playsound
from bs4 import BeautifulSoup
import pyttsx3
import datetime
import sys
from newsapi import NewsApiClient
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import wolframalpha
import json
import smtplib
import requests as rq
import pyjokes
import pywhatkit
import datefinder
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from json.decoder import JSONDecodeError
from win10toast import ToastNotifier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Raven. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said:\n", query)

    except Exception as e:
        # print(e)
        print("Please repeat your statement again....")
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('Your email id', 'your email password')
    server.sendmail('Senders mail id', to, content)
    server.close()

def get_category():
    speak("Please select category of news\n1- Business\n2- Entertainment\n3- Health\n4- Science\n5- Sport\n6- Technology")
    print("Please select category of news\n1- Business\n2- Entertainment\n3- Health\n4- Science\n5- Sport\n6- Technology")
    category = takeCommand()
    return category

def timer (remider,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=20)
    notificator.show_toast(f"Reminder",remider,duration=20)

    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open documents' in query:
            Doc_path = "C:\\Users\\KIIT\\Documents"
            os.startfile(Doc_path)

        elif 'open downloads' in query:
            Doc_path = "C:\\Users\\KIIT\\Downloads"
            os.startfile(Doc_path)

        elif 'open videos' in query:
            Doc_path = "C:\\Users\\KIIT\\Videos"
            os.startfile(Doc_path)

        elif 'open c drive' in query:
            Doc_path = "C:\\"
            os.startfile(Doc_path)

        elif 'send a mail' in query:
            try:
                speak("What should I mail?")
                content = takeCommand()
                speak("Whom should i send?")
                to = input()
                sendmail(to, content)
                speak("Your mail has been sent")

            except Exception as e:
                print(e)
                speak("I am not able to send this mail")

        elif 'who are you' in query:
            speak("I am Raven 1 point o")

        elif 'who made you' in query:
            speak("I am designed by Rohit.")

        elif 'bye' in query:
            speak("Thank you for the conversation")
            exit()

        elif 'calculate' in query:
            app_id = "LRGWK5-E5VL4GTTAH"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res=  client.query(' '.join(query))
            answer = next(res.results).text
            print(f"The answer is {answer}")
            speak(f"The answer is {answer}")

        elif 'shutdown' in query:
            speak("Your device will shut down in a second....")
            os.system("shutdown /s /t 1")

        elif 'news' in query:
            def get_news(category):
                if 'business' in query:
                    category = "business"
                    speak(category)
                elif 'entertainment' in query:
                    category = "entertainment"
                    speak(category)
                elif 'health' in query:
                    category = "health"
                    speak(category)
                elif 'science' in query:
                    category = "science"
                    speak(category)
                elif 'sport' in query:
                    category = "sport"
                    speak(category)
                elif 'technology' in query:
                    category = "Technology"
                    speak(category)
                API_KEY = "2141b2ccd45543bb891ea29b95d40ca1"
                api_url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"
                speak(f"Please wait while I load the {category} headlines for you")
                top_news = rq.get(api_url).text
                news_json = json.loads(top_news)
                for x in news_json["articles"]:
                    speak(f"{x['title']}")
                    speak("Do you want to continue?")
                    yesno = takeCommand()
                    if 'yes' in query:
                        speak(x["description"])
                    else:
                        speak("Thank you for listening")
                        break
            category = get_category()
            get_news(category)

        elif 'my location' in query:
            location = query
            speak("You are being located....")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif 'weather' in query:
            speak("What is your city name?")
            search = takeCommand()
            url = f"https://www.google.com/search?q=weather+{search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current temperature in {search} is {temp}")

        elif 'joke' in query:
                speak(pyjokes.get_joke())

        elif 'log out' in query:
            speak("Logging off....")
            os.system("shutdown -l")

        elif 'restart' in query:
            speak("Restarting....")
            os.system("shutdown -r")

        elif 'good morning' in query:
            speak("Good Morning !! Rohit")

        elif 'photo' in query or 'picture' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'cmd' in query:
            os.system("start cmd")

        elif 'search' in query:
            speak("What should I search in google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            speak("Whom do you want to send a message")
            send = takeCommand().lower()
            speak("what do you want to send")
            message = takeCommand().lower
            Time = datetime.datetime.now + datetime.timedelta(minutes = 2)
            pywhatkit.sendwhatmsg(f"{send}", f"{message}", f"{Time}")

        elif 'alarm' in query:
            speak("What shall I remind")
            words = takeCommand()
            speak("Enter seconds: ")
            sec = takeCommand()
            timer(words, sec)

        else:
            speak("I didnt get your command.")
            speak("Let's google it")
            webbrowser.open("www.google.com")