import pyttsx3
import datetime


engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #for a 12 hours time
    speak("The current time is")
    speak(Time)

time()





