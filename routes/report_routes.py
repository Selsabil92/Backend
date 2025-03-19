# routes/report_routes.py
from flask import Blueprint, jsonify

# Crée le blueprint 'reports'
reports = Blueprint('reports', __name__)

@reports.route('/generate_report', methods=['GET'])
def generate_report():
    # Logique pour générer un rapport
    return jsonify({"message": "Rapport généré avec succès!"})
