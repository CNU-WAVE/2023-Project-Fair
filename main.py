from dns_query_module.check_connection import check_DNS_query
from ap_list_module.search_aps import *
from setting.setting import *
from getpass import getpass


if __name__ == "__main__":
    for _ in range(3):
        print()
    print("\t _       _____ _    ________")
    print("\t| |     / /   | |  / / ____/")
    print("\t| | /| / / /| | | / / __/   ")
    print("\t| |/ |/ / ___ | |/ / /___   ")
    print("\t|__/|__/_/  |_|___/_____/   \n")

    print("   Wireless AP Vulnerability Examinator\n")
    
    print("#############      CHECK MENU      #############")
    print("  [1] KRACK vulnerability")
    print("  [2] Connection of External Network")
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
        print("SSID:",selected_AP["SSID"])
        print("Address:", selected_AP["Address"])
        print("IE:", selected_AP["IE"])
        print("#######################################\n")
    
        passwd = getpass("Input AP's password: ")
        set_conf(selected_AP, passwd)
        print()
        print("Save succeeded in network.conf\n")



        #########################################
        # TODO:                                 #
        # KRACK CHECKING CODE                   #
        #########################################

        print("KRACK CHECKING CODE will be here!")
        print("Attack for", selected_AP["SSID"])
        print()
        print()

    elif menu == 2:
        connected_ap = get_connected_ap()
        print_connected_AP(connected_ap)
        # option needed
        check_DNS_query()

