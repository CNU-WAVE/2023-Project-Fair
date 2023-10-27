from tabulate import tabulate

def packet_parsing():
    # TO-DO: parsing function
    return

def print_packet(packets):
    # Header of table
    headers = ['Pakcet #','Source', 'Destination', 'Protocol', 'Length', 'Info']
    # iterating packet list and print each information
    table_data = [[i, packet['Source'], packet['Destination'], packet['Protocol'], packet['Length'], packet['Info']] for i,packet in enumerate(packets)]
    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

