from app import app
from flask import render_template
@app.route('/')
def home():
    foods_list = ['ramen', 'sushi', 'tortas', 'tamales', 'arroz con leche', 'spicy bulgogi']
    return render_template('index.html', foods=foods_list)