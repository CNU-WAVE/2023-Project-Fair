#include <stdio.h>
#include <iwlib.h>

#define MAX_APS 100

int main() {
    wireless_scan_head scan_result;
    wireless_scan* scan_list;
    iwrange range;
    int sock;
    int count = 0;

    sock = iw_sockets_open();
    if (sock == -1) {
        perror("iw_sockets_open");
        return 1;
    }

    if (iw_get_range_info(sock, "wlan0", &range) < 0) {
        perror("ERROR");
        iw_sockets_close(sock);
        return 1;
    }
    if (iw_scan(sock, "wlan0", range.we_version_compiled, &scan_result) < 0) {
        perror("ERROR");
        iw_sockets_close(sock);
        return 1;
    }
    scan_list = scan_result.result;
    printf("=============================================================\n");
    while (scan_list != NULL && count < MAX_APS) {
        printf("\t[SSID] %s\n", scan_list->b.essid);
        printf("\t[Address] %02X:%02X:%02X:%02X:%02X:%02X\n", scan_list->ap_addr.sa_data[0],
            scan_list->ap_addr.sa_data[1], scan_list->ap_addr.sa_data[2], scan_list->ap_addr.sa_data[3],
            scan_list->ap_addr.sa_data[4], scan_list->ap_addr.sa_data[5]);
        printf("\t[Frequency] %d MHz\n", scan_list->b.freq);
        printf("\t[Encryption] %s\n", scan_list->b.has_key ? "Yes" : "No");
        printf("\t[Quality] %d /100\n", scan_list->stats.qual.level);
        count++;
        scan_list = scan_list->next;
    }
    printf("=============================================================\n");
    printf("\t\t\t찾은 AP 수: %d\n", count);
    printf("=============================================================\n");


    iw_sockets_close(sock);

    return 0;
}
