import tkinter as t
import random as r
from PIL import ImageTk, Image

window = t.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x600")

# Picturesx
image_1 = Image.open("rock.jpeg")
rock_image = ImageTk.PhotoImage(image_1)

image_2 = Image.open("paper.jpeg")
paper_image = ImageTk.PhotoImage(image_2)

image_3 = Image.open("scissors.png")
scissors_image = ImageTk.PhotoImage(image_3)

# Create Functions
def computer():

    random_number = r.randint(1, 3)
    if random_number == 1:
        label_tester["text"] = "R"
    elif random_number == 2:
        label_tester["text"] = "P"
    elif random_number == 3:
        label_tester["text"] = "S"

def rock():

    computer()

    # Deal with choices
    if label_tester["text"] == "R":
        label_user_choice['image'] = rock_image
        label_result['text'] = "TIE"
        label_computer_choice['image'] = rock_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"
    elif label_tester["text"] == "P":
        label_user_choice['image'] = rock_image
        label_result['text'] = "COMPUTER WINS"
        label_computer_choice['image'] = paper_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"
    elif label_tester["text"] == "S":
        label_user_choice['image'] = rock_image
        label_result['text'] = "YOU WIN"
        label_computer_choice['image'] = scissors_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"

def paper():

    computer()

    # Deal with choices
    if label_tester["text"] == "R":
        label_user_choice['image'] = paper_image
        label_result['text'] = "YOU WIN"
        label_computer_choice['image'] = rock_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"
    elif label_tester["text"] == "P":
        label_user_choice['image'] = paper_image
        label_result['text'] = "TIE"
        label_computer_choice['image'] = paper_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"
    elif label_tester["text"] == "S":
        label_user_choice['text'] = paper_image
        label_result['text'] = "COMPUTER WINS"
        label_computer_choice['image'] = scissors_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"

def scissors():

    computer()

    # Deal with choices
    if label_tester["text"] == "R":
        label_user_choice['image'] = scissors_image
        label_result['text'] = "COMPUTER WINS"
        label_computer_choice['image'] = rock_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"
    elif label_tester["text"] == "P":
        label_user_choice['image'] = scissors_image
        label_result['text'] = "YOU WIN"
        label_computer_choice['image'] = paper_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"
    elif label_tester["text"] == "S":
        label_user_choice['image'] = scissors_image
        label_result['text'] = "TIE"
        label_computer_choice['image'] = scissors_image
        button_rock["state"] = "disabled"
        button_paper["state"] = "disabled"
        button_scissors["state"] = "disabled"
        button_reset["state"] = "normal"

def reset():

    label_tester["text"] = ""
    label_computer_choice['image'] = ""
    label_user_choice['image'] = ""
    label_result['text'] = "Choose..."
    button_rock["state"] = "normal"
    button_paper["state"] = "normal"
    button_scissors["state"] = "normal"
    button_reset["state"] = "disabled"

# Create Widgets
button_rock = t.Button(window, text="Rock", command = rock)
button_rock.pack()

button_paper = t.Button(window, text="Paper", command = paper)
button_paper.pack()

button_scissors = t.Button(window, text="Scissors", command = scissors)
button_scissors.pack()

label_computer_choice = t.Label(window, image="")
label_computer_choice.pack()

label_user_choice = t.Label(window, image="")
label_user_choice.pack()

label_result = t.Label(window, text="Choose...")
label_result.pack()

button_reset = t.Button(window, text="Reset", command = reset)
button_reset.pack()

label_tester = t.Label(window, text="")

window.mainloop()