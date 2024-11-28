from flask import Flask, jsonify, render_template, request
from network_utils import get_wireless_interfaces, set_monitor_mode, scan_wifi_networks
from attack_utils import capture_handshake, deauth_attack, ddos_attack

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/get_interfaces')
def get_interfaces():
    """API endpoint to get wireless interfaces"""
    try:
        interfaces = get_wireless_interfaces()
        return jsonify(interfaces)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/enable_monitor', methods=['POST'])
def enable_monitor():
    """API endpoint to enable monitor mode"""
    try:
        data = request.json
        interface = data['interface']
        output = set_monitor_mode(interface, enable=True)
        return jsonify({'message': f'Modo monitor activado en {interface}\n{output}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/disable_monitor', methods=['POST'])
def disable_monitor():
    """API endpoint to disable monitor mode"""
    try:
        data = request.json
        interface = data['interface']
        output = set_monitor_mode(interface, enable=False)
        return jsonify({'message': f'Modo monitor desactivado en {interface}\n{output}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/scan_networks', methods=['POST'])
def scan_networks():
    """API endpoint to scan for WiFi networks"""
    try:
        data = request.json
        interface = data['interface']
        networks = scan_wifi_networks(interface)
        return jsonify(networks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/capture_handshake', methods=['POST'])
def capture_handshake_route():
    """API endpoint to capture WPA handshake"""
    try:
        data = request.json
        output = capture_handshake(
            data['interface'],
            data['bssid'],
            data['channel']
        )
        return jsonify({'message': f'Captura completada. Resultados:\n{output}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/deauth_network', methods=['POST'])
def deauth_network():
    """API endpoint to perform deauth attack"""
    try:
        data = request.json
        output = deauth_attack(data['interface'], data['bssid'])
        return jsonify({'message': f'Ataque de desautenticación completado\n{output}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ddos_attack', methods=['POST'])
def ddos_network():
    """API endpoint to perform DDoS attack"""
    try:
        data = request.json
        output = ddos_attack(data['interface'], data['bssid'])
        return jsonify({'message': f'Ataque DDoS completado\n{output}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
