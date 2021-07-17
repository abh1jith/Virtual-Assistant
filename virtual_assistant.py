# Importing all the modules used in the code
# GUI Module
from tkinter import *
# Text-to-Speech Module
import pyttsx3
# Threading
import threading
# Speech Recognition Module
import speech_recognition as sr
# Web-Browser Module
import webbrowser
# WolframAlpha API module
import wolframalpha
# Wikipedia API module
import wikipedia



# Initialising Recogniser for Speech Recognisation
r = sr.Recognizer()
# Initialising Microphone for Speech Recognisation
mic = sr.Microphone()

# Creating a window
search = Tk()
# Set the title of the window
search.title("Virtual Assistant by Abhijith")
# Formatting the search window for better look
search.config(bg = '#282828', highlightbackground = "black", highlightthickness = 5)
# Initialising the Text-To-Speech
audio = pyttsx3.init()

# Function to search for the  query
def searchquery(question):
    # Checking if there are any specific statically defined cases by converting the query into lower case and comparing it
    lq = question.lower()
    
    # If it is "bye", we thank the user and quit the application
    if(lq == "bye"):
        audio.say("Thankyou! Have a great day.")
        audio.runAndWait()

        exit()
    # If the user wahts to open a specific website, the application opens it and terminates itself
    if("open youtube" in lq):
        audio.say("Opening Youtube")
        audio.runAndWait()

        webbrowser.open("www.youtube.com")

        exit()
    # If the user wahts to open a specific website, the application opens it and terminates itself
    if("open google" in lq):
        audio.say("Opening Google")
        audio.runAndWait()

        webbrowser.open("www.google.com")

        exit()
    # This is a specific question designed by the developer
    if(("who made you" in lq) or ("who created you" in lq)):
        audio.say("My creator is the one and only great and the greatest GOD, Abhijith. I am so grateful for him.")
        audio.runAndWait()
        return
    
    

    # We first check for the query in Wolfram Alpha.
    try:
        # WolframAlpha
        client = wolframalpha.Client(app_id = "TE4TK9-RA45ETJ6P9")

        res = client.query(question)
        ans = next(res.results).text

        # Printing the search result in a new window
        result = Tk()
        # Title of the search window
        result.title("Search Result")
        # Initialising the background colour
        result.config(bg = "White")
        # Answer
        answer = Message(result, text = ans, bg = "White", font = ("Serif", 10))
        # Also displaying the query given
        query = Label(result, text = question, bg = "White", font = ("Serif", 10))

        query.grid(row = 0, padx = 10, pady = 10)
        answer.grid(row = 2, padx = 10, pady = 10)

        # Threading for simultaenus voice
        threading.Thread(target = wolframvoice).start()
        

        result.mainloop()

    except:
        # Wikipoedia
        try:
            ans = wikipedia.summary(question, sentences = 2)
            # Printing the result in a new window
            result = Tk()
            result.title("Search Result")
            result.config(bg = "White")

            # Printing the asked query first
            query = Label(result, text = question, bg = "White", font = ("Serif", 10))
            # Then the result found from wikipedia
            answer = Message(result, text = ans, bg = "White", font = ("Serif", 10))

            query.grid(row = 0, padx = 10, pady = 10)
            answer.grid(row = 2, padx = 10, pady = 10)
            
            # Threading for simultaenus voice
            threading.Thread(target = wikivoice).start()


            result.mainloop()
        # If the query is not found anywhere, or the user is not connected to the internet, this gets run
        except:
            audio.say("I am sorry I cannot complete this operation for you.")
            audio.runAndWait()
    


# Take input using google speech recognisation
def voice_search():

    with mic as source:
        audio = r.listen(source)
        inp = r.recognize_google(audio)

    searchquery(inp)

# Taking input manually (or) explicitly
def take_input():

    inp = inputtxt.get(1.0, "end-1c")
    
    searchquery(inp)

# Intro voice message
def intro():
    say = "Hello! I'm a virtual assistant, created by Abhi. How can I help you?"

    audio.say(say)
    audio.runAndWait()

# Voice message for WolframAlpha output
def wolframvoice():

    audio.say("Here's what I've found from WolframAlpha. Hope it helps")
    audio.runAndWait()

# Voice message for Wikipedia output
def wikivoice():

    audio.say("Here's what I've found form Wikipedia. Hope it helps")
    audio.runAndWait()

# Threading for simultaenous voice output
threading.Thread(target = intro).start()

# Main GUI page
# Introduction label
intro = Label(search, text = "Hello! How can I help you?", font = ("Serif", 20), bg = "#282828", fg = "White")
intro.grid(row = 0, columnspan = 2, padx = 10, pady = 10)

# Text input widget
inputtxt = Text(search, height = 2, width = 50, border = 5, bg = "#B0C4DE", font =("Times", 15), fg = "Black", padx = 5, pady = 5)
# Text search button widget
inputbtn = Button(search, text = "Search", command = take_input, font = ("Serif", 15), bg = "#8B2252", fg = "White")
# Voice search button widget
inputvoice = Button(search, text = "Voice Search", command = voice_search, font = ("Serif", 15), bg = "#8B2252", fg = "White")

# Displaying the widgets
inputtxt.grid(row = 1, column = 0, padx = 10, pady = 10)
inputbtn.grid(row = 2, column = 0, padx = 10, pady = 10)
inputvoice.grid(row = 3, column = 0, padx = 10, pady = 10)


search.mainloop()
