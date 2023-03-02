from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Create the grid
grid_size = 1000
square_size = 10
colors = {}

for i in range(0, grid_size, square_size):
    for j in range(0, grid_size, square_size):
        x1 = i
        y1 = j
        x2 = i + square_size
        y2 = j + square_size
        square_id = f"{i}_{j}_{random.randint(0, 1000000)}"
        colors[square_id] = 'white'

@app.route('/')
def index():
    return render_template('index.html', grid_size=grid_size, square_size=square_size, colors=colors)

@app.route('/change_color', methods=['POST'])
def change_color():
    square_id = request.form['square_id']
    current_color = colors[square_id]
    new_color = request.form['new_color']
    colors[square_id] = new_color
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
