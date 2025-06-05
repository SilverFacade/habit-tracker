from flask import Flask

app = Flask(__name__)

# import and register blueprints
from app.routes import routes
app.register_blueprint(routes)