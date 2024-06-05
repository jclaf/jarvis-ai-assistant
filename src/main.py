import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr

class Speech :
    def __init__(self):
        self.engine = pyttsx3.init("espeak")
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[26].id)
        self.engine.setProperty('rate', 180)

    # search languague voices
    def search_voices(self):
        for n in range(0, len(self.voices)):
            print(n,self.voices[n])
        self.engine.runAndWait()

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        self.engine.stop()

    def time_(self):
        Time=datetime.datetime.now().strftime("%I:%M")
        self.speak("Il est " + Time)

    def date_(self):
        #v1
        Today=date.today().strftime("%d %B")
        self.speak("On est le " + Today)
        #v2
        # year = datetime.datetime.now().year
        # month = datetime.datetime.now().month
        # date = datetime.datetime.now().date
        # self.speak("On est le ")
        # self.speak(date)
        # self.speak(month)
        # self.speak(year)

    def wishme(self):    
        hour = datetime.datetime.now().hour
        
        if hour>=6 and hour<18:
            self.speak("Bonjour Monsieur !")
        elif hour>=18 and hour<24:
            self.speak("Bonsoir Monsieur !")    
        self.date_()
        self.time_()
        
        self.speak("Jarvis est à votre service. Dites moi ce dont vous avez besoin ?")

    def TakeComman():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("En écoute ....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try
        
jarvis = Speech()
jarvis.wishme()



#test