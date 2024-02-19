#define functions
#text to speech conversion
def text_to_speech():
       #read inputs given by user
       text = text_entry.get("1.0","end-1c")
       language = accent_entry.get()
       #Check if the user submitted inputs
       if (len(text)<=1) | (len(language)<=0):
               messagebox.showerror(message="Enter required details")
               return     
       #Using the inputs, convert the text to speech
       speech = gTTS(text = text, lang = language, slow = False)
       #save the speech to an MP3 file
       speech.save("text.mp3")
       #Play the file using mpg123 in linux and start in windows
       os.system("mpg123 "+"text.mp3")