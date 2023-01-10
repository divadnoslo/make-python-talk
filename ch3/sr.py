# Import Speech Recognition Module
import speech_recognition as sr

# Instaniate a "Recognizer" object
speech = sr.Recognizer()

# Not sure what this does exactly
with sr.Microphone(device_index=4) as source:
    speech.adjust_for_ambient_noise(source)
    print("Python is listening...")
    audio = speech.listen(source)
    inp = speech.recognize_google(audio)
    
# Print what I said
print(f"You just said: {inp}")