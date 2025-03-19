import paramiko

def ssh_connect_and_execute(host, username, password, command):
    """
    Établit une connexion SSH et exécute une commande sur une machine distante.

    :param host: Adresse IP ou hostname de la machine distante.
    :param username: Nom d'utilisateur SSH.
    :param password: Mot de passe SSH.
    :param command: Commande à exécuter.
    :return: Résultat de la commande.
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        client.close()

        return output if output else error

    except Exception as e:
        return f"Erreur SSH: {str(e)}"
