import socket

def check_DNS_query(num_queries=5):

    dns_server = "8.8.8.8"  # Google DNS Server

    # Hostname to resolve
    hostname = "www.google.com"

    # Create a UDP socket
    dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout for the socket
    dns_socket.settimeout(3)

    # count the number of connection success
    external_count = 0

    for num in range(num_queries):
        # Create a DNS query for the hostname to the DNS server
        dns_query = bytearray.fromhex("AA AA 01 00 00 01 00 00 00 00 00 00")
        dns_query += bytearray.fromhex("07 65 78 61 6D 70 6C 65 03 63 6F 6D 00 00 01 00 01")

        try:
            # Send the DNS query and receive the response
            dns_socket.sendto(dns_query, (dns_server, 53))
            response, _ = dns_socket.recvfrom(1024)

            # Check if the DNS response indicates an external network connection
            if response:
                external_count += 1
        except socket.timeout:
            print("DNS query timed out. Try Count:", num+1)

    # Analyze the DNS query results
    if external_count != 0:
        print(f"Access Point connected to external network: Hostname - {hostname}, DNS Server - {dns_server}")
        return True
    else:
        print(f"Access Point is not connected to external network")
        return False


    # Close the DNS socket
    dns_socket.close()

if __name__ == "__main__":
    # Call the function to check access points
    check_DNS_query()
