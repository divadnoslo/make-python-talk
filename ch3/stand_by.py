# Import Speech Recognition Module
import speech_recognition as sr

# Instaniate a "Recognizer" object
speech = sr.Recognizer()

# Begin Infinite Loop
while True:
    inp = ""

    # Begin to Listen:
    with sr.Microphone(device_index=4) as source:
        speech.adjust_for_ambient_noise(source)
        try:
            print("Python is listening...")
            audio = speech.listen(source)
            inp = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
        
    
    # Print what I said
    print(f"You just said: {inp}")
    
    # Break From Loop
    if inp == "stop listening":
        print("Bye!")
        break