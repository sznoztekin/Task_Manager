from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

@app.route('/')
def index():
    return "Ana sayfa - Giriş yapın veya kayıt olun."

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
