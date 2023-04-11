import pyttsx3 # Text to speech conversion library
import datetime # For the current time
import speech_recognition as sr # For speech recognition sr is shorthand for speech recognition
import wikipedia
import webbrowser
import requests # We are using an API (Application Programming Interface) so requests is used to get url
import json # JSON is a lightweight format for storing and transporting data. Used in news functionality
import os # For opening Windows Applications
import pywhatkit as kit # To play a particular YouTube video
from pytube import YouTube # For Downloading YouTube videos

engine = pyttsx3.init('sapi5') # init function is used to get an engine instance for the speech synthesis.
# sapi5 is the inbuilt voice module of Windows Operating System. We're going to use it for audio feedback

voices = engine.getProperty('voices') # You can grab the list of available voices 
# print(voices)
engine.setProperty('voice',voices[1].id) # Setting the voice. Selecting voice 0 - Male, 1 - Female
# print(voices[1].id)
author = "Boss"
def speak(audio): # Speak the audio. Text as argument & convert text to audio
  engine.say(audio) # From pyttsx3
  engine.runAndWait() # From pyttsx3

def wishing():
  hour = int(datetime.datetime.now().hour) # Return Hour as integer format
  if hour >=0 and hour <12:
    speak(f"Good Morning {author}")
  elif hour >= 12 and hour <18:
    speak(f"Good Afternoon {author}")
  else:
    speak(f"Good Evening {author}")
  speak(f"Please Tell me how can i assist you")

def command(): # Audio input and convert it into text format
  record = sr.Recognizer() # Help to take voice/microphone input from user and return string
  with sr.Microphone() as source:
    print("Listening...")
    record.pause_threshold = 1.5 # Seconds of non-speaking audio before a phase is complete
    audio = record.listen(source,phrase_time_limit=6) # Listen to audio and time limit
  try: # The try block lets you test a block of code for errors.
      print("Recognizing...")
      query = record.recognize_google(audio,language='en-in') # Recognize_google used as it is used in Android phone.So is accurate. Converting audio into text
      print(f"User Said:{query} \n")
  except Exception as e:  # The except block lets you handle the error.
      print(f"Sorry {author}, Say that again...") # When no/wrong input is given this executes
      speak(f"Sorry {author}, Say that again...")
      return "None"
  return query

if __name__ == "__main__": # Entry point like main() in C and C++. Place from where program execution begins.
  
  speak(f"Welcome back{author}, Iam Friday your personal assistant")  
  wishing()
  #command()
  if 1: # Runs one time. Over and over use while loop

    # Wikipedia

    query = command().lower() # Converting  query to lower case
    if 'wikipedia' and 'who' in query: # Triggers
      speak("Searching Wikipedia...")
      results = wikipedia.summary(query,sentences = 2) # Function from Wikipedia Module
      speak("According to wikipedia")
      print(results)
      speak(results)

    # Opening Google.com

    elif 'open google' in query: # Triggers
      speak("Sure Sir")
      webbrowser.open("google.com")

     # Opening YouTube.com

    elif 'open youtube' in query: # Triggers
      speak("Okay Sir")
      webbrowser.open("youtube.com")

    # Opening Red Team Hacker Academy

    elif 'open my institution' in query: # Triggers
      speak("Ofcourse Sir")
      webbrowser.open("https://redteamacademy.com/")

    # Browsing with Web Browser
       
    elif 'search browser' in query: # Triggers
      speak("What should i search ?")
      usercommand = command().lower() # Convert query to lower case
      webbrowser.open(f"{usercommand}")
      speak("Hope you are happy")

    # Current News

    elif 'news' in query:  # Triggers
      speak("News Headlines")
      url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=e676816d63354ed8b697f373905beb7c"
      news = requests.get(url).text 
      news = json.loads(news) # API sent Json data.So Convert Json data into python objects using json.loads()
      art = news['articles'] # Getting all contents of articles
      for article in art: # Printing all trending news
        print(article['title']) # News Headlines
        speak(article['title'])

        print(article['description']) # News Content
        speak(article['description'])
        speak("Moving on to the next news")

    # Knowing the ip address

    elif 'ip address' in query: # Triggers
      ip = requests.get('http://api.ipify.org').text # Return IP in text format
      print(f"Your IP is {ip}")
      speak(f"Your IP is {ip}")
      speak("Is it correct or should I check again.... I am Joking")

    # Opening Command Prompt

    elif 'open command prompt' in query: # Triggers
      os.system("start cmd")
      speak("Hope you are happy...")

    # Opening Adobe Photoshop

    elif 'open photoshop' in query: # Triggers
      location = ("C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe") # Location of exe file
      os.startfile(location)
      speak("Have a good day sir")

    # Opening YouTube and playing a video

    elif 'play youtube' in query:
      speak('what should i search in youtube ?')
      usercommand = command().lower() # Convert query to lower case
      kit.playonyt(f"{usercommand}")

    # Youtube Downloader

    elif 'download video' in query:
      speak("Enter or Copy the Video Link to continue: ")
      link = input("Enter a youtube URL\n") # Enter youtube video link
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

        Download_Video_Link.streams.get_highest_resolution().download() # To get highest resolution 720p Maximum
        print("Download finished successfully")
      details()
      video_downloader()
      speak("Video downloaded successfully")

    # Directory Enumerator

    elif 'scanner' in query: # Trigger
      speak(f"{author}Enter a website to continue")
      def does_exist(url):
        response = requests.get(url) # To get URL
        if response.status_code == 200: # Sorting website with 200 OK response
          print(f'URL exists {url}') # Print existing URL

      with open("common.txt") as f: # Common.txt is wordlist
        contents = f.read()
        print("****************************************")
        print("*                                      *")
        print("*        Directory Enumerator          *")
        print("*                                      *")
        print("****************************************")
        website = input("Enter a website\n")
        for line in contents.split('\n'): # Get results in new line
            
            u = website + '/' + line # Printing a slash after result
            #print(u) # Displays all bruteforce results
            does_exist(u) # Showing 200 OK response results

    # Clickjacking

    elif 'clickjacking' in query:
        speak("Enter a website")
        print("****************************************")
        print("*                                      *")
        print("*            Clickjacking              *")
        print("*                                      *")
        print("****************************************")
        domain = input("Enter a website\n")
        headers = requests.get(domain).headers
        #print(headers)
        if 'X-Frame-Options' in headers: # Http Response Header. Avoid click-jacking attacks, by ensuring that their content is not embedded into other sites.
          print("Entered Website is not vulnerable")
          speak("Entered Website is not vulnerable")
        else:
          print("Entered Website is vulnerable")
          speak("Entered Website is vulnerable")