from dns_query_module.check_connection import check_DNS_query
from ap_list_module.search_aps import *

apList = scan_access_points()
print_ap_list(apList)

# if user select index of ap
# Check that ap is vulnerable for KRACK
# Checking Code needed

# option needed
check_DNS_query()

