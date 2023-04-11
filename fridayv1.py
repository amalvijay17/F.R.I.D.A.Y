import pyttsx3 
import datetime 
import speech_recognition as sr 
import wikipedia
import webbrowser
import requests 
import json 
import os
import pywhatkit as kit
from pytube import YouTube 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
print(voices)
engine.setProperty('voice',voices[1].id)
author = "Boss"

def speak(audio): 
  engine.say(audio) 
  engine.runAndWait() 

def wishing():
  hour = int(datetime.datetime.now().hour) 
  if hour >=0 and hour <12:
    speak(f"Good Morning {author}")
  elif hour >= 12 and hour <18:
    speak(f"Good Afternoon {author}")
  else:
    speak(f"Good Evening {author}")
  speak(f"Please Tell me how can i assist you")

def command(): 
  record = sr.Recognizer() 
  with sr.Microphone() as source:
    print("Listening...")
    record.pause_threshold = 1.5
    audio = record.listen(source,phrase_time_limit=6) 
  try: 
      print("Recognizing...")
      query = record.recognize_google(audio,language='en-in') 
      print(f"User Said:{query} \n")
  except Exception as e: 
      print(f"Sorry {author}, Say that again...") 
      speak(f"Sorry {author}, Say that again...")
      return "None"
  return query

if __name__ == "__main__":
  
  #speak(f"Welcome back{author}, Iam Friday your personal assistant")
  #wishing()
  #command()
  if 1: 

    # Wikipedia

    query = command().lower() 
    if 'wikipedia' and 'who' in query:
      speak("Searching Wikipedia...")
      results = wikipedia.summary(query,sentences = 2) 
      speak("According to wikipedia")
      print(results)
      speak(results)

    # Opening Google.com

    elif 'open google' in query: 
      speak("Sure Sir")
      webbrowser.open("google.com")

     # Opening YouTube.com

    elif 'open youtube' in query:
      speak("Okay Sir")
      webbrowser.open("youtube.com")

    # Opening Red Team Hacker Academy

    elif 'open my institution' in query: 
      speak("Ofcourse Sir")
      webbrowser.open("https://redteamacademy.com/")

    # Browsing with Web Browser
       
    elif 'search browser' in query: 
      speak("What should i search ?")
      usercommand = command().lower() 
      webbrowser.open(f"{usercommand}")
      speak("Hope you are happy")

    # Current News

    elif 'news' in query: 
      speak("News Headlines")
      url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=e676816d63354ed8b697f373905beb7c"
      news = requests.get(url).text 
      news = json.loads(news) 
      art = news['articles'] 
      for article in art: 
        print(article['title']) 
        speak(article['title'])

        print(article['description']) 
        speak(article['description'])
        speak("Moving on to the next news")

    # Knowing the ip address

    elif 'ip address' in query: 
      ip = requests.get('http://api.ipify.org').text 
      print(f"Your IP is {ip}")
      speak(f"Your IP is {ip}")
      speak("Is it correct or should I check again.... I am Joking")

    # Opening Command Prompt

    elif 'open command prompt' in query:
      os.system("start cmd")
      speak("Hope you are happy...")

    # Opening Adobe Photoshop

    elif 'open photoshop' in query: 
      location = ("C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe") 
      os.startfile(location)
      speak("Have a good day sir")

    # Opening YouTube and playing a video

    elif 'play youtube' in query:
      speak('what should i search in youtube ?')
      usercommand = command().lower() 
      kit.playonyt(f"{usercommand}")

    # Youtube Downloader

    elif 'download video' in query:
      speak("Enter or Copy the Video Link to continue: ")
      link = input("Enter a youtube URL\n") 
      Download_Video_Link = YouTube(link)

      Title = Download_Video_Link.title
      Number_of_views = Download_Video_Link.views
      Length_of_Video = Download_Video_Link.length
      Author_of_Video = Download_Video_Link.author
      Publish_date = Download_Video_Link.publish_date

      def details():

        print("Title: ", Title)
        print("Number of Views:", Number_of_views)
        print("Length of the Video in seconds:", Length_of_Video)
        print("Youtube Channel:", Author_of_Video)
        print("Publish Date:", Publish_date)

      def video_downloader():

        Download_Video_Link.streams.get_highest_resolution().download() 
        print("Download finished successfully")
      details()
      video_downloader()
      speak("Video downloaded successfully")

    # Directory Enumerator

    elif 'scanner' in query: 
      speak(f"{author}Enter a website to continue")
      def does_exist(url):
        response = requests.get(url) 
        if response.status_code == 200: 
          print(f'URL exists {url}') 

      with open("common.txt") as f: 
        contents = f.read()
        print("****************************************")
        print("*                                      *")
        print("*        Directory Enumerator          *")
        print("*                                      *")
        print("****************************************")
        website = input("Enter a website\n")
        for line in contents.split('\n'): 
            
            u = website + '/' + line
            #print(u)
            does_exist(u) 

    # Clickjacking

    elif 'clickjacking' in query:
        speak("Enter a website")
        print("****************************************")
        print("*                                      *")
        print("*             Clickjacking             *")
        print("*                                      *")
        print("****************************************")
        domain = input("Enter a website\n")
        headers = requests.get(domain).headers
        #print(headers)
        if 'X-Frame-Options' in headers:
          print("Entered Website is not vulnerable")
          speak("Entered Website is not vulnerable")
        else:
          print("Entered Website is vulnerable")
          speak("Entered Website is vulnerable")