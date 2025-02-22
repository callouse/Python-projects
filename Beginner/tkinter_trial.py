import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Demo")
root.geometry("400x400")

def clear_screen(): 
    for widgets in root.winfo_children(): 
        widgets.destroy()

def go_to_home(): 
    clear_screen()
    tk.Label(root, text="Home").pack(pady=20)

    
def login():
    
    usrname_get = usrname_entry.get()
    pswd_get = pswd_entry.get()

    if usrname_get and pswd_get: 
        clear_screen()
        success_label = tk.Label(root, text="You've successfully logged in!!", font=("Arial", 20))
        success_label.grid(row=1, column=1, pady=20)
        tk.Button(root, text="OK", command=go_to_home).grid(row=2, column=1)
    
    else: 
        messagebox.showerror("Login Failed", "Please enter both Username and Password")
        

# label = tk.Label(root, text="Click on the button below", font=("Arial", 14))
# label.pack(pady=10)

# btn = tk.Button(root, text="Click here", command=say_hello)
# btn.pack(pady=10)

# entry = tk.Entry(root)
# entry.pack(pady=10)

usrname = tk.Label(root, text="Username")
pswd = tk.Label(root, text="Password")
usrname_entry = tk.Entry(root)
pswd_entry = tk.Entry(root, show="*")
btn = tk.Button(root, text="Login", command=login)

usrname.grid(row=0, column=0, padx=10, pady=5)
pswd.grid(row=1, column=0, padx=10, pady=5)
usrname_entry.grid(row=0, column=1, padx=10, pady=5)
pswd_entry.grid(row=1, column=1, padx=10, pady=5)
btn.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()