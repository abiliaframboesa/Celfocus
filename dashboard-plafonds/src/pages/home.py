# filepath: /dashboard-plafonds/dashboard-plafonds/src/pages/home.py

from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('home.html', title='Dashboard de Plafonds', message='Bem-vindo ao Dashboard de Plafonds!')