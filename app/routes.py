from flask import Blueprint
from flask import render_template

# create a blueprint for a route
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')