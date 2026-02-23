import socket
import threading
import tkinter as tk

# config de l'écoute UDP locale
IP = "10.5.2.2" # L'adresse IP de cette machine (RPi2)
PORT = 5005

# création et liaison du socket au port spécifié
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

# initialisation de l'interface graphique Tkinter // source et docu dans le rapport
root = tk.Tk()
root.title("Mesure de la distance")
root.geometry("400x300")

label = tk.Label(root, text="En attente", font=("Arial", 24))
label.pack(expand=True) # Ajout du pack pour centrer le texte
# pr les fonctions ci dessous les sources sont dans le rapport
# fonction qui modifie la couleur de la fenêtre selon la distance
def update_color(distance):
    if distance < 20:
        color = "red"
    elif 20 <= distance <= 50:
        color = "orange"
    else:
        color = "green"

    # màj du background et du texte
    root.configure(bg=color)
    label.configure(text=f"{distance:.2f} cm", bg=color)

# fnction tournant en arrière-plan pour recevoir les données UDP
def receive_udp():
    while True:
        data, addr = sock.recvfrom(1024) # Taille du buffer
        try:
            distance = float(data.decode())
            # Envoi de la donnée reçue à l'interface graphique en toute sécurité
            root.after(0, update_color, distance)
        except:
            pass

# lancement du Thread pour la réception UDP (Daemon permet de le fermer en quittant)
thread = threading.Thread(target=receive_udp, daemon=True)
thread.start()

# lancement de la boucle principale de l'interface
root.mainloop()
