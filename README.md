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
WPA2(Wi-Fi Protected Access II)를 사용하는 무선 폐쇄망에 대해 KRACK 취약점(CVE-2017-13077, CVE-2017-13078, CVE-2017-13082)과 외부망과의 연결을 확인하여 네트워크 보안 상태를 점검하는 도구

## 연구 배경
현재 발전소와 같은 우리나라의 핵심 국가기반시설이나 보안 유지가 중요시되는 연구소, 기업, 공장 등에서는 보안 강화를 위해 외부와 연결이 제한된 폐쇄망을 사용한다.
폐쇄망의 경우 업데이트 과정을 위해 외부와 연결해야 하므로 신속한 보안 업데이트가 이루어지기 어렵다.

- 현재 상용 중인 WPA2(Wi-Fi Protected Access II) 방식에 취약점이 존재함
- 보안 패치가 미비할 가능성이 큰 폐쇄망의 특성
- 폐쇄망은 외부망과의 연결이 치명적일 수 있다는 점

위의 세 가지 항목에 초점을 맞추어 폐쇄망 환경에서 사용되는 무선 AP 중 WPA2 방식을 사용하는 BSS(Basic Service Set)의 보안을 점검하는 도구가 필요하다고 판단하였다.

## 연구 목표
타겟 AP에 대해 KRACK의 가능성을 가늠하고 추후 프로젝트를 진행하면서 그 외의 부가적인 기능들(패킷 수집 및 분석 등)을 추가하여 폐쇄망 환경에서 무선 네트워크 보안 검사를 위해 AP 대상 보안 검사 도구를 제작하는 것을 최종 목표로 한다. 

### 기능 구현 목표
- 주변에 존재하는 AP 목록을 검색
- 사용자가 선택한 AP가 KRACK 공격에 취약한 지 판단
- 폐쇄망의 특성을 고려하여 외부망과의 연결이 보안 침해 사고로 이어질 수 있으므로 외부와 연결되어 있는 AP를 검사


해당 기능들을 제공하여 폐쇄망 환경에 대한 보안 점검이 가능



## 연구 내용
### Development Environment
```
Language: Python(3.11.2)
OS: Kali Linux(2023.1)
kernel header: Linux kali 6.1.0-kali9-amd64
python library:
```

<div>
  <div>
    <h3> 4-way handshake</h3>
    <img width="400" alt="스크린샷 2023-05-31 오후 8 05 21" src="https://github.com/CNU-WAVE/2023-Project-Fair/assets/81208791/907e36b0-7703-4f87-ba50-fc4d7d71ecfb">
  </div>
  <div>
    <h3>KRACK(Key Reinstallation Attakc</h3>
    <img width="400" alt="스크린샷 2023-05-31 오후 8 05 59" src="https://github.com/CNU-WAVE/2023-Project-Fair/assets/81208791/06149dea-b261-4527-a3f4-682f08ec93b4">
  </div>
</div>


## 기대 효과
- 무선 AP에 대해 KRACK 가능성을 판단하고, 외부망과의 연결 여부를 판별해 보안 유지가 중요한 원자력 발전소와 같은 국가기반시설이나 은행권, 연구소 등의 무선 네트워크 보안을 점검할 수 있다.
- 프로그램의 사용 결과에 따라 적절한 조처를 함으로써 폐쇄망을 안전하게 유지할 수 있다. 
- 추후 추가적인 연구를 통해 다양한 취약점들에 대해 점검할 수 있도록 하여 종합적인 보안 진단 도구를 제공해 무선 네트워크 보안 유지에 도움이 될 수 있다.

## 발표 자료
![Poster](https://github.com/CNU-WAVE/2023-Project-Fair/assets/81208791/1bc4be6f-c205-4573-8f21-26de9a8a4467)




