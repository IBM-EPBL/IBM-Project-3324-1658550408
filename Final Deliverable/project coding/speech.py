import speech_recognition as sr    

def speech_to_text():              
   
   r = sr.Recognizer()               
   with sr.Microphone() as source: 
       try:
                                 
          audio_data = r.listen(source)
          print("Recognizing...")
          text = r.recognize_google(audio_data)
          print(text)
        
       except sr.UnknownValueError:   
          print("Could not understand your voice")
        
       except sr.RequestError as e:    
          print("Speak Error or your are in offline".format(e))

if __name__=="__main__":               
    speech_to_text()                   