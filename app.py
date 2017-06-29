#!/usr/bin/env python3

import random
from flask import Flask, request
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', **{})

@app.route('/cheeses')
def cheeses():
	availableCheeses = ('Roquefort', 'Camembert', 'Cotija', 'Chèvre', 'Feta', 'Mozzarella', 'Emmental', 'Cheddar', 'Gouda', 'Taleggio', 'Parmigiano-Reggiano', 'Manchego', 'Monterey Jack',)
	selectedCheeses = random.sample(availableCheeses, 3)
	return json.dumps(selectedCheeses)

if __name__ == '__main__':
	app.run(debug=True)
