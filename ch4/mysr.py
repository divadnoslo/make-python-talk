# Import Speech Recognition Module
import platform
import webbrowser as wb
import speech_recognition as sr

#==============================================================================
# # Remove ALSA Error Messages
# if platform.system() == "Linux":
#     from ctypes import CFUNCTYPE, c_char_p, c_int, cdll

#     # Define error handler
#     error_handler = CFUNCTYPE\
#                     (None, c_char_p, c_int, c_char_p, c_int, c_char_p)
                    
#     # Don't do anything if there is an error message
#     def py_error_handler(filename, line, function, err, fmt):
#         pass
    
#     # Pass to C
#     c_error_handler = error_handler(py_error_handler)
#     asound = cdll.LoadLibrary('libasound.so')
#     asound.snd_lib_error_set_handler(c_error_handler)

#==============================================================================

# Define voice_to_text function
def voice_to_text(deviceIndex=4):
    
    speech = sr.Recognizer()
    voice_input = ""
    
    with sr.Microphone(device_index=deviceIndex) as source:
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