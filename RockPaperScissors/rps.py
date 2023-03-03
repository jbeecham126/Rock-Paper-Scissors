import tkinter
import random
from PIL import ImageTk, Image

# Creates GUI
window = tkinter.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x600")

# Pictures
rock_image = ImageTk.PhotoImage(Image.open('rock.jpeg').resize((100, 100)))
paper_image = ImageTk.PhotoImage(Image.open('paper.jpeg').resize((100, 100)))
scissors_image = ImageTk.PhotoImage(Image.open('scissors.png').resize((100, 100)))

# Functions
# Function that randomly chooses computer's choice
def computer():

    random_number = random.randint(1, 3)
    if random_number == 1:
        label_computer_choice["text"] = "Computer Chooses Rock"
        computer_choice_pic['image'] = rock_image

    elif random_number == 2:
        label_computer_choice["text"] = "Computer Chooses Paper"
        computer_choice_pic['image'] = paper_image

    elif random_number == 3:
        label_computer_choice["text"] = "Computer Chooses Scissors"
        computer_choice_pic['image'] = scissors_image

# Function for if player chooses rock
def rock():

    # Disables all buttons except reset button
    button_rock["state"] = button_paper["state"] = button_scissors["state"] = "disabled"
    button_reset["state"] = "normal"

    # Runs computer choice
    computer()

    # Changes user selection and image to rock
    user_choice_pic['image'] = rock_image
    label_user_choice["text"] = "Player Chooses Rock"

    # Deal with choices
    if label_computer_choice["text"] == "Computer Chooses Rock":
        label_result['text'] = "TIE"

    elif label_computer_choice["text"] == "Computer Chooses Paper":
        label_result['text'] = "COMPUTER WINS"

    elif label_computer_choice["text"] == "Computer Chooses Scissors":
        label_result['text'] = "YOU WIN"

# Function for if player chooses paper
def paper():

    # Disables all buttons except reset button
    button_rock["state"] = button_paper["state"] = button_scissors["state"] = "disabled"
    button_reset["state"] = "normal"

    # Runs computer choice
    computer()

    # Changes user selection and image to rock
    user_choice_pic['image'] = paper_image
    label_user_choice["text"] = "Player Chooses Paper"

    # Deal with choices
    if label_computer_choice["text"] == "Computer Chooses Rock":
        label_result['text'] = "YOU WIN"

    elif label_computer_choice["text"] == "Computer Chooses Paper":
        label_result['text'] = "TIE"

    elif label_computer_choice["text"] == "Computer Chooses Scissors":
        label_result['text'] = "COMPUTER WINS"

# Function for if player chooses scissors
def scissors():

   # Disables all buttons except reset button
    button_rock["state"] = button_paper["state"] = button_scissors["state"] = "disabled"
    button_reset["state"] = "normal"

    # Runs computer choice
    computer()

    # Changes user selection and image to rock
    user_choice_pic['image'] = scissors_image
    label_user_choice["text"] = "Player Chooses Scissors"

    # Deal with choices
    if label_computer_choice["text"] == "Computer Chooses Rock":
        label_result['text'] = "COMPUTER WINS"

    elif label_computer_choice["text"] == "Computer Chooses Paper":
        label_result['text'] = "YOU WIN"

    elif label_computer_choice["text"] == "Computer Chooses Scissors":
        label_result['text'] = "TIE"

# Resets entire game
def reset():
    computer_choice_pic['image'] = user_choice_pic['image'] = ""
    label_computer_choice["text"] = label_user_choice["text"] = ""
    label_result['text'] = "Choose..."
    button_rock["state"] = button_paper["state"] = button_scissors["state"] = "normal"
    button_reset["state"] = "disabled"

# Create Widgets
button_rock = tkinter.Button(window, text="Rock", command=rock)
button_rock.pack()

button_paper = tkinter.Button(window, text="Paper", command=paper)
button_paper.pack()

button_scissors = tkinter.Button(window, text="Scissors", command=scissors)
button_scissors.pack()

label_user_choice = tkinter.Label(window, text="")
label_user_choice.pack()

user_choice_pic = tkinter.Label(window, image="")
user_choice_pic.pack()

label_computer_choice = tkinter.Label(window, text="")
label_computer_choice.pack()

computer_choice_pic = tkinter.Label(window, image="")
computer_choice_pic.pack()

label_result = tkinter.Label(window, text="Choose...")
label_result.pack()

button_reset = tkinter.Button(window, text="Reset", command=reset)
button_reset.pack()

window.mainloop()
