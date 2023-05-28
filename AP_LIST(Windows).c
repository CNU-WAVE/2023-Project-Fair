#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <windows.h>
#include <wlanapi.h>
#include <wtypes.h>


#pragma comment(lib, "wlanapi.lib")

#define MAX_APS 100 // 최대 100개

int main() {
    HANDLE handle;
    PWLAN_INTERFACE_INFO_LIST interfaceList; // 인터페이스
    PWLAN_AVAILABLE_NETWORK_LIST networkList; // 리스트

    unsigned long version;
    unsigned long error;
    // 이런걸 할땐 unsigned long 보단 DWORD을 많이 사용한다는데 
    // 따라가보니 DWORD = typedef unsigned long ...


    // 핸들 생성
    error = WlanOpenHandle(2, NULL, &version, &handle);
    if (error != ERROR_SUCCESS) { printf("초기화 실패. 에러\n"); return 1; }
    // 인터페이스 목록 가져오기
    error = WlanEnumInterfaces(handle, NULL, &interfaceList);
    if (error != ERROR_SUCCESS) {
        printf("인터페이스 못가져옴... 에러");
        WlanCloseHandle(handle, NULL);
        return 1;
    }
    // 스캔 수행
    error = WlanScan(handle, &(interfaceList->InterfaceInfo[0].InterfaceGuid), NULL, NULL, NULL);
    if (error != ERROR_SUCCESS) {
        printf("스캔 에러");
        WlanFreeMemory(interfaceList);
        WlanCloseHandle(handle, NULL);
        return 1;
    }
    error = WlanGetAvailableNetworkList(handle, &(interfaceList->InterfaceInfo[0].InterfaceGuid), 0, NULL, &networkList);
    if (error != ERROR_SUCCESS) {
        printf("??");
        WlanFreeMemory(interfaceList);
        WlanCloseHandle(handle, NULL);
        return 1;
    }

    // 결과 출력

    printf("=============================================================\n");

    int count = 0;

    char test[MAX_APS][32]; // 중복 검사하기 위해서
    memset(test, 0, sizeof(test));

    for (int i = 0; i < networkList->dwNumberOfItems; i++) {
        if (count >= MAX_APS)break; // 최대 100개까지 출력
        PWLAN_AVAILABLE_NETWORK network = &(networkList->Network[i]);
        //중복검사
        int check = 0;
        for (int j = 0; j < count; j++) {
            if (strcmp((const char*)network->dot11Ssid.ucSSID, test[j]) == 0) { // 현재 돌고있는게 이때까지 나온거 비교해서 있는지? 확인
                check = 1; // ex) SJ 2.4 SS 2.4 SJ 2.4 로 총 3개가 있다고 하고  SS2.4가 들어오면 SS2.4가 있으니 check = 1
                break;
            }
        }
        if (check) continue;  // 중복 패스 
        strncpy(test[count], (const char*)network->dot11Ssid.ucSSID, 32 - 1); // 복사
       // printf("\t %d %d\n", network->dot11DefaultAuthAlgorithm, network->dot11DefaultCipherAlgorithm);??
        if (!strcmp((const char*)network->dot11Ssid.ucSSID, "") || !strcmp((const char*)network->dot11Ssid.ucSSID, " "))
            printf("\t[SSID] 알 수 없음\t[Signal] %d\n", network->wlanSignalQuality); // ????? 뭔지 모르겠음.... 왜 공백인지..
        else
            printf("\t[SSID] %s\t[Signal] %d\n", network->dot11Ssid.ucSSID, network->wlanSignalQuality);

        
        //? 중복
        count++;
    }
    printf("=============================================================\n");
    printf("\t\t\t찾은 AP 수 %d\n", count);
    printf("=============================================================\n");
    //음... 1개가 뜨거나 20개가 뜨거나 18개가 뜨거나 하는데 이유 모르겠네...
    //핸들 메모리등 초기화 
    WlanFreeMemory(networkList);
    WlanFreeMemory(interfaceList);
    WlanCloseHandle(handle, NULL);

    return 0;
}
