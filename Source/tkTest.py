from tkinter import LEFT, ttk
from turtle import left
from ttkthemes import ThemedTk

# Creating an app with a theme: this is the ThemedTk object
# The theme will applied to every ttk widget in your application



root = ThemedTk(theme='arc')
root.geometry('200x100')

# Get the available themes
print(root.get_themes())

# Creating a themed button
button = ttk.Button(root, text="Quit", command=root.destroy)
button.pack(side = LEFT, side = TOP)

button = ttk.Button(root, text="Qui1", command=root.destroy)
button.pack(pady=10)

button = ttk.Button(root, text="qui2", command=root.destroy)
button.pack(pady=10)

root.mainloop()