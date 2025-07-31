from flask import Flask

app = Flask(__name__)

# import and register blueprints
from app.routes import main_bp
app.register_blueprint(main_bp)