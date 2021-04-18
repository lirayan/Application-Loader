import tkinter as tk
from tkinter import Canvas, Frame, Label, Pack, filedialog , Text
import os

root = tk.Tk()

# List
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# Add apps Commands
def addApp():
    for widget in Frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select Files", filetypes=(("executables", "*.exe"), ("All Fils", "*.*")))
    apps.append(filename)
    
    print(filename)
    
    for app in apps:
        Label = tk.Label(Frame, text=app, bg="yellow", fg="black")
        Label.pack()

# Run apps Commands
def ruunApps ():
    for app in apps:
        os.startfile(app)

# clear list command
def clearApp():
    apps.clear()

# Root
Canvas = tk.Canvas(root, height=700, width=700, bg="#34495e")
Canvas.pack()

# Frame
Frame = tk.Frame(root, bg="#3498db")
Frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

# Open File Button
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="White", bg="#34495e", command=addApp)
openFile.pack()

# Run Apps Buton
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="White", bg="#34495e", command=ruunApps)
runApps.pack()

for app in apps:
    label = tk.Label(Frame, text=app)
    label.pack()

# Clear list Button
clearList = tk.Button(root, text=" Clear List ", padx=10, pady=5, fg="White", bg="#34495e", command=clearApp)
clearList.pack()

root.mainloop()

# Save file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ",")