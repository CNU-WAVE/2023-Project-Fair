import pywifi
from pywifi import const

def get_nearby_aps():
    # Create a new instance of the WiFi interface
    wifi = pywifi.PyWiFi()

    # Get the first available wireless interface
    interface = wifi.interfaces()[0]

    # Scan for nearby APs
    interface.scan()

    # Get the scan results
    scan_results = interface.scan_results()

    # Print the details of each AP
    for ap in scan_results:
        print(f"SSID: {ap.ssid}, BSSID: {ap.bssid}, Signal: {ap.signal}, Channel: {ap.channel}")

# Call the function to get nearby APs
get_nearby_aps()

