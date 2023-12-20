from scapy.all import sniff

# Inspects the IP layer of the packets and prints information about source IP, destination IP, and the protocol used
def packet_callback(packet):
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")


# Sniff network packets
def start_sniffing(interface='eth0', count=10):
    print(f"Sniffing {count} packets on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, count=count)