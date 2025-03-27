from flask import render_template, request, redirect, url_for
from app import app

# Temporary list to store food items (for future expansion, use a database)
food_items = []

@app.route('/')
def index():
    return render_template('index.html', food_items=food_items)

@app.route('/add_food', methods=['POST'])
def add_food():
    food_name = request.form.get('food_name')
    expiration_date = request.form.get('expiration_date')
    if food_name and expiration_date:
        food_items.append({'name': food_name, 'expiration_date': expiration_date})
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_food():
    global food_items
    food_items = []
    return redirect(url_for('index'))
