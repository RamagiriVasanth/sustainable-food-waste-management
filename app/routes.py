from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

food_items = []

@app.route('/')
def index():
    return render_template('index.html', food_items=food_items)

@app.route('/add_food', methods=['POST'])
def add_food():
    food_name = request.form['food_name']
    expiration_date = request.form['expiration_date']
    
    # Adding food item to the list
    food_items.append({
        'name': food_name,
        'expiration_date': expiration_date
    })
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_items():
    food_items.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
