import sys
import subprocess

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
    

def set_conf(ap, passwd):

    file = open('network.conf', 'w')
    file.write("ctrl_interface=/var/run/wpa_supplicant\n")
    file.write("network={\n")
    file.write('\tssid=\"'+ap["SSID"]+'\"\n')
    file.write('\tkey_mgmt=FT-PSK\n')
    file.write('\tpsk=\"'+passwd+'\"\n')
    file.write('}')

    file.close()

def print_connected_AP(connected_ap):
    if connected_ap:
        print("\nSSID:", connected_ap['SSID'])
        print("MAC:", connected_ap['MAC'])
        print()
    else:
        print("\nNo AP connected\n")
