# Routes pour exécuter les scans Nmap, OpenVAS, Metasploit
from flask import Blueprint, request, jsonify
from config.ssh_config import ssh_connect_and_execute
from services.report_service import generate_report

scans = Blueprint('scans', __name__)

@scans.route('/api/scans/execute', methods=['POST'])
def execute_scan():
    data = request.get_json()
    target_ip = data.get('target_ip')
    scan_type = data.get('scan_type')

    if not target_ip or not scan_type:
        return jsonify({"status": "error", "message": "Missing target_ip or scan_type"}), 400

    if scan_type == "nmap":
        command = f"nmap -sV {target_ip}"
    elif scan_type == "openvas":
        command = f"openvas-cli --target {target_ip}"
    else:
        return jsonify({"status": "error", "message": "Unsupported scan type"}), 400

    scan_output = ssh_connect_and_execute(command, 'KALI_IP', 'KALI_USER', 'path_to_private_key')
    
    # Génération du rapport
    result = generate_report(scan_results=[{"target_ip": target_ip, "scan_type": scan_type, "status": "completed", "scan_output": scan_output}])

    return jsonify(result)

