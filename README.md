# Toolbox Pentest 🛠️💻🔐

## Description

Une application web pour automatiser les tests d'intrusion, intégrer des scans de sécurité (Nmap, OpenVAS, Metasploit), analyser les vulnérabilités et générer des rapports. Le projet inclut également une gestion des utilisateurs et des notifications.

## Prérequis

Avant de commencer, assurez-vous d'avoir les prérequis suivants installés :

- Python 3.9 ou plus récent
- PostgreSQL
- Une machine Kali Linux configurée pour effectuer les scans de sécurité

## Installation

1. Clonez ce dépôt :
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Configurez votre fichier `.env` avec vos variables d'environnement.

4. Lancez l'application Flask :
    ```bash
    flask run
    ```

## Fonctionnalités

- **Gestion des utilisateurs** : Création et authentification des utilisateurs avec JWT.
- **Scans de sécurité** : Intégration avec Nmap, OpenVAS, Metasploit pour effectuer des scans.
- **Analyse des vulnérabilités** : Détection des vulnérabilités dans les résultats des scans.
- **Notifications** : Envoi de notifications par email à l'utilisateur lorsque des résultats sont disponibles.
- **Stockage** : Utilisation de PostgreSQL pour stocker les résultats des scans et les vulnérabilités détectées.

## Contact

Pour toute question, contactez-moi à : selsabil.guennouni@supdevinci-edu.fr
