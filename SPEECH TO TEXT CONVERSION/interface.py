#Invoke call to class to view a window
window = Tk()
#Set dimensions of window and title
window.geometry("500x300")
window.title("Convert Speech to text and text to Speech: PythonGeeks")
title_label = Label(window, text="Convert Speech to text and text to Speech: PythonGeeks").pack()
#Read inputs
#text_to_speech input
text_label = Label(window, text="Text:").place(x=10,y=20)
text_entry = Text(window, width=30,height=5)
text_entry.place(x=80,y=20)
#Accent input
accent_label = Label(window, text="Accent:").place(x=10,y=110)
accent_entry = Entry(window,  width=26)
accent_entry.place(x=80,y=110)
duration_label = Label(window, text="Duration:").place(x=10,y=110)
duration_entry = Entry(window,  width=26)
duration_entry.place(x=80,y=140)
 
#Perform the functions
button1 = Button(window,text='List languages', bg = 'Turquoise',fg='Red',command=list_languages).place(x=10,y=190)
button2 = Button(window,text='Convert Text to Speech', bg = 'Turquoise',fg='Red',command=text_to_speech).place(x=130,y=190)
button3 = Button(window,text='Convert Speech to Text', bg = 'Turquoise',fg='Red',command=speech_to_text).place(x=305,y=190)
 
#close the app
window.mainloop()