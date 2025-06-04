# This is the typing test app - by Vince Vagay 30036567
# This version display words and user input would cycle words on screen. A timer was added.

import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("Typing Test - Vince Vagay")
window.geometry("500x400+500+70") # size and positioning x and y from the top
window.config(border=10, relief="ridge", bg="white")
window.resizable(1,1)

# paragraph holds the paragraph that the user will attempt to type out
paragraph = "This is what I'm going to type to split up into its words this is the " \
"end sentence to declare that the program is over test me"
# An array that has the paragraph split up into it's individual words
wordsArray = paragraph.split()

def countdown(count):
    if count > 0:
        # Displays the timer
        # Just for string formatting, adds a 0 as placeholder for seconds less thant 10
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

# Function that updates the words shown on screen
def line(blank):
    # Using the chunkCount variable and updating it
    global chunkCount
    # Constant variable to how many words appear at a time
    NUMWORD = 5
    # Clearing the line
    chunk = ""
    try:
        print(str(chunkCount) + str(len(wordsArray)))
        # If the amount of words exceeds the amount of words in the paragraph.
        if chunkCount >= len(wordsArray):
            print("Reached max limit")
            # Clears the entry
            typing.delete(0, tk.END)
            tk.messagebox.askokcancel(title=None, message="You reached the end")
            pass
        # Otherwise append the line to the label
        else:
            for x in range(chunkCount, (chunkCount + NUMWORD)):
                chunk = (chunk + str(wordsArray[x]) + " ")
            chunk = chunk[:-1]
            # Sets label to display the chunk of sentence
            words.config(text=chunk)
            # Clears the entry
            typing.delete(0, tk.END)
            chunkCount += NUMWORD

        print(chunkCount)
    except:
        if chunkCount == 0:
            words.config(text='Typing Test')
            pass
        else:
            print("Max limit reached")
            words.config(text=chunk)
            typing.delete(0, tk.END)
            chunkCount += NUMWORD

# The function is passed a 'blank' parameter because the entry requires a given argument
line(blank = '')
blank = ''

# Where the user will input what they've typed
typing = tk.Entry(window, font=("Verdana", 20), bg="white", width=20)
# Pressing ENTER will call the line function
typing.bind("<Return>", line)
typing.pack(pady=(10,10))

# Creates start a button
start_button = tk.Button(window, font=("Verdana", 20), fg="black", bg="green", text="Start",  command=lambda:[line(blank), countdown(59)])
start_button.pack(pady=(10,10))

# Run the main window
window.mainloop()