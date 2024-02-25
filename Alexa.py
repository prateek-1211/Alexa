import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon!")
        print("Good AfterNoon!")
    elif hour >= 18 and hour < 22.30:
        speak("Good Evening!")
        print("Good Evening!")
    else:
        speak("Good Night")
        print("Good Night")
    
    speak("I am Alexa Sir. Please tell me how may I help you")
    print("I am Alexa Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeninig...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
def Quit():
    speak("Quit Now")
    print("Quit Now")

         
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open whatsappweb' in query:
            webbrowser.open("whatsappweb.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Asus\\OneDrive\\Desktop\\Spotify_Clone\\song'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "D:\\C_Programming Practise"
            os.startfile(codePath)
        elif 'email to Prateek' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "kannubhargav386@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak("sorry my friend Prateek. I am not able to send this email")
        else:
            Quit()