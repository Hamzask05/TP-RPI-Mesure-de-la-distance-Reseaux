import socket # Importation de la bibliothèque pour gérer les communications réseau

# 1. Configuration de l'écoute UDP
IP = "0.0.0.0" # "0.0.0.0" permet d'écouter sur toutes les cartes réseau de la machine (très pratique pour éviter les erreurs d'IP)
PORT = 5005    # le port de communication défini pour le TP

# 2. Création du socket réseau
# AF_INET : indique qu'on utilise le protocole IPv4
# SOCK_DGRAM : indique qu'on utilise le protocole UDP (envoi par datagrammes) // src dans le rapport
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. Liaison du socket
# On attache notre programme à l'IP et au port configurés plus haut
sock.bind((IP, PORT))

print("Serveur UDP en écoute sur le port", PORT)

# 4. Boucle d'écoute infinie
while True:
    # La fonction recvfrom() met le programme en pause jusqu'à ce qu'un message arrive.
    # elle lit un maximum de 1024 octets (le buffer).
    # puis renvoie le message (data) et l'adresse IP de l'expéditeur (addr).
    data, addr = sock.recvfrom(1024)
    
    # affichage dans la console :
    # data.decode() permet de transformer le message brut (bytes) en texte lisible (string)
    print("Reçu de", addr, ":", data.decode())
