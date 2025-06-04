# This is the typing test app - by Vince Vagay 30036567
# Added checking of words input by user and counting correct matches.

import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("Typing Test - Vince Vagay")
window.geometry("500x400+500+70") # size and positioning x and y from the top
window.config(border=10, relief="ridge", bg="white")
window.resizable(1,1)

# 'paragraph' holds the paragraph that the user will attempt to type out
paragraph = "This is what I'm going to type to split up into its words this is the " \
"end sentence to declare that the program is over test me"
# An array that has the paragraph split up into it's individual words
wordsArray = paragraph.split()

# variable that will count how many words the user has correctly matched with the line
wordsMatched = 0

# Function thats checks the word is correct with the line and keeps count of how many are correct
def check(chunk):
    typed = str(typing.get())
    # Importing variables
    global chunkCount
    global NUMWORD
    global wordsMatched

    # Splitting the user's input into words, stored into an array
    typedSplit = typed.split()
    print(typedSplit) # For testing purposes - Checking if the user's input was split correctly
    try:
        # For each word that the user has input, it will check with the words in an array to see if it's correct
        # It will add one to the counter variable 'wordsMatched' if it's correct
        for x in range (0, len(typedSplit)):
            print("Typed Array: ", typedSplit[x])
            print("Word Array: ", wordsArray[(chunkCount - NUMWORD) + x])
            if typedSplit[x] == wordsArray[(chunkCount - NUMWORD) + x]:
                print(typedSplit[x], " = ", wordsArray[(chunkCount - NUMWORD) + x])
                wordsMatched += 1
                print("Words matched: ", wordsMatched)
    except:
        print("Error")

def countdown(count):
    if count > 0:
        # Displays the timer
        # Just for string formatting, adds a 0 as placeholder for seconds less than 10
        if count < 10:
            timer1.config(text=f"[00:0{count}]")
        else:
            timer1.config(text=f"[00:{count}]")
        # After 1000ms call this function and remove one from count variable(seconds)
        window.after(1000, countdown, count-1)
    else:
        # Once timer hits 0, displays message
        timer1.config(text="Time's up!")

# Timer label
timer1 = tk.Label(font=("Verdana", 20), fg="black", bg="white", text="[1:00]")
timer1.pack()

# Displays the current words the user will type into the entry
words = tk.Label(font=("Verdana", 20), fg="black", bg="white", text="Typing Test")
words.pack(pady=(10,10))

# Counter variable to keep track of words in the array
chunkCount = 0
# NUMWORD is used to say how many words are displayed at a time
NUMWORD = 5
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
            check(chunk)
            print("Reached max limit") # For testing purposes, when the last line is reached
            # Clears the entry
            typing.delete(0, tk.END)
            # Displays a messagebox to the user that they have reached the end
            tk.messagebox.askokcancel(title=None, message="You reached the end")
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
            check(chunk)
            # Clears the entry
            typing.delete(0, tk.END)
            # Adds number of words to display onto counter variable
            chunkCount += NUMWORD

        # print(chunkCount)
    except:
        # On initial window load it will display 'Typing Test'
        if chunkCount == 0:
            # Sets label to display the chunk of a sentence
            words.config(text='Typing Test')
            pass
        else:
            # When the last line is reached, it will append the last line
            print("Last line reached")
            # Sets label to display the chunk of a sentence
            words.config(text=chunk)
            # Checks the input by calling the check function and passing the line
            check(chunk)
            # Clears the entry
            typing.delete(0, tk.END)
            # Adds number of words to display onto counter variable
            chunkCount += NUMWORD

# The function is passed a 'blank' parameter because the entry requires a given argument
line(blank = '')


# Where the user will input what they've typed
typing = tk.Entry(window, font=("Verdana", 20), bg="white", width=20)
# Pressing ENTER will call the line function
typing.bind("<Return>", line)
typing.pack(pady=(10,10))

# Creates start a button
start_button = tk.Button(window, font=("Verdana", 20), fg="black", bg="green", text="Start",  command=lambda:[line(blank=''), countdown(59)])
start_button.pack(pady=(10,10))

# Run the main window
window.mainloop()