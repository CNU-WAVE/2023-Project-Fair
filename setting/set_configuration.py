import sys

def set_conf(ap, passwd):

    file = open('network.conf', 'w')
    file.write("ctrl_interface=/var/run/wpa_supplicant\n")
    file.write("network={\n")
    file.write('\tssid=\"'+ap["SSID"]+'\"\n')
    file.write('\tkey_mgmt=FT-PSK\n')
    file.write('\tpsk=\"'+passwd+'\"\n')
    file.write('}')

    file.close()


