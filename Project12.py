# This is the typing test app - by Vince Vagay 30036567
# This version enables the user to change the paragraphs that they will type against
# These stories are AI generated in the JSON file
# The JSON file called 'paragraphs' is required for this version to work

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json


# Create window
window = tk.Tk()
window.title("Typing Test - Vince Vagay")
window.geometry("750x500+250+20") # size and positioning x and y from the top
window.config(border=10, relief="ridge", bg="deepskyblue2")
window.resizable(1,1)

# A label for the combobox "Change timer"
timerLabel = tk.Label(font=("Roboto", 10, "underline", "bold"), fg="black", bg="deepskyblue2", text="Change timer")
timerLabel.grid(row = 0, column = 0, rowspan = 3, columnspan = 2)

# Combobox for choosing the time
times = tk.StringVar(window, "01:00")
timeOpt = ttk.Combobox(window, width = 5, textvariable = times, font=("Roboto", 15), state="readonly")
timeOpt.grid(row = 1, column = 0, rowspan = 1, columnspan = 2)

# User's time options
timeOpt['values'] = ('00:30','01:00','01:30','02:00')

# A variable that holds how much time the user wants to do the test in(in seconds)
userTime = 60

# variable that holds the seconds the user has to do the test
count = userTime

# Function that converts the chosen times as string and returns a int
def TimeChosen():
    try:
        setTime = timeOpt.get()
        if setTime == '00:30':
            return 30
        elif setTime == '01:00':
            return 60
        elif setTime == '01:30':
            return 90
        elif setTime == '02:00':
            return 120
        else:
            print("Unexpected time input")
            return 60
    except:
        print("Unexpected time input")
        return 60

# This section is dedicated to changing the paragraph that the user will type against
# It is pulled from a JSON file

# Load paragraphs from a JSON file
def loadParagraphs():
    try:
        with open("paragraphs.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return 

# Update the label based on the selected paragraph
def updateParagraph():
    global paragraph
    global wordsArray
    selectedParagraph = paragraphSelect.get()
    paragraphs.get(selectedParagraph)
    print((selectedParagraph), "story selected")
    # Updates the paragraph the user is typing against
    paragraph = str(paragraphs.get(selectedParagraph)[0])
    # Updates an array that has the paragraph split up into its individual words
    wordsArray = paragraph.split()

# Initializing the JSON file to import contents
paragraphs = loadParagraphs()

# A label for the combobox "Change paragraph"
paragraphLabel = tk.Label(font=("Roboto", 10, "underline", "bold"), fg="black", bg="deepskyblue2", text="Change paragraph")
paragraphLabel.grid(row = 7, column = 0, pady = 5)

# Combobox for choosing the paragraph
paragraphDefault = tk.StringVar(window, "Lighthouse")
paragraphSelect = ttk.Combobox(window, width = 10, textvariable = paragraphDefault, font=("Roboto", 12), state="readonly")
paragraphSelect.grid(row = 7, column = 0, columnspan = 2, pady = 5)

# Paragraph options - If you add stories this needs to be changed in relation to the JSON file
paragraphSelect['values'] = ('Lighthouse', 'Sweetness', 'Baker', 'Morning')

# 'paragraph' holds the paragraphs that the user will attempt to type out
# These short stories were created using Google's Gemini
# The prompt was "Generate me a story I can use for a typing test"
# Initialize the paragraph variable which holds what the user is typing against.
paragraph = str(paragraphs.get(paragraphSelect.get())[0])

# An array that has the paragraph split up into its individual words
wordsArray = paragraph.split()

# variable that will count how many words the user has correctly matched with the line
wordsMatched = 0

# Function that checks the word is correct with the line and keeps count of how many are correct
def check():
    typed = str(typing.get())
    # Importing variables
    global chunkCount
    global NUMWORD
    global wordsMatched

    # Splitting the user's input into words, stored into an array
    typedSplit = typed.split()
    # For testing purposes - Checking if the user's input was split into individual words correctly
    if chunkCount != 0:
        print(typedSplit)

        try:
            
            # For each word that the user has input, it will check with the words in an array to see if it's correct
            # It will add one to the counter variable 'wordsMatched' if it's correct
                # Error input, if the user enters more words than there are on the screen it will not check the extra words
                # The range is limited from 0 to how many words have been displayed to the user
            for x in range (0, len((words.cget("text")).split())):
                print("Typed Array: ", typedSplit[x]) # For testing purposes - seeing what the user input
                print("Word Array: ", wordsArray[(chunkCount - NUMWORD) + x]) # For testing purposes - seeing the comparison word
                # If it finds a matched word, it counts it and as to the 'wordsMatched' variable
                if typedSplit[x] == wordsArray[(chunkCount - NUMWORD) + x]:
                    print(typedSplit[x], " = ", wordsArray[(chunkCount - NUMWORD) + x]) # For testing purposes - displaying both words
                    wordsMatched += 1
                # Restricts the calculation to only accept the number of words that were displayed to the user
                if len(typedSplit) <= NUMWORD:
                # For testing purposes - printing out the correct words matched out of how many words attempted with accuracy percentage
                # 4 possibilities
                # When the user enters a partial amount or required amount of words
                    if (chunkCount) <= len(wordsArray):
                        print("Words matched: ", wordsMatched, "/", (chunkCount + len(typedSplit) - NUMWORD))
                        accuracy.config(text=str(f"Accuracy: {((wordsMatched / (chunkCount + len(typedSplit) - NUMWORD)) * 100):.2f}%"))
                        print(f"Accuracy: {((wordsMatched / (chunkCount + len(typedSplit) - NUMWORD)) * 100):.2f}%")
                # When the user reaches the end of the paragraph and only puts in a partial amount of words
                    else:
                        print("Words matched: ", wordsMatched, "/", len(wordsArray))
                        accuracy.config(text=str(f"Accuracy: {((wordsMatched / (len(wordsArray) + len(typedSplit) - NUMWORD)) * 100):.2f}%"))
                        print(f"Accuracy: {((wordsMatched / (len(wordsArray) + len(typedSplit) - NUMWORD) ))}")
                else:
                # This acts as 'catch' if the user puts in more words than there are in the displayed line, 
                # it corrects the calculation to only account for how many words were displayed to them
                    if (chunkCount) <= len(wordsArray):
                        print("Words matched: ", wordsMatched, "/", (chunkCount))
                        accuracy.config(text=str(f"Accuracy: {((wordsMatched / chunkCount) * 100):.2f}%"))
                        print(f"Accuracy: {((wordsMatched / chunkCount) * 100):.2f}%")
                # If the user is at the end of the paragraph and puts in more words than there are in the prompt
                # This case is very unlikely to happen but it can
                    else:
                        print("Words matched: ", wordsMatched, "/", len(wordsArray))
                        accuracy.config(text=str(f"Accuracy: {((wordsMatched / (len(wordsArray))) * 100):.2f}%"))
                        print(f"Accuracy: {((wordsMatched / len(wordsArray)) * 100):.2f}%")

                # To avoid dividing with 0
                if wordsMatched != 0:
                    # To calculate and display the words per minute according to the words matched, per time the user chose
                    wpm.config(text=f"WPM: {int(wordsMatched / (TimeChosen() / 60))}")
        except:
            # Except is triggered when the user hasn't input the correct amount of words as the displayed words
            print(len(typedSplit), "/", len(words.cget("text").split()), "words input")
            pass

# variable that holds the value of an active timer so it can be canceled
activeTimer = None

# Function to display a countdown timer
def countdown(count):
    global activeTimer
    if count > 0:
        # Displays the timer
        # Rounding and converting the count in seconds to minutes
        minutes = int(count / 60)
        seconds = count % 60

        # Just for string formatting, adds a 0 as placeholder for seconds less than 10
        if seconds < 10:
            timer1.config(text=f"[0{minutes}:0{seconds}]")
        else:
            timer1.config(text=f"[0{minutes}:{seconds}]")
        # After 1000ms call this function and remove one from count variable(seconds)
        activeTimer = window.after(1000, countdown, count-1)
    else:
        # Once timer hits 0, run the time up function
        finish()

def finish():
    # Runs this function to capture user's last input
    check()
    # Clears the typing entrybox and sets the focus on the reset button
    typing.delete(0, tk.END)
    reset_button.focus_set()
    # Disables the user from entering anything in the input entry box
    typing.config(state='disabled')
    # Changes the timer to display that the time is up
    timer1.config(text="Time's up!")
    # Messagebox displaying the user's words per minute and accuracy
    messagebox.showinfo("Results", f"{wpm.cget("text")}, {accuracy.cget("text")}")

# Function for checking if the timer was already active, it will cancel the active timer and start a new timer
def start_timer():
    global activeTimer
    # Cancel previous timer if running
    if activeTimer is not None:
        window.after_cancel(activeTimer)
    countdown(TimeChosen())  # Start countdown with the time the user chooses

# Displays the title of the program
title = tk.Label(window, font=("Roboto", 30, "bold"), bg="deepskyblue2", width=25, text="Typing Test")

# Timer label
timer1 = tk.Label(font=("Roboto", 25, "bold"), fg="black", bg="deepskyblue2", text="[00:00]")

# Displays the current words the user will type into the entry
words = tk.Label(font=("Verdana", 20), fg="black", bg="deepskyblue2", text="Type this text here")

# Counter variable to keep track of words in the array
chunkCount = 0
# NUMWORD is used to say how many words are displayed at a time
NUMWORD = 6
# Function that updates the words shown on screen
def line(blank):
    # Using the chunkCount variable and updating it
    global chunkCount
    # Constant variable to how many words appear at a time
    global NUMWORD
    # Clearing the line
    chunk = ""
    try:
        # If the amount of words exceeds the amount of words in the paragraph.
        if chunkCount >= len(wordsArray):
            # Checks the input by calling the check function and passing the line
            check()
            # Clears the entry
            typing.delete(0, tk.END)
            # This section is dedicated to when the user reaches the end of the paragraph before the timer finishes
            # Cancels the active timer
            window.after_cancel(activeTimer)
            words.config(text="")
            # Messagebox displaying the user's words per minute and accuracy
            messagebox.showinfo("Results", f"{wpm.cget("text")}, {accuracy.cget("text")}")
            # Disables the user from entering anything in the input entry box
            typing.config(state='disabled')
            pass
        # Otherwise append the line to the label
        else:
            # Displays a number of words NUMWORD is used to say how many words are displayed at a time
            for x in range(chunkCount, (chunkCount + NUMWORD)):
                # chunk is used to get a 'chunk' of the paragraph(a line)
                chunk = (chunk + str(wordsArray[x]) + " ")
            chunk = chunk[:-1] # Used to format the line, just removes the spacing at the end
            # Sets label to display the chunk of a sentence
            words.config(text=chunk)
            # Checks the input by calling the check function and passing the line
            check()
            # Clears the entry
            typing.delete(0, tk.END)
            # Adds number of words to display onto counter variable
            chunkCount += NUMWORD

    except:
        # On initial window load it will display 'Typing Test'
        if chunkCount == 0:
            # Sets label to display the chunk of a sentence
            words.config(text='Type this text here')
            pass
        else:
            # When the last line is reached, it will append the last line
            print("Last line reached")
            # Checks the input by calling the check function and passing the line
            check()
            # Sets label to display the chunk of a sentence
            words.config(text=chunk)
            # Clears the entry
            typing.delete(0, tk.END)
            # Adds number of words to display onto counter variable
            chunkCount += NUMWORD


# The function is passed a 'blank' parameter because the entry requires a given argument
line(blank = '')

def start():
    # Locks in the chosen time by the user
    TimeChosen()
    # Run the updated paragraph in case the user changed it
    updateParagraph()
    # Initialize the WPM and accuracy display
    wpm.config(text="WPM: 0")
    accuracy.config(text="Accuracy: 0.00 %")
    # Disables the choosing of the timer and start button
    timeOpt.config(state="disabled")
    start_button.config(state="disabled")
    paragraphSelect.config(state="disabled")
    # Points the user into the typing entrybox and allows them to type
    typing.config(state="normal")
    typing.focus_set()

# Function thats clears and resets everything
def end():
    # Importing global variables
    global chunkCount
    global chunk
    global count
    global wordsMatched
    global activeTimer
    # Clears the entry
    typing.delete(0, tk.END)
    # Disables typing, doesn't allow user input at all
    typing.config(state="disabled")
    # Takes the focus out of the typing entry box
    reset_button.focus_set()
    # Enables the start button again
    start_button.config(state="normal")
    # Enables changing the timer
    timeOpt.config(state="readonly")
    # Enables changing of paragraph
    paragraphSelect.config(state="readonly")
    # Reseting variables and widgets to starting state
    chunkCount = 0
    chunk = ''
    wordsMatched = 0
    count = userTime
    words.config(text="Type this text here")
    wpm.config(text="WPM:   ")
    accuracy.config(text="Accuracy:    %")
    # Reset timer
    # Cancel previous timer if running
    if activeTimer is not None:
        window.after_cancel(activeTimer)
    # Note the user can not change the time in this version
    # Defaulted to 1 minute
    timer1.config(text="[00:00]")
    

# Where the user will input what they've typed
typing = tk.Entry(window, font=("Verdana", 17), bg="white", width=32, state="disabled")
# Pressing ENTER will call the line function
typing.bind("<Return>", line)

# Creates start a button
start_button = tk.Button(window, font=("Verdana", 15, "bold"), fg="black", bg="deepskyblue", text="START", width=7,  command=lambda:[start(), start_timer(), line(blank='')])

# Creates start a button
reset_button = tk.Button(window, font=("Verdana", 15, "bold"), fg="black", bg="deepskyblue", text="RESET", width=7,  command=lambda:[end()])

# Displays words per minutes
wpm = tk.Label(font=("Roboto", 20, "bold"), fg="black", bg="deepskyblue2", text="WPM:   ")

# Displays accuracy of input words
accuracy = tk.Label(font=("Roboto", 20, "bold"), fg="black", bg="deepskyblue2", text="Accuracy:    %")

# Displays instructions
instructions = tk.Label(font=("Verdana", 15), fg="black", bg="deepskyblue2", text="Press [ENTER] after every line")


# Defining a grid
window.columnconfigure((0,1,2), weight = 1, uniform='a')
window.rowconfigure((0,1,2,3,4,5,6,7), weight = 1)

# Assigning widget to grid
title.grid(row = 0, column = 1, pady = 30)
timer1.grid(row = 2, column = 0, columnspan = 2)
words.grid(row = 3, column = 0, columnspan = 3, pady = 15)
typing.grid(row = 4, column = 0, columnspan= 3, pady = 15)
start_button.grid(row = 5, column = 2)
reset_button.grid(row = 5, column = 0)
wpm.grid(row = 1, column = 1, columnspan = 2)
accuracy.grid(row = 2, column = 1, columnspan = 2)
instructions.grid(row = 5, column = 0, columnspan = 3, pady = 10)


# Run the main window
window.mainloop()
