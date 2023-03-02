import tkinter as tk
import tkinter.colorchooser as tkColorChooser

# Create the main window
root = tk.Tk()

# Create the canvas to hold the grid
canvas = tk.Canvas(root, width=1000, height=1000, bg='white')
canvas.pack()

# Define the size of the squares
square_size = 10

# Create a dictionary to store the colors for each square
colors = {}

# Create the grid
for i in range(0, 1000, square_size):
    for j in range(0, 1000, square_size):
        # Calculate the coordinates of each square
        x1 = i
        y1 = j
        x2 = i + square_size
        y2 = j + square_size
        
        # Create the square and store its ID in the colors dictionary
        square_id = canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
        colors[square_id] = 'white'
        
        # Bind the left mouse button click event to the square
        canvas.tag_bind(square_id, '<Button-1>', lambda event, square=square_id: change_color(event, square))

# Function to change the color of a square when it is clicked
def change_color(event, square_id):
    current_color = colors[square_id]
    
    # Show a color chooser dialog box
    new_color = tkColorChooser.askcolor(parent=root, initialcolor=current_color)[1]
    if new_color is None:
        # The user clicked cancel on the color chooser dialog box
        return
    
    # Update the fill color of the square and the colors dictionary
    canvas.itemconfig(square_id, fill=new_color)
    colors[square_id] = new_color

# Run the main loop
root.mainloop()
