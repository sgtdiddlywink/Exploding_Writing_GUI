# --------------------------------------------------Import Modules-----------------------------------------------------#
from tkinter import *

# --------------------------------------------------Set CONSTANTS------------------------------------------------------#
FONT_NAME = "Arial"
FONT_HEIGHT = 12
FONT_TYPE = "bold"
BACKGROUND_COLOR = "#A5C9CA"

# Set variables
timer = 5
current_text = ""


# ------------------------------Timer Function----------------------#
def start_timer():
    global timer, current_text
    if timer > 0:
        timer -= 1
        window.after(1000, start_timer)
    else:
        check_text(initial_text=current_text, inputted_text=typed_entry_box.get())
        timer += 5
        current_text = typed_entry_box.get()


def check_text(initial_text, inputted_text):
    if initial_text == inputted_text:
        typed_entry_box.delete(0, END)
        window.after(1000, start_timer)
    else:
        window.after(1000, start_timer)


# --------------------------------------------Open Tk Window Box-------------------------------------------------------#
window = Tk()
window.title("EXPLODING WORDS!!!!!!!")
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)

# ------------------------------------------Instructions Label at the top----------------------------------------------#
label_1 = "CLICK THE START BUTTON AND START TYPING!" \
          "\nWARNING!" \
          "\nYOUR TEXT WILL DISAPPEAR AFTER 5 SECONDS OF INACTIVITY." \
          "\nSO KEEP TYPING!" \
          "\n" \
          "---------------------------------------------------------------------------------------------------\n"
instructions_label = Label(text=label_1, font=(FONT_NAME, 14, FONT_TYPE), bg=BACKGROUND_COLOR)
instructions_label.config(padx=5, pady=5)
instructions_label.grid(row=0, column=0)

# ----------------------------------------------Add start button-------------------------------------------------#
start_timer_button = Button(text="Start Timer", command=start_timer, font=(FONT_NAME, 16, FONT_TYPE))
start_timer_button.config(padx=2, pady=2)
start_timer_button.grid(row=1, column=0)

# -----------------------------------------Add entry box for the typed text--------------------------------------------#
typed_entry_box = Entry(width=100, font=(FONT_NAME, 16, FONT_TYPE), bd=5)
typed_entry_box.grid(row=2, column=0)

# -----------------------------------------------Keeps window open-----------------------------------------------------#
window.mainloop()
