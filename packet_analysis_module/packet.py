import sys
from scapy.all import *
from tabulate import tabulate

packet_number = 0  # 패킷 개수
capture_time = input("Time: ")  # 시간
protocols = {1: 'icmp', 6: 'tcp', 17: 'udp'}

# 필터링을 위한 변수
filter_protocol = None
filter_destination_ip = None
filter_source_ip = None
filtering = False

def capture_init():
    global packet_number
    print("Capture Start")
    pcap_file = sniff(prn=capture_start, timeout=int(capture_time))
    if packet_number == 0:
        print("Packet number is zero")
        sys.exit()

def capture_start(packet):
    global packet_number

    # 각 프로토콜의 데이터를 저장할 리스트 초기화
    icmp_data = []
    tcp_data = []
    udp_data = []

    if IP in packet:
        proto = packet[IP].proto
        ttl = packet[IP].ttl
        length = packet[IP].len
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # 패킷 번호 증가
        packet_number += 1

        if filtering:
            # 필터링 조건 확인
            if (filter_protocol is not None and proto != filter_protocol) or \
               (filter_destination_ip is not None and dst_ip != filter_destination_ip) or \
               (filter_source_ip is not None and src_ip != filter_source_ip):
                return  # 필터 조건에 맞지 않으면 패킷 처리 중단

        if proto in protocols:
            # ICMP
            if proto == 1:
                message_type = packet[ICMP].type
                code = packet[ICMP].code
                icmp_data.append([
                    ["packet number", packet_number, protocols[proto].upper()],
                    ["src", src_ip, "dst", dst_ip, "TTL", ttl],
                    ["type", message_type, "code", code]
                ])

            # TCP
            if proto == 6:
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                seq = packet[TCP].seq
                ack = packet[TCP].ack
                flag = packet[TCP].flags
                tcp_data.append([
                    ["packet number", packet_number, protocols[proto].upper()],
                    ["src", src_ip, "dst", dst_ip],
                    ["TTL", ttl, "Length", length],
                    ["sport", sport, "dport", dport],
                    ["seq", seq, "ack", ack, "flag", flag]
                ])

            # UDP
            if proto == 17:
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                udp_length = packet[UDP].len
                udp_data.append([
                    ["packet number", packet_number, protocols[proto].upper()],
                    ["src", src_ip, "dst", dst_ip, "TTL", ttl],
                    ["sport", sport, "dport", dport, "Packet Length", udp_length]
                ])

        if src_ip == dst_ip:
            print("Source IP and Destination IP are the same. Stopping the capture.")
            sys.exit()

        combined_data = icmp_data + tcp_data + udp_data
        table = tabulate(combined_data, tablefmt="grid")
        print(table)

# 필터링 옵션 선택
print("Filtering Options:")
print("1. Protocol")
print("2. Destination IP")
print("3. Source IP")
print("4. No Filtering")
filter_choice = input("Enter filter choice (separate by commas, e.g., 1,2,4): ")

if '4' in filter_choice.split(','):
    filtering = False
else:
    filtering = True
    for choice in filter_choice.split(','):
        if choice == '1':
            filter_protocol = int(input("Enter protocol number (1 for ICMP, 6 for TCP, 17 for UDP): "))
        elif choice == '2':
            filter_destination_ip = input("Enter destination IP address: ")
        elif choice == '3':
            filter_source_ip = input("Enter source IP address: ")
        else:
            print(f"Invalid filter choice: {choice}")

if __name__ == "__main__":
    # 초기화 함수 호출
    capture_init()
    print("Capture end")

