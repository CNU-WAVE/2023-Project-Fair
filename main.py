from dns_query_module.check_connection import check_DNS_query
from ap_list_module.search_aps import *
from setting.set_configuration import *
from getpass import getpass


if __name__ == "__main__":
    for _ in range(5):
        print()
    print("\t _       _____ _    ________")
    print("\t| |     / /   | |  / / ____/")
    print("\t| | /| / / /| | | / / __/   ")
    print("\t| |/ |/ / ___ | |/ / /___   ")
    print("\t|__/|__/_/  |_|___/_____/   ")


    apList = scan_access_points()
    print_ap_list(apList)



    # if user select index of ap
    # Check that ap is vulnerable for KRACK
    # Checking Code needed
    selected_num = int(input("Select the number of AP: "))
    selected_AP = apList[selected_num]
    print()
    print(selected_AP)
    print("############# Selected AP #############")
    print("SSID:",selected_AP["SSID"])
    print("Address:", selected_AP["Address"])
    print("IE:", selected_AP["IE"])
    print("#######################################")
    print()
    
    passwd = getpass("Input AP's password: ")
    set_conf(selected_AP, passwd)
    print()
    print("Save successed in network.conf")
    print()





    #########################################
    # TODO:                                 #
    # KRACK CHECKING CODE                   #
    #########################################

    print("KRACK CHECKING CODE will be here!")
    print("Attack for", selected_AP["SSID"])
    print()
    print()

    # option needed
    check_DNS_query()

