import socket
import struct

# Set up the socket
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
sock.bind(("wlan0", 0))  # Replace "wlan0" with your wireless interface name

# Create a set to store unique APs
aps = set()

# Continuously capture and process packets
while True:
    packet = sock.recv(2048)
    
    # Extract the type and subtype from the frame control field
    frame_control = struct.unpack('H', packet[0:2])[0]
    frame_type = (frame_control >> 2) & 0x03
    frame_subtype = (frame_control >> 4) & 0x0F
    
    # Check if it's a beacon frame
    if frame_type == 0 and frame_subtype == 8:
        # Extract the SSID from the packet
        ssid_offset = 36  # Offset to the SSID field
        ssid_length = packet[ssid_offset]  # Length of the SSID field
        ssid = packet[ssid_offset + 2 : ssid_offset + 2 + ssid_length].decode()
        
        # Add the SSID to the set of APs
        aps.add(ssid)
        
    # Display the list of nearby APs
    print("Nearby APs:")
    for ap in aps:
        print(ap)

