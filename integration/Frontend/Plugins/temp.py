import speech_recognition as sr
recognizer = sr.Recognizer()

def record():
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        recognizer.dynamic_energy_threshold = True
        print("Listening...")
        audio = recognizer.listen(mic) 
        print(audio)       
        try:
            text = recognizer.recognize_google(audio, language='us-in').lower()
        except:
            return None
    print("USER -> " + text)
    return text

record()