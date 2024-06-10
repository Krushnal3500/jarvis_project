try:
    # importing prebuilt modules
    from django.conf import settings
    import os
    import wave
    import logging
    import pyttsx3
    logging.disable(logging.WARNING)
    # from browsing_functionalities import 
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # disabling warnings for gpu requirements
    import time
    from keras_preprocessing.sequence import pad_sequences
    import numpy as np
    from keras.models import load_model
    from pickle import load
    import speech_recognition as sr
    import sys
    #sys.path.insert(0, os.path.expanduser('~') + "/PycharmProjects/Virtual_Voice_Assistant")
    # sys.path.insert(0, os.path.expanduser('~')+"/JARVIS- Personal Voice Assistant") # adding voice assistant directory to system path
    # sys.path.insert(0, os.path.expanduser('~')+"/INTEGRATION")
    # importing modules made for assistant
    from Frontend.Plugins.database import *
    from Frontend.Plugins.image_generation import generate_image
    # print("the")
    from Frontend.Plugins.gmail import *
    # print("hello")
    from Frontend.Plugins.API_functionalities import *
    # print("hello1")
    from Frontend.Plugins.system_operations import *
    # print("hello2")
    # from browsing_functionalities import *
    from Frontend.Plugins.browser import *
    # print("hello3")
except (ImportError, SystemError, Exception, KeyboardInterrupt) as e:
    print(f"ERROR OCCURRED WHILE IMPORTING THE MODULES ,{e}")
    exit(0)

'''
import os
import logging
import pyttsx3
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # disabling warnings for gpu requirements
from keras_preprocessing.sequence import pad_sequences
import numpy as np
from keras.models import load_model
from pickle import load
import speech_recognition as sr
import sys
#sys.path.insert(0, os.path.expanduser('~')+"/PycharmProjects/Virtual_Voice_Assistant")
sys.path.insert(0, os.path.expanduser('~')+"/Virtual_Voice_Assistant") # adding voice assistant directory to system path
# importing modules made for assistant
from database import *
from image_generation import generate_image
from gmail import send_email
from API_functionalities import *
from system_operations import *
from browsing_functionalities import *
'''

# recognizer = sr.Recognizer()

# engine = pyttsx3.init()

# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)
# # engine.setProperty('rate', 185)

# sys_ops = SystemTasks()
# tab_ops = TabOpt()
# win_ops = WindowOpt()

recognizer = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# engine.setProperty('rate', 185)

sys_ops = SystemTasks()
tab_ops = TabOpt()
win_ops = WindowOpt()

# load trained model
model = load_model('Frontend\\Data\\chat_model')

# load tokenizer object
with open('Frontend\\Data\\tokenizer.pickle', 'rb') as handle:
    tokenizer = load(handle)

# load label encoder object
with open('Frontend\\Data\\label_encoder.pickle', 'rb') as enc:
    lbl_encoder = load(enc)
    
def resp():
    return "hello world"   

def speak(text):
    print("ASSISTANT -> " + text)
    try:
        engine.say(text)
        engine.runAndWait()
    except KeyboardInterrupt or RuntimeError:
        return

def chat(text):
    # parameters
    max_len = 20
    while True:
        result = model.predict(pad_sequences(tokenizer.texts_to_sequences([text]),
                                                                          truncating='post', maxlen=max_len), verbose=False)
        intent = lbl_encoder.inverse_transform([np.argmax(result)])[0]
        return intent

def record():
    # with sr.Microphone() as mic:
        # recognizer.adjust_for_ambient_noise(mic)
        # recognizer.dynamic_energy_threshold = True
        # print("Listening...")
        # audio = recognizer.listen(mic) 
    #     print(audio)       
    #     print(type(audio)) 
    # audio = sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav'))#read audio object and transcribe  
    # print(type(audio)) 
    # with sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav')) as audio_file:
    #     # Record audio data from the file
    #     audio_data = recognizer.record(audio_file)  
    # print(type(audio_data)) 
    
    
    
    # audio = sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'blob'))#read audio object and transcribe
    
    
    
    # audio = recognizer.record(sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'blob')))
    # with audio as source:
    #     audio = recognizer.listen(source)                  
    #     result = recognizer.recognize_google(audio)
    # print("hii")
    # print(result)
    # print("123")
    
    # # with sr.AudioFile(file_path) as source:
    # #         audio_data = recognizer.record(source)
    # try:
    #     text = recognizer.recognize_google(audio_data, language='us-in').lower()
    #     print(text)
    # except Exception as e:
    #     print(e)
    #     return None
    # print("USER -> " + text)
    # return text
    
    # audio = None
    # audio = sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav'))#read audio object and transcribe
    # print(type(audio))



    # Read the WAV file
    # audio = sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav'))
    # print("rc")
    # with wave.open(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav'), 'rb') as wav_file:
    #     print("r")
    #     # Read audio data
    #     audio_data = wav_file.readframes(wav_file.getnframes())
    #     print("r1")
    #     # Create an AudioData instance
    #     audio = sr.AudioData(audio_data, wav_file.getframerate(), wav_file.getsampwidth())
    #     print("r2")
    # print("cr")
    # if audio:
    #     try:
    #         # Perform speech recognition
    #         text = recognizer.recognize_google(audio, language='en-US')
    #         print("USER -> " + text)
    #         return text.lower()
    #     except sr.UnknownValueError:
    #         return "Speech recognition could not understand audio"
    #     except sr.RequestError as e:
    #         return f"Error with the speech recognition service: {e}"
    # else:
    #     return "Error reading audio file"
    # audio = sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav'))
    # print("rc")
    # with audio as source:
    #     audio = recognizer.record(source)
    #     print("Recording completed")
    # print("cr")
    # if audio:
    #     try:
    #         # Perform speech recognition
    #         text = recognizer.recognize_google(audio, language='en-US')
    #         print("USER -> " + text)
    #         return text.lower()
    #     except sr.UnknownValueError:
    #         return "Speech recognition could not understand audio"
    #     except sr.RequestError as e:
    #         return f"Error with the speech recognition service: {e}"
    # else:
    #     return "Error reading audio file"
    
    
    # try:
    #     with wave.open(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav'), 'rb') as wav_file:
    #         # Read audio data
    #         audio_data = wav_file.readframes(wav_file.getnframes())
    #         sample_rate = wav_file.getframerate()
    #         sample_width = wav_file.getsampwidth()

    #     audio = sr.AudioData(audio_data, sample_rate, sample_width)

    #     print("Recording completed")
        
    #     # Perform speech recognition
    #     text = recognizer.recognize_google(audio, language='en-US')
    #     print("USER -> " + text)
    #     return text.lower()
    
    # # except FileNotFoundError:
    # #     return "Audio file not found"
    # # except Exception as e:
    # #     return f"Error during speech recognition: {e}"
    # except FileNotFoundError:
    #     print("Audio file not found")
    #     return None
    # except Exception as e:
    #     print("Error during speech recognition:", e)
    #     return None
    
    try:
        with sr.AudioFile(os.path.join(settings.MEDIA_ROOT, 'audio', 'temp.wav')) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='en-US')
            print("USER -> " + text)
            return text.lower()
    except FileNotFoundError:
        return "Audio file not found"
    except Exception as e:
        return f"Error during speech recognition: {e}"
    
    
    


def listen_audio():
    try:
        while True:
            print("listening")
            response = record()
            print("recording")
            if response is None:
                break
                # continue
            else:
                main(response)
                break
    except KeyboardInterrupt:
        return
    except Exception as e:
        # print("345")
        print(e)
        # return

def main(query):
        add_data(query)
        intent = chat(query)
        done = False
        if ("google" in query and "search" in query) or ("google" in query and "how to" in query) or "google" in query:
            googleSearch(query)
            return
        elif ("youtube" in query and "search" in query) or "play" in query or ("how to" in query and "youtube" in query):
            youtube(query)
            return
        elif "distance" in query or "map" in query:
            get_map(query)
            return
        if intent == "joke" and "joke" in query:
            joke = get_joke()
            if joke:
                speak(joke)
                done = True
        elif intent == "news" and "news" in query:
            news = get_news()
            if news:
                speak(news)
                done = True
        elif intent == "ip" and "ip" in query:
            ip = get_ip()
            if ip:
                speak(ip)
                done = True
        elif intent == "movies" and "movies" in query:
            speak("Some of the latest popular movies are as follows :")
            get_popular_movies()
            done = True                
        elif intent == "tv_series" and "tv series" in query:
            speak("Some of the latest popular tv series are as follows :")
            get_popular_tvseries()
            done = True
        elif intent == "weather" and "weather" in query:
            city = re.search(r"(in|of|for) ([a-zA-Z]*)", query)
            if city:
                city = city[2]
                weather = get_weather(city)
                speak(weather)
            else:
                weather = get_weather()
                speak(weather)
            done = True
        elif intent == "internet_speedtest" and "internet" in query:
            speak("Getting your internet speed, this may take some time")
            speed = get_speedtest()
            if speed:
                speak(speed)
                done = True
        elif intent == "system_stats" and "stats" in query:
            stats = system_stats()
            speak(stats)
            done = True
     
        elif intent == "image_generation" and "image" in query:
            speak("what kind of image you want to generate?")
            text = record()
            speak("Generating image please wait..")
            generate_image(text)
            done = True
        elif intent == "system_info" and ("info" in query or "specs" in query or "information" in query):
            info = systemInfo()
            speak(info)
            done = True
        elif intent == "email" and "email" in query:
            speak("Type the Receiver Email-id : ")
            receiver_id = input()
            while not check_email(receiver_id):
                speak("Invalid email id\nType reciever id again : ")
                receiver_id = input()
            speak("Tell the subject of email")
            subject = record()
            speak("tell the body of email")
            body = record()
            success = send_email(receiver_id, subject, body)
            if success:
                speak('Email sent successfully')
            else:
                speak("Error occurred while sending email")
            done = True
        elif intent == "select_text" and "select" in query:
            sys_ops.select()
            done = True
        elif intent == "copy_text" and "copy" in query:
            sys_ops.copy()
            done = True
        elif intent == "paste_text" and "paste" in query:
            sys_ops.paste()
            done = True
        elif intent == "delete_text" and "delete" in query:
            sys_ops.delete()
            done = True
        elif intent == "new_file" and "new" in query:
            sys_ops.new_file()
            done = True
        elif intent == "switch_tab" and "switch" in query and "tab" in query:
            tab_ops.switchTab()
            done = True
        elif intent == "close_tab" and "close" in query and "tab" in query:
            tab_ops.closeTab()
            done = True
        elif intent == "new_tab" and "new" in query and "tab" in query:
            tab_ops.newTab()
            done = True
        elif intent == "close_window" and "close" in query:
            win_ops.closeWindow()
            done = True
        elif intent == "switch_window" and "switch" in query:
            win_ops.switchWindow()
            done = True
        elif intent == "minimize_window" and "minimize" in query:
            win_ops.minimizeWindow()
            done = True
        elif intent == "maximize_window" and "maximize" in query:
            win_ops.maximizeWindow()
            done = True
        elif intent == "screenshot" and "screenshot" in query:
            win_ops.Screen_Shot()
            done = True
        elif intent == "stopwatch":
            pass        
        elif intent == "wikipedia" and ("tell" in query or "about" in query):
            description = tell_me_about(query)
            if description:
                speak(description)
            else:
                googleSearch(query)
            done = True
        elif intent == "math":
            answer = get_general_response(query)
            if answer:
                speak(answer)
                done = True
        elif intent == "open_website":
            completed = open_specified_website(query)
            if completed:
                done = True
        elif intent == "open_app":
            completed = open_app(query)
            if completed:
                done = True
        elif intent == "note" and "note" in query:
            speak("what would you like to take down?")
            note = record()
            take_note(note)
            done = True
        elif intent == "get_data" and "history" in query:
            get_data()
            done = True
        elif intent == "exit" and ("exit" in query or "terminate" in query or "quit" in query):
            exit(0)
        if not done:
            answer = get_general_response(query)
            if answer:
                speak(answer)
            else:
                speak("Sorry, not able to answer your query")
        return


# if __name__ == "__main__":
def start():
    try:
        listen_audio()
    except:
        print("EXITED")
        
if __name__ == "__main__":
    start()