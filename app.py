# Point d'entrée principal du backend Flask 
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from routes.auth_routes import auth
from routes.scan_routes import scans
from flask_sqlalchemy import SQLAlchemy
from routes.results_routes import results
from routes.report_routes import reports
from routes.notification_routes import notifications
from config.db_config import DB_CONFIG
from config.ssh_config import ssh_connect_and_execute
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toolbox.db'  # Exemple avec SQLite, ajustez pour PostgreSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#CORS(app)

# Charger la clé secrète JWT depuis la variable d'environnement
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)

# Enregistrer les blueprints
app.register_blueprint(auth)
app.register_blueprint(scans)
app.register_blueprint(results)
app.register_blueprint(reports)
app.register_blueprint(notifications)

# Route pour la racine
@app.route('/')
def accueil():
    return "Bienvenue dans l'application Toolbox Pentest 🛠️💻🔐"

# Route pour le favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
