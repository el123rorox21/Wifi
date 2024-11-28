# network_utils.py
import subprocess

def get_wireless_interfaces():
    """Get all wireless network interfaces"""
    try:
        cmd = "iwconfig"
        output = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
        interfaces = []
        for line in output.split('\n'):
            if 'IEEE 802.11' in line:
                iface = line.split()[0]
                interfaces.append({'name': iface, 'type': 'IEEE 802.11'})
        return interfaces
    except Exception as e:
        raise Exception(f"Error getting interfaces: {str(e)}")

def set_monitor_mode(interface, enable=True):
    """Enable or disable monitor mode for a given interface"""
    try:
        cmd = f"airmon-ng {'start' if enable else 'stop'} {interface}"
        output = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
        return output
    except Exception as e:
        raise Exception(f"Error setting monitor mode: {str(e)}")

def scan_wifi_networks(interface):
    """Scan for available WiFi networks"""
    try:
        cmd = f"airodump-ng {interface} --output-format csv --write /tmp/scan"
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        import time
        time.sleep(10)  # Scan for 10 seconds
        process.terminate()
        
        networks = []
        with open('/tmp/scan-01.csv', 'r') as f:
            lines = f.readlines()
            for line in lines[2:]:  # Skip header lines
                if line.strip():
                    parts = line.split(',')
                    if len(parts) > 13:
                        networks.append({
                            'bssid': parts[0].strip(),
                            'channel': parts[3].strip(),
                            'frequency': parts[4].strip(),
                            'ssid': parts[13].strip()
                        })
        
        import os
        os.remove('/tmp/scan-01.csv')
        return networks
    except Exception as e:
        raise Exception(f"Error scanning networks: {str(e)}")