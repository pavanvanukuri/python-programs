import tkinter as tk

# Create window
window = tk.Tk()
window.title("Greeting App")
window.geometry("300x200")

# Input box
entry = tk.Entry(window)
entry.pack()

# Output label
label = tk.Label(window, text="")
label.pack()

# Function (logic)
def greet():
    name = entry.get()
    
    if name.strip() == "":
        label.config(text="Please enter your name")
    else:
        label.config(text="Welcome " + name)

# Button
button = tk.Button(window, text="Greet", command=greet)
button.pack()

# Run the program
window.mainloop()
