# 📡 Réseau de Capteurs UDP sur Raspberry Pi (Architecture Routée)

Ce projet permet de mesurer des distances à l'aide d'un capteur ultrason, de transmettre ces données via le protocole UDP à travers un réseau hybride (Ethernet + Wi-Fi Ad-Hoc), et de les afficher en temps réel sur une interface graphique.

## 🏗️ Architecture du Réseau

Le projet utilise 3 Raspberry Pi configurés de la manière suivante (Exemple basé sur le Groupe 4) :

* **RPi1 (Le Capteur) - `10.4.1.2` :** Connecté en Ethernet. Il lit les données du capteur de distance et les envoie en UDP.
* **RPi3 (Le Routeur) - `10.4.1.1` & `10.4.2.1` :** Fait le pont (IP Forwarding) entre le réseau filaire Ethernet et le réseau sans-fil.
* **RPi2 (L'Affichage) - `10.4.2.2` :** Connecté en Wi-Fi Ad-Hoc (IBSS). Il héberge un serveur UDP et une interface graphique (Tkinter) pour afficher les mesures.

## 🛠️ Prérequis

* 3 Raspberry Pi (avec Raspberry Pi OS).
* 1 Capteur de distance à ultrasons (connecté sur les broches GPIO du RPi1).
* 1 Câble Ethernet (entre RPi1 et RPi3).
* Python 3 installé sur le RPi1 et le RPi2.
* Bibliothèques Python : `RPi.GPIO` (pour le capteur), `socket`, `tkinter` (intégrée de base).

## 🚀 Configuration du Réseau

Avant de lancer les scripts, le réseau doit être configuré manuellement. 

1. **Sur le Routeur (RPi3) :**
   * Activer l'interface `eth0` et le Wi-Fi `wlan0` en mode Ad-Hoc.
   * Activer le routage : `sudo sysctl -w net.ipv4.ip_forward=1`
2. **Sur le Capteur (RPi1) :**
   * Configurer l'IP sur `eth0`.
   * Ajouter la route vers le routeur : `sudo ip route add default via 10.4.1.1`
3. **Sur l'Affichage (RPi2) :**
   * Rejoindre le Wi-Fi Ad-Hoc.
   * Ajouter la route pour répondre : `sudo ip route add default via 10.4.2.1`

*(Note : Sous Linux, le gestionnaire de réseau automatique peut parfois effacer ces règles, il faut alors les retaper).*

## 💻 Utilisation des Scripts

L'ordre de lancement est très important. Le serveur (qui écoute) doit toujours être lancé avant le client (qui envoie).

### 1. Lancer le Serveur (Sur le RPi2)
Le programme va écouter sur le port UDP `5005` (sur toutes les interfaces `0.0.0.0`) et ouvrir l'interface graphique.
```bash
python3 serveur_udp.py
