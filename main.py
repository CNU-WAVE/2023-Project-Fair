from dns_query_module.check_connection import check_DNS_query
from ap_list_module.search_aps import *
from setting.setting import *
from packet_analysis_module.packet import *
from getpass import getpass


if __name__ == "__main__":
    for _ in range(3):
        print()
    print("\t _       _____ _    ________")
    print("\t| |     / /   | |  / / ____/")
    print("\t| | /| / / /| | | / / __/   ")
    print("\t| |/ |/ / ___ | |/ / /___   ")
    print("\t|__/|__/_/  |_|___/_____/   \n")

    print("  Wireless Air-gap Vulnerability Examinator\n")

    print("#############      CHECK MENU      #############")
    print("  [1] Connect with WiFi")
    print("  [2] Connection of External Network")
    print("  [3] Monitoring Packet")
    print("################################################\n")

    menu = int(input("Select Menu(Number): "))
    if menu == 1:
        apList = scan_access_points()
        print_ap_list(apList)

        # if user select index of ap
        # Check that ap is vulnerable for KRACK
        # Checking Code needed
        selected_num = int(input("Select the number of AP: "))
        selected_AP = apList[selected_num]
        print()
        print("############# Selected AP #############")
        print("SSID:", selected_AP["SSID"])
        print("Address:", selected_AP["Address"])
        print("IE:", selected_AP["IE"])
        print("#######################################\n")

        passwd = getpass("Input AP's password: ")
        set_conf(selected_AP['SSID'], passwd, "./network.conf")
        print()

        connect_wifi("./network.conf")

    elif menu == 2:
        connected_ap = get_connected_ap()
        print_connected_AP(connected_ap)
        # option needed
        check_DNS_query()
        
        
    elif menu == 3:
        capture_init()
        
