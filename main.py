import speech_recognition as sr
import webbrowser
import pyttsx3
import importlib
import musicLibrary
import requests
from datetime import datetime
import os
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ENTER_YOUR_API_KEY"
listening_for_command = False  # Add a flag to indicate when Jarvis should stop talking and start listening

def speak(text):
    engine.say(text)
    engine.runAndWait()

def stop_speaking():
    engine.stop()  # This stops the speech engine immediately

def aiProcess(command):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(command)

    return response.text

def processCommand(command):
    global listening_for_command  # Access the global flag
    command = command.lower()

    if"good morning" in command:
        # Get the current hour
        current_hour = datetime.now().hour
        
        if 5 <= current_hour < 12:
            speak("Good morning, sir! How can I assist you today?")
        elif 12 <= current_hour < 18:
            speak(f"It's {datetime.now().strftime('%H:%M')}. sorry sir its not morning  Good afternoon, sir!")
        else:
            speak(f"It's {datetime.now().strftime('%H:%M')}. sorry sir its not morning Good night, sir!")
        

    elif "good night" in command:
        speak("Good night, sir! Have a great rest!")

    elif "open google" in command:
        webbrowser.open("https://google.com")

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "open python" in command:
        webbrowser.open("https://python.com")

    elif command.startswith("play"):
        importlib.reload(musicLibrary)
        parts = command.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            link = musicLibrary.music.get(song.lower())
            if link:
                speak(f"Playing {song} now.")
                webbrowser.open(link)
            else:
                speak("Song not found in the library.")
        else:
            speak("Please specify the song to play.")

    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            for article in data['articles']:
                speak(article['title'])
        else:
            speak("I am unable to fetch the news right now.")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    elif "who are you" in command or "what is your name" in command:
        speak("I am MAX, your personal assistant.")

    elif "how r u" or "how are you"in command:
        speak("I'm just a program, but I'm here to assist you!")

    else:
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing MAX...")

    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if word.lower() in ["MAX", "hey max","hey MAX","max","hemax"]:
                stop_speaking()  # Stop any ongoing speech
                listening_for_command = True  # Set the flag to true
                speak("Yes, what can I help you with?")
                
                with sr.Microphone() as source:
                    print("MAX Active...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    print("Command:", command)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Google Speech Recognition error; {e}")
