import sys
from scapy.all import *
from tabulate import tabulate

packet_number = 0  # 패킷 개수
capture_time = input("Time: ")  # 시간
protocols = {1: 'icmp', 6: 'tcp', 17: 'udp'}




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
        table = tabulate(combined_data,  tablefmt="grid")
        print(table)
# 초기화 함수 호출
capture_init()
print("Capture end")

