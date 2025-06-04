# This is the typing test app - by Vince Vagay 30036567
# This update was for resetting the program to its initial state with a reset button
# Once the timer reaches 0, it will display the user's WPM and Accuracy
# The timer has been improved so that the active timer can be canceled and reset
# Choosing the time has yet to be implemented
# This reaches the minimum viable product with the exception of 
        # having a short paragraph for the user to type
        # choosing the timer
        # UI incomplete(designed)

import tkinter as tk
from tkinter import messagebox


# Create window
window = tk.Tk()
window.title("Typing Test - Vince Vagay")
window.geometry("500x500+500+70") # size and positioning x and y from the top
window.config(border=10, relief="ridge", bg="white")
window.resizable(1,1)


# 'paragraph' holds the paragraph that the user will attempt to type out
paragraph = "This is what I'm going to type to split up into its words this is the " \
"end sentence to declare that the program is over test me"
# An array that has the paragraph split up into its individual words
wordsArray = paragraph.split()

# variable that will count how many words the user has correctly matched with the line
wordsMatched = 0

# A variable that holds how much time the user wants to do the test in(in seconds) - Although changing this will occur in a future update
userTime = 60

# variable that holds the seconds the user has to do the test
count = userTime

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
                    # For testing purposes - printing out the correct words matched out of how many words attempted
                    # When on the last line it will print the words matched out of the total words available
                    if (chunkCount) <= len(wordsArray):
                        print("Words matched: ", wordsMatched, "/", chunkCount)
                        accuracy.config(text=str(f"Accuracy: {((wordsMatched / chunkCount) * 100):.2f} %"))
                        print(f"Accuracy: {((wordsMatched / chunkCount) * 100):.2f}%")
                    else:
                        print("Words matched: ", wordsMatched, "/", len(wordsArray))
                        accuracy.config(text=str(f"Accuracy: {((wordsMatched / len(wordsArray)) * 100):.2f} %"))
                        print(f"Accuracy: {((wordsMatched / len(wordsArray)) * 100):.2f}%")

            # To avoid dividing with 0
            if wordsMatched != 0:
                # To calculate and display the words per minute according to the words matched, per time the user chose
                wpm.config(text=f"WPM: {int(wordsMatched / (count / 60))}")
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
    typing.delete(0, tk.END)
    # Changes the timer to display that the time is up
    timer1.config(text="Time's up!")
    # Messagebox displaying the user's words per minute and accuracy
    messagebox.showinfo("Results", f"{wpm.cget("text")}, {accuracy.cget("text")}")
    # Disables the user from entering anything in the input entry box
    typing.config(state='disabled')

        

# Function for checking if the timer was already active, it will cancel the active timer and start a new timer
def start_timer():
    global activeTimer
    # Cancel previous timer if running
    if activeTimer is not None:
        window.after_cancel(activeTimer)
    countdown(userTime)  # Start countdown with the time the user chooses

# Timer label
timer1 = tk.Label(font=("Verdana", 20), fg="black", bg="white", text="[01:00]")
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
            check()
            print("Reached max limit") # For testing purposes, when the last line is reached
            # Clears the entry
            typing.delete(0, tk.END)
            # Displays a messagebox to the user that they have reached the end
            messagebox.showinfo(None,"You reached the end")
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
    start_button.config(state="disabled")
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
    # Enables the start button again
    start_button.config(state="normal")
    # Reseting variables and widgets to starting state
    chunkCount = 0
    chunk = ''
    wordsMatched = 0
    count = userTime
    words.config(text="Typing Test")
    wpm.config(text="WPM:   ")
    accuracy.config(text="Accuracy:    %")
    # Reset timer
    # Cancel previous timer if running
    if activeTimer is not None:
        window.after_cancel(activeTimer)
    # Note the user can not change the time in this version
    # For testing purposes the time has been set to 30 seconds
    timer1.config(text="[01:00]")
    

# Where the user will input what they've typed
typing = tk.Entry(window, font=("Verdana", 20), bg="white", width=20, state="disabled")
# Pressing ENTER will call the line function
typing.bind("<Return>", line)
typing.pack(pady=(10,10))


# Creates start a button
start_button = tk.Button(window, font=("Verdana", 20), fg="black", bg="green", text="Start",  command=lambda:[line(blank=''), start_timer(), start()])
start_button.pack(pady=(10,10))

# Creates start a button
reset_button = tk.Button(window, font=("Verdana", 20), fg="black", bg="green", text="Reset",  command=lambda:[end()])
reset_button.pack(pady=(10,10))


# Displays words per minutes
wpm = tk.Label(font=("Verdana", 20), fg="black", bg="white", text="WPM:   ")
wpm.pack(pady=(10,10))


# Displays accuracy of input words
accuracy = tk.Label(font=("Verdana", 20), fg="black", bg="white", text="Accuracy:    %")
accuracy.pack(pady=(10,10))


# Run the main window
window.mainloop()
