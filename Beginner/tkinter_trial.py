import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Demo")
root.geometry("400x400")

def login():
    usrname_get = usrname_entry.get()
    pswd_get = pswd_entry.get()

    if usrname_get and pswd_get: 
        new_window = tk.Toplevel(root)
        new_window.title("Sucess")
        new_window.geometry("400x400")
        tk.Label(new_window, text="You've successfully logged in!!", font=("Arial", 20)).pack(pady=20)
        tk.Button(new_window, text="OK", command=new_window.destroy). pack(pady = 10)
    
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