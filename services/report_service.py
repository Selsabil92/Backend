# Génération et formatage des rapports
import os 
import json
from datetime import datetime
# Vérifier si le dossier 'reports' existe, sinon le créer

if not os.path.exists('reports'):
    os.makedirs('reports')

# Fonction pour générer un rapport de scan
def generate_report(scan_results=None, vulnerabilities=None):
    """
    Génère un rapport sous forme de JSON.
    - scan_results : les résultats des scans (ex : nmap, openvas, etc.)
    - vulnerabilities : les vulnérabilités détectées lors de l'analyse
    """

    if not scan_results:
        scan_results = []  # Utiliser une liste vide si aucune donnée de scan n'est fournie
    
    if not vulnerabilities:
        vulnerabilities = []  # Utiliser une liste vide si aucune vulnérabilité n'est fournie

    # Création du rapport avec les résultats des scans et des vulnérabilités
    report = {
        "report_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scan_results": scan_results,
        "vulnerabilities": vulnerabilities,
    }

    # Sauvegarder le rapport dans un fichier JSON
    report_filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        with open(f"reports/{report_filename}", 'w') as f:
            json.dump(report, f, indent=4)
        return {
            "status": "success",
            "message": f"Report generated successfully: {report_filename}",
            "report_filename": report_filename
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
