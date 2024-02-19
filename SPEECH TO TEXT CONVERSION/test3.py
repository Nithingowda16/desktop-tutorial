#Python speech to text conversion
def speech_to_text(): 
      
       #Initialise the recognizer class
       recorder = sr.Recognizer()
       try:
               duration =int(duration_entry.get())
       except:
               messagebox.showerror(message="Enter the duration")
               return
       #use the microphone
       messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")  
       with sr.Microphone() as mic: 
               #Prompt the user to record
               #Record audio from the user
               recorder.adjust_for_ambient_noise(mic)
               audio_input = recorder.listen(mic, duration=duration)   
               try:                        #Convert to text
                       text_output =recorder.recognize_google(audio_input)
                       #Display the output
                       messagebox.showinfo(message="You said:\n "+text_output)       
               except:
                        messagebox.showerror(message="Couldn't process the audio input.")