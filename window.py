import tkinter as tk

main_window = tk.Tk()


# Frames 
main_frame = tk.Frame()
title_frame = tk.Frame()

answer_frame = tk.Frame()
rewind_frame = tk.Frame()

def info_submission():
    info = input.get()
    main_frame.pack_forget()
    title_frame.pack_forget()
    answer_window()
    return info

def rewind():
    answer_frame.pack_forget()
    rewind_frame.pack_forget()
    intro_window()

# Fact check
accuracy = "This is the answer!"

# Components for intro window
title = tk.Label(master = title_frame, text = "Fact Checker by Eesa Aamer", justify="center")
greeting = tk.Label(master = main_frame, text="Enter your fact: ", width = 12, height = 2, justify="left")
submission = tk.Button(master = main_frame, text="Submit", command = info_submission, width = 7)
input = tk.Entry(master = main_frame, width = 50)

# Components for answer window
answer = tk.Label(master=answer_frame, text=accuracy)
rewind_time = tk.Button(master=rewind_frame, text="Click here to enter another fact!", command = rewind)

# Function that develops the answer window
def answer_window():
    # develops the frames
    answer_frame.pack()
    rewind_frame.pack()
    # develops the components in the frame
    answer.grid(row=0, column=0)
    rewind_time.grid(row=1, column=0)



# Function that develops the intro window
def intro_window():
    # develops frames
    title_frame.pack()
    main_frame.pack()
    # creates components 
    title.grid(row=0, column=1)
    greeting.grid(row=1,column=1)
    input.grid(row=1,column=2)
    submission.grid(row=1, column=3)



intro_window()
# Main loop that keeps window open
main_window.mainloop()

