# Importing libraries 
import tkinter as tk

# Initializing window
root = tk.Tk()
# root.resizable(height=False, width=False)
root.title('Maze Path Finder')

# Initializing play area
play_area = tk.Frame(root, width=800, height=500, bg="white")
play_area.grid(row=0, column=0, padx=10, pady=10)

# Invisible 1x1 pixel to make button square
btn_img = tk.PhotoImage("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=")

# Defining block class for configuring 
class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.value = None # value be start, stop, block or none
        self.button = tk.Button(play_area, image = btn_img, text='', bg='white', width = 50, height=50)
        self.button.grid(row=x, column=y)
    
    def reset(self):
        self.button.configure(text='', bg='white')
        self.value = None

# Generating a grid in the play area
for x in range(1, 11):
    for y in range(1, 11):
        Block(x, y)


# Initializing selection area
selection_area = tk.Frame(root)
selection_area.grid(row=0, column=1, padx=10, pady=10)

v = tk.IntVar()

# Dictionary to create multiple buttons
func_values = {
    "start": 1,
    "stop" : 2,
    "brick" : 3,
    "reset" : 4
}

for (text, value) in func_values.items():
    tk.Radiobutton(selection_area, text=text, variable=v, value=value).pack()






root.mainloop()