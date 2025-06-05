from flask import Blueprint

# create a blueprint for a route
routes = Blueprint('main', __name__)

@routes.route('/')
def home():
    return "Using Blueprints! Habit Tracker 🚀"

@routes.route('/about')
def about():
    return "Details about our Habit Tracker"