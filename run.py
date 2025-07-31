# imports the app instance created in __init__.py
# this works because the app/ directory becomes a python package when it contains __init__.py file
# python looks into __init__.py when importing from app/ directory
# the __init__.py file runs when the package is imported, which creates the app instance
from app import app

if __name__ == '__main__':
    app.run(debug=True)