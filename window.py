import tkinter as tk

main_window = tk.Tk()

def info_submission():
    info = input.get()
    print(info)


main_frame = tk.Frame()
title_frame = tk.Frame(0)
title_frame.pack()
main_frame.pack()


title = tk.Label(master = title_frame, text = "Fact Checker by Eesa Aamer", justify="center")
greeting = tk.Label(master = main_frame, text="Enter your fact: ", width = 12, height = 2, justify="left")
submission = tk.Button(master = main_frame, text="Submit", command = info_submission, width = 7)
input = tk.Entry(master = main_frame, width = 50)





title.grid(row=0, column=1)
greeting.grid(row=1,column=1)
input.grid(row=1,column=2)
submission.grid(row=1, column=3)



# Main loop that keeps window open
main_window.mainloop()

