# Import Speech Recognition Module
import webbrowser as wb
import speech_recognition as sr

# Define voice_to_text function
def voice_to_text():
    voice_input = ""
    with sr.Microphone(device_index=4) as source:
        speech.adjust_for_ambient_noise(source)
        try:
            #clear_screen()
            print("Python is listening...")
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
        
        # Return Text
        return voice_input
        
# Define Clear Spyder Terminal
def clear_screen():
    print("\033[H\033[J") 

#==============================================================================
# Instaniate a "Recognizer" object
speech = sr.Recognizer()

# Begin Infinite Loop

    # Get Some Voice Input
    inp = voice_to_text()    

    # Print what I said
    print(f"You just said: {inp}")
    
    # Break From Loop
    if inp == "stop listening":
        print("Bye!")
        break
    elif "browser" in inp:
        inp = inp.replace('browser ','')
        wb.open("http://"+inp)
        continue
    elif "Google" in inp:
        inp = inp.replace('Google','')
        wb.open("http://google.com/search?q="+inp)
        continue
    elif "search" in inp:
        inp = inp.replace('search','')
        wb.open("http://google.com/search?q="+inp)
        continue
        
    
