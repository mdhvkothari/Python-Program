import pyttsx3
import datetime
#we use microsoft api which is sapi5
engine = pyttsx3.init('sapi5')
#in our computer we have two voices one is of male and another is female
voices = engine.getProperty('voices')

#we select male one
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am jarvis! how may i help u")

if __name__ == "__main__":
    wishMe()
