import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit


engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}")
    except:
        speak("Sorry, I didn't catch that. Please say again.")
        return ""
    return query.lower()
def process_command(query):
     if "who is" in query or "what is" in query:
        speak("Searching in Wikipedia")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find that.")
