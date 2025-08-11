import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")

# Add widgets to frame1 and frame2 here

# Button to switch to frame2
switch_btn = tk.Button(frame1, text="Go to Frame 2", command=frame2.tkraise)
switch_btn.pack()

# Button to switch to frame1
back_btn = tk.Button(frame2, text="Back to Frame 1", command=frame1.tkraise)
back_btn.pack()

frame1.tkraise()  # Show frame1 first

root.mainloop()