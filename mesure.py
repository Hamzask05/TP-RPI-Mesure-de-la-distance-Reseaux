import RPi.GPIO as GPIO
import time
import socket

# def des broches GPIO selon le câblage
TRIG_PIN = 23
ECHO_PIN = 24

# config du réseau UDP
UDP_IP = "10.5.2.2"  # IP cible : le RPi2 sur le réseau Wi-Fi
UDP_PORT = 5005      # Port d'écoute du serveur

# création du socket UDP (IPv4, Datagram) // sources et documentation dans le rapport
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# configuration matérielle des broches
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True: # boucle infinie ajoutée pour lire en continu
        # génération d'une impulsion de 10 microsecondes sur TRIG
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        
        # enregistrement du temps de départ (t1) quand l'écho est à 0
        while(GPIO.input(ECHO_PIN) == 0):
            t1 = time.time()
            
        # enregistrement du temps d'arrivée (t2) quand l'écho repasse à 1
        while(GPIO.input(ECHO_PIN) == 1):
            t2 = time.time()
                
        # calcul de la distance avec la vitesse du son (34300 cm/s)
        duree = t2 - t1
        distance = (duree * 34300) / 2
        print(f"Distance mesurée : {distance:.2f} cm")
        
        # envoi de la donnée convertie en chaîne de caractères via UDP
        message = str(distance)
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
        
        # Pause avant la prochaine mesure 
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    # nettoyage des ports GPIO à la fermeture pour éviter les courts-circuits // info trouvée en ligne sur un forum src dans le rapport
    GPIO.cleanup()