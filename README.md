<h1 align="center">WPA2(Wi-FI Protected Access II) 사용 무선 폐쇄망에 대한 네트워크 보안 검사 도구</h1>

<div align="center">

  <img src="https://github.com/CNU-WAVE/.github/blob/main/profile/image/WAVE(NoBackground).png?raw=true" width="200" align="center"> 
  <h2>WAVE: Wireless Air-gap Vulnerability Examinatior</h2>
 
</div>
 
### 팀 구성
<div align="center">
  
|[윤지현](https://github.com/jhYun505)|[박근우](https://github.com/emptiness123)|[박시준](https://github.com/CanSJun)
|:---:|:---:|:---:|
|<img src="https://avatars.githubusercontent.com/u/81208791?v=4" width="120">|<img src="https://avatars.githubusercontent.com/u/37283262?v=4" width="120">|<img src="https://avatars.githubusercontent.com/u/98388286?v=4" width="120">|
|팀장|팀원|팀원|
  
</div>

### 프로젝트 개요
WPA2(Wi-Fi Protected Access II)를 사용하는 무선 폐쇄망에 대해 패킷 캡처 및 필터링과 DNS Query를 통한 외부망과의 연결을 확인을 기반으로 한 네트워크 보안 상태를 점검하는 도구

## 연구 배경
현재 발전소와 같은 우리나라의 핵심 국가기반시설이나 보안 유지가 중요시되는 연구소, 기업, 공장 등에서는 보안 강화를 위해 외부와 연결이 제한된 폐쇄망을 사용한다.
폐쇄망의 경우 업데이트 과정을 위해 외부와 연결해야 하므로 신속한 보안 업데이트가 이루어지기 어렵다.

- 현재 상용 중인 WPA2(Wi-Fi Protected Access II) 방식에 취약점이 존재함
- 보안 패치가 미비할 가능성이 큰 폐쇄망의 특성
- 폐쇄망은 외부망과의 연결이 치명적일 수 있다는 점

위의 세 가지 항목에 초점을 맞추어 폐쇄망 환경에서 사용되는 무선 AP 중 WPA2 방식을 사용하는 BSS(Basic Service Set)의 보안을 점검하는 도구가 필요하다고 판단하였다.

## 연구 목표
패킷 캡처 및 필터링과 DNS Query를 통한 외부망과의 연결을 확인을 통해 폐쇄망 환경에서 무선 네트워크 보안 검사를 위한 도구를 제작하는 것을 최종 목표로 한다. 

### 기능 구현 목표
- 주변에 존재하는 AP 목록을 검색 후 사용자 입력에 따른 연결
- 해당 네트워크 내에서 패킷을 수집하고 이를 필터링하여 비정상 패킷을 탐지함
- 폐쇄망의 특성을 고려하여 외부망과의 연결이 보안 침해 사고로 이어질 수 있으므로 외부와 연결되어 있는 AP를 검사


해당 기능들을 제공하여 폐쇄망 환경에 대한 보안 점검이 가능



## 연구 내용
### Development Environment
```
Language: Python(3.11.2)
OS: Kali Linux(2023.1)
kernel header: Linux kali 6.1.0-kali9-amd64
python library:
sacpy
tabulate
configparser
```

### 세부 내용
폐쇄망 환경에서 일어날 수 있는 공격 시도에 대해 패킷 덤프 분석을 통해 공격 가능성이 있는 패킷(예를 들어 출발지와 목적지 주소가 동일한 패킷)에 대한 정보를 사용자에게 제공하고, 폐쇄망 내에서 외부와 연결이 되면 안되는 AP가 외부망과 연결이 되어있는지, 보안 정책상 차단한 사이트에 접속이 되는지를 확인할 수 있는 도구를 제작하는 것을 최종 목표로 한다.
해당 도구에서는 주변에 존재하는 AP 목록을 검색하고, 사용자가 선택한 AP에 연결하여 패킷을 수집한다. 해당 수집과정에서 이상 패킷이 발견되는 경우, 해당 패킷에 대한 정보를 출력하여 사용자에게 전달한다. 이상 패킷의 경우 공격을 위한 패킷이 아니라 특정 취약점이 발생할 수 있는 가능성이 있는 패킷의 경우도 탐지하여 미리 경고하여 무선 네트워크 보안을 강화할 수 있도록 돕는다. 외부망 연결 확인 기능은 DNS Query를 활용하여 구현하였다.

<img width="1297" alt="image" src="https://github.com/CNU-WAVE/2023-Project-Fair/assets/81208791/160b8ee3-3757-44a6-be83-f2320e788537">
<img width="1432" alt="image" src="https://github.com/CNU-WAVE/2023-Project-Fair/assets/81208791/e13d90e6-349c-4205-901b-e795dc5da244">



## 기대 효과
- 무선 네트워크 내에서 비정상 패킷을 탐지하고, 외부망과의 연결 여부를 판별해 보안 유지가 중요한 원자력 발전소와 같은 국가기반시설이나 은행권, 연구소 등의 무선 네트워크 보안을 점검할 수 있다.
- 프로그램의 사용 결과에 따라 적절한 조처를 함으로써 폐쇄망을 안전하게 유지할 수 있다. 
- 추후 추가적인 연구를 통해 다양한 취약점들에 대해 점검할 수 있도록 하여 종합적인 보안 진단 도구를 제공해 무선 네트워크 보안 유지에 도움이 될 수 있다.

## 발표 자료
![poster](https://github.com/CNU-WAVE/.github/blob/main/profile/image/%5B%ED%8F%AC%EC%8A%A4%ED%84%B0%5DWAVE.jpg?raw=true)




