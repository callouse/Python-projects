import tkinter as tk 

root = tk.Tk()

def say_hello():
    label.config(text="Hello, Tkinter!")

root.title("Tkinter Demo")
root.geometry("400x400")

label = tk.Label(root, text="Click on the button below", font=("Arial", 14))
label.pack(pady=10)

btn = tk.Button(root, text="Click here", command=say_hello)
btn.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)



root.mainloop()