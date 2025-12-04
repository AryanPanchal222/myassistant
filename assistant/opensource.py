import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import datetime
import webbrowser
import wikipedia
import pywhatkit
import os
import random

# ---------------- GLOBAL LANGUAGE SETTINGS ----------------
current_recog_lang = "en-IN"   # for speech recognition
current_tts_lang = "en"        # for speaking
current_lang_name = "English"  # just for printing

def set_language(lang_code):
    global current_recog_lang, current_tts_lang, current_lang_name

    if lang_code == "hi":   # Hindi
        current_recog_lang = "hi-IN"
        current_tts_lang = "hi"
        current_lang_name = "Hindi"
        wikipedia.set_lang("hi")
        speak("अब से मैं हिंदी में बात करूँगा।")
    elif lang_code == "gu": # Gujarati
        current_recog_lang = "gu-IN"
        current_tts_lang = "gu"
        current_lang_name = "Gujarati"
        wikipedia.set_lang("gu")
        speak("હવે હું ગુજરાતી માં વાત કરીશ.")
    else:                   # English default
        current_recog_lang = "en-IN"
        current_tts_lang = "en"
        current_lang_name = "English"
        wikipedia.set_lang("en")
        speak("Now I will speak in English.")

# ---------------- TEXT TO SPEECH ----------------
def speak(text):
    print(f"Assistant ({current_lang_name}):", text)
    try:
        tts = gTTS(text=text, lang=current_tts_lang)
        filename = f"voice_{random.randint(1, 10000)}.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("Error in speak:", e)

# ---------------- LISTEN FROM MIC ----------------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening ({current_lang_name})...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language=current_recog_lang)
        print("You:", query)
    except Exception as e:
        if current_tts_lang == "hi":
            speak("माफ़ कीजिए, दुबारा बोलिए।")
        elif current_tts_lang == "gu":
            speak("માફ કરજો, ફરીથી બોલશો?")
        else:
            speak("Sorry, please say that again.")
        return ""
    return query.lower()

# ---------------- MAIN COMMAND LOGIC ----------------
def process_command(query):
    # -------- LANGUAGE CHANGE COMMANDS --------
    if any(x in query for x in ["hindi", "हिंदी", "hindime", "hindī"]):
        set_language("hi")
        return True

    if any(x in query for x in ["gujarati", "ગુજરાતી", "gujrati", "gujarati ma"]):
        set_language("gu")
        return True

    if any(x in query for x in ["english", "इंग्लिश", "ઈંગ્લિશ"]):
        set_language("en")
        return True

    # -------- TIME --------
    if any(x in query for x in ["time", "samay", "समय", "વખત", "સમય શું", "what is time"]):
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        if current_tts_lang == "hi":
            speak(f"अभी समय है {time_str}")
        elif current_tts_lang == "gu":
            speak(f"હમણું સમય છે {time_str}")
        else:
            speak(f"The time is {time_str}")
        return True

    # -------- DATE --------
    if any(x in query for x in ["date", "today", "aaj ki tareekh", "आज की तारीख", "આજે તારીખ"]):
        today = datetime.date.today()
        d = today.strftime('%d %B %Y')
        if current_tts_lang == "hi":
            speak(f"आज की तारीख है {d}")
        elif current_tts_lang == "gu":
            speak(f"આજની તારીખ છે {d}")
        else:
            speak(f"Today's date is {d}")
        return True

    # -------- OPEN YOUTUBE --------
    if any(x in query for x in ["youtube", "यूट्यूब", "યુટ્યુબ"]):
        if current_tts_lang == "hi":
            speak("यूट्यूब खोल रहा हूँ।")
        elif current_tts_lang == "gu":
            speak("યુટ્યુબ ખોલું છું.")
        else:
            speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com/")
        return True

    # -------- OPEN GOOGLE --------
    if any(x in query for x in ["google", "गूगल", "ગુગલ"]):
        if current_tts_lang == "hi":
            speak("गूगल खोल रहा हूँ।")
        elif current_tts_lang == "gu":
            speak("ગુગલ ખોલું છું.")
        else:
            speak("Opening Google.")
        webbrowser.open("https://www.google.com/")
        return True

    # -------- GOOGLE SEARCH --------
    if any(x in query for x in ["search", "खोजो", "ढूंढो", "શોધ", "search karo"]):
        if current_tts_lang == "hi":
            speak("क्या सर्च करूँ?")
        elif current_tts_lang == "gu":
            speak("શુ સર્ચ કરું?")
        else:
            speak("What should I search?")
        search_query = take_command()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            if current_tts_lang == "hi":
                speak(f"{search_query} सर्च कर रहा हूँ।")
            elif current_tts_lang == "gu":
                speak(f"{search_query} સર્ચ કરી રહ્યો છું.")
            else:
                speak(f"Searching for {search_query}.")
            webbrowser.open(url)
        return True

    # -------- PLAY SONG ON YOUTUBE --------
    if any(x in query for x in ["play", "चलाओ", "चला दो", "બજાવો"]):
        # remove words like 'play', 'चलाओ' etc.
        song = query.replace("play", "").replace("चलाओ", "").replace("चला दो", "").replace("બજાવો", "").strip()
        if not song:
            song = query
        if current_tts_lang == "hi":
            speak(f"{song} यूट्यूब पर चला रहा हूँ।")
        elif current_tts_lang == "gu":
            speak(f"{song} યુટ્યુબ પર ચલાવી રહ્યો છું.")
        else:
            speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
        return True

    # -------- WIKIPEDIA --------
    if any(x in query for x in ["who is", "what is", "कौन है", "क्या है", "શું છે"]):
        if current_tts_lang == "hi":
            speak("विकिपीडिया पर देख रहा हूँ।")
        elif current_tts_lang == "gu":
            speak("વિકિપીડિયા પર શોધું છું.")
        else:
            speak("Searching in Wikipedia.")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            if current_tts_lang == "hi":
                speak("माफ़ कीजिए, मुझे कुछ नहीं मिला।")
            elif current_tts_lang == "gu":
                speak("માફ કરશો, મને કઈ મળ્યું નહીં.")
            else:
                speak("Sorry, I couldn't find that.")
        return True

    # -------- EXIT --------
    if any(x in query for x in ["stop", "exit", "bye", "बस", "रुको", "બંધ", "બસ હવે"]):
        if current_tts_lang == "hi":
            speak("ठीक है, फिर मिलते हैं।")
        elif current_tts_lang == "gu":
            speak("બરાબર, પછી મળીશું.")
        else:
            speak("Okay, bye! Have a nice day.")
        return False

    # -------- DEFAULT --------
    if current_tts_lang == "hi":
        speak("अभी मैं ये काम नहीं कर सकता, बाद में सिखा देना।")
    elif current_tts_lang == "gu":
        speak("હાલ હું આ કામ નથી કરી શકતો, મને પછી શીખવી દેજો.")
    else:
        speak("Sorry, I don't know how to do that yet.")
    return True


# ---------------- RUN ASSISTANT ----------------
if __name__ == "__main__":
    set_language("en")  # start in English, you can change
    speak("Hello Aryan, I am your personal assistant. बोलो, क्या मदद चाहिए?")
    while True:
        query = take_command()
        if query == "":
            continue
        if not process_command(query):
            break
