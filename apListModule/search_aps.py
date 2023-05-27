import subprocess
import re
from tabulate import tabulate

def scan_access_points(interface='wlan0'):
    cmd = ['iwlist', interface, 'scan']
    output = subprocess.check_output(cmd).decode('utf-8')

    # Split into individual cells
    cells = re.split(r'Cell \d+ -', output)
    cells = [cell.strip() for cell in cells if cell.strip()]

    # Prepare the AP information in a structured format
    aps = []
    for cell in cells:
        address_match = re.search(r'Address:\s+(\S+)', cell)
        ssid_match = re.search(r'ESSID:"(.*?)"', cell)
        protocol_match = re.search(r'IEEE\s+(\S+)', cell)
        channel_match = re.search(r'Channel (\d+)', cell)
        frequency_match = re.search(r'Frequency:(.*?)\s', cell)
        encryption_match = re.search(r'Encryption key:(\S+)', cell)
        quality_match = re.search(r'Quality=(\d+)/\d+', cell)
        signal_level_match = re.search(r'Signal level=(-?\d+)/\d+', cell)
        ie_match = re.findall(r'IE:\s(.*?)\n', cell)

        if address_match and ssid_match and frequency_match and encryption_match and quality_match and signal_level_match and protocol_match and len(ie_match) > 0:
            address = address_match.group(1)
            ssid = ssid_match.group(1)
            frequency = frequency_match.group(1)
            encryption = encryption_match.group(1)
            quality = quality_match.group(1)
            signal_level = signal_level_match.group(1)
            channel = channel_match.group(1)
            protocol = protocol_match.group(1)
            ap = {
                'Address': address,
                'SSID': ssid,
                'Frequency': frequency,
                'Encryption': encryption,
                'Quality': quality,
                'Signal Level': signal_level,
                'Channel': channel,
                'Protocol': protocol,
                'IE': ie_match[0]
            }
            if not (ap['SSID'] is None):
                aps.append(ap)

    return aps


# Print the ap list as a table
def print_ap_list(access_points):
    print("------------AP List-------------")

    # Header of table
    headers = ['#','SSID', 'Address', 'Channel', 'IE']
    # iterating ap list and print each information
    table_data = [[i, ap['SSID'], ap['Address'], ap['Channel'], ap['IE']] for i,ap in enumerate(access_points)]
    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

access_points = scan_access_points()
print_ap_list(access_points)

