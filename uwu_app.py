from tkinter import *

from uwu_translator import uwu

""" General variables """
outer_bg = "#333333"
inner_bg = "#e8e8e8"
label_bg = "#454545"
label_font = "Verdato 10"
label_font_color = "white"
box_bg = "white"

# Initializations for uwu app
window = Tk()
window.minsize(700, 350)
window.geometry('700x350')
window.title("English to UwU Translator")

user_input = StringVar()

def convert_input_to_uwu(ar):
    result = input_box.get(1.0, "end-1c")
    user_input.set(uwu(result))
    print(user_input)


""" Header """
# Header frame for placement reference
header_frame = Frame(bd=0, height=50, bg=outer_bg)
header_frame.pack(fill='x', side="top")
# Place future upper menu contents here (if any)

""" Footer """
# Header frame for placement reference
header_frame = Frame(bd=0, height=50, bg=outer_bg)
header_frame.pack(fill='x', side="bottom")
# Place future upper menu contents here (if any)

""" Body """
# body frame for placement reference
body_frame = Frame(bg=inner_bg)
body_frame.pack(padx=10, pady=20, fill="both", expand="yes")

""" Body - Input """
# Input frame for placement reference of other widgets
input_frame = Frame(body_frame)
input_frame.pack(side="left", fill="both", expand="yes")

""" Body - Input - Labels """
# Input label text
input_text = "INPUT TEXT TO TRANSLATE HERE"
# Header label for input box
input_label = Label(input_frame, bd=0, bg=label_bg, text=input_text, font=label_font, fg=label_font_color)
input_label.pack(side="top", fill="x", ipadx=10, ipady=10, padx=10)
# Footer label for input box
input_label = Label(input_frame, bd=0, bg=label_bg, text=uwu(input_text), font=label_font, fg=label_font_color)
input_label.pack(side="bottom", fill="x", ipadx=10, ipady=10, padx=10)

# Accepts multi-line text entry for translation
input_box = Text(input_frame, bd=0, bg=box_bg, width=1, borderwidth=20, relief="flat", font="Consolas 12")
input_box.pack(side="top", fill="both", expand="yes", padx=10)

""" Body - Output """
# Output frame for placement reference
output_frame = Frame(body_frame, bd=0)
output_frame.pack(side="right", fill="both", expand="yes")

""" Body - Output - Labels """
# Output label text
output_text = "SEE TRANSLATED TEXT HERE"
# Header label for output box
output_label = Label(output_frame, bd=0, bg=label_bg, text=output_text, font=label_font, fg=label_font_color)
output_label.pack(side="top", fill="x", ipadx=10, ipady=10, padx=10)
# Footer label for output box
output_label = Label(output_frame, bd=0, bg=label_bg, text=uwu(output_text), font=label_font, fg=label_font_color)
output_label.pack(side="bottom", fill="x", ipadx=10, ipady=10, padx=10)

""" Body - Output - Label output """
# Shows uwu translation of text entry in input box
output_box = Label(output_frame, bd=0, bg=box_bg, height=200, textvariable=user_input, font="Consolas 12", anchor="nw",
                   borderwidth=20, relief="flat")
output_box.pack(side="top", fill="both", padx=10)

window.bind("<Key>", convert_input_to_uwu)

window.mainloop()
