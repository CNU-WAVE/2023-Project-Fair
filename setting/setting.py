import sys
import subprocess
import configparser

def get_connected_ap():
    try:
        result = subprocess.run(['iw', 'dev', 'wlan0', 'link'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Parse
        output_lines = result.stdout.split('\n')
        mac = ""
        ssid = ""
        for line in output_lines:
            if 'Connected to' in line:
                mac = line.split('to')[1]
            elif 'SSID' in line:
                ssid = line.split('SSID: ')[1]
            
        if(mac != ""):
            return {"MAC": mac, "SSID": ssid}
        else:
            return None
    except subprocess.CalledProcessError:
        return None
    

def set_conf(ssid, passwd):

    config = configparser.ConfigParser()
    config['AccessPoint'] = {'SSID':ssid, 'Password': passwd}

    with open('network.conf', 'w') as configfile:
        config.write(cofnigfile)
    print("network.conf created successfully.")
    
def read_config_file(config_file):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        ssid = config.get('AccessPoint', 'SSID')
        password = config.get('AccessPoint', 'Password')
        return ssid, password
    exception Exception as e:
        print(f"Error reading settings file: {e}")
        return None, None

def connect_wifi(config_file):
    ssid, password = read_config_file(config_file)
    if ssid and password:
        command = f"nmcli device wifi connect '{ssid} password '{password}'"
        try:
            subprocess.run(command, shell=Ture, check=True)
            print(f"Connected to '{ssid}' successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to '{ssid}'.")

    
