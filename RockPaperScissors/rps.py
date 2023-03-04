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
images = (rock_image, paper_image, scissors_image)
outcomes = {
    ("Rock", "Paper"): "COMPUTER WINS",
    ("Rock", "Scissors"): "YOU WIN",
    ("Paper", "Rock"): "YOU WIN",
    ("Paper", "Scissors"): "COMPUTER WINS",
    ("Scissors", "Rock"): "COMPUTER WINS",
    ("Scissors", "Paper"): "YOU WIN",
    ("Rock", "Rock"): "TIE",
    ("Paper", "Paper"): "TIE",
    ("Scissors", "Scissors"): "TIE",
}

# Functions
# Function that randomly chooses computer's choice
def computer():
    moves = ("Rock", "Paper", "Scissors")
    index = random.randint(0, 2)
    move = moves[index]
    label_computer_choice.configure(text=f"Computer chooses {move}")
    computer_choice_pic.configure(image=images[index])
    return move

# Function for if player chooses rock
def rock():

    # Disables all buttons except reset button
    button_rock.configure(state=tkinter.DISABLED)
    button_paper.configure(state=tkinter.DISABLED)
    button_scissors.configure(state=tkinter.DISABLED)
    button_reset.configure(state=tkinter.NORMAL)

    # Runs computer choice
    computer_move = computer()

    # Changes user selection and image to rock
    user_move = "Rock"
    user_choice_pic.configure(image=rock_image)
    label_user_choice.configure(text=f"Player Chooses {user_move}")

    # Deal with choices
    label_result.configure(text=outcomes[(user_move, computer_move)])

# Function for if player chooses paper
def paper():

    # Disables all buttons except reset button
    button_rock.configure(state=tkinter.DISABLED)
    button_paper.configure(state=tkinter.DISABLED)
    button_scissors.configure(state=tkinter.DISABLED)
    button_reset.configure(state=tkinter.NORMAL)

    # Runs computer choice
    computer_move = computer()

    # Changes user selection and image to rock
    user_move = "Paper"
    user_choice_pic.configure(image=paper_image)
    label_user_choice.configure(text=f"Player Chooses {user_move}")

    # Deal with choices
    label_result.configure(text=outcomes[(user_move, computer_move)])

# Function for if player chooses scissors
def scissors():

    # Disables all buttons except reset button
    button_rock.configure(state=tkinter.DISABLED)
    button_paper.configure(state=tkinter.DISABLED)
    button_scissors.configure(state=tkinter.DISABLED)
    button_reset.configure(state=tkinter.NORMAL)

    # Runs computer choice
    computer_move = computer()

    # Changes user selection and image to rock
    user_move = "Scissors"
    user_choice_pic.configure(image=scissors_image)
    label_user_choice.configure(text=f"Player Chooses {user_move}")

    # Deal with choices
    label_result.configure(text=outcomes[(user_move, computer_move)])

# Resets entire game
def reset():

    # Enables all buttons except reset button
    button_rock.configure(state=tkinter.NORMAL)
    button_paper.configure(state=tkinter.NORMAL)
    button_scissors.configure(state=tkinter.NORMAL)
    button_reset.configure(state=tkinter.DISABLED)

    # Clears images and text labels
    computer_choice_pic.configure(image="")
    user_choice_pic.configure(image="")
    label_result.configure(text="Choose...")
    label_computer_choice.configure(text="")
    label_user_choice.configure(text="")

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
