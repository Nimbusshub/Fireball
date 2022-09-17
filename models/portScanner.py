#!/usr/bin/python3
"""Fireball port scanner"""

import socket
import subprocess
from datetime import datetime


def Scanner(ipaddress, ports=0, portLr=0):
    """Function that scans for open port"""
    subprocess.call('clear', shell=True)

    try:
        ipv4 = socket.gethostbyname(ipaddress)
    except Exception:
        print("Error resolving the hostname. Check the hostname and try again")
        return
    socket.setdefaulttimeout(2)
    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    no_ports = 0
    """Print Port Scanner Bannner"""
    print("=" * 50)
    print("Scan started. This might take some seconds")
    started_at = datetime.now()
    print("=" * 50)

    try:
        print('\nScan report for {}\n'.format(ipv4))
        if ports == 0:
            for port in range(1, 65535):
                conn = socks.connect_ex((ipv4, port))
                if conn == 0:
                    print("Port {:d}:   Open".format(port))
                    no_ports += 1
            socks.close()

        elif isinstance(ports, list):
            for port in ports:
                conn = socks.connect_ex((ipv4, int(port)))
                if conn == 0:
                    print("Port {:d}:   Open".format(int(port)))
                    no_ports += 1
            socks.close()

        elif ports and portLr:
            for port in range(ports, portLr):
                conn = socks.connect_ex((ipv4, port))
                if conn == 0:
                    print("Port {:d}:   Open".format(port))
                    no_ports += 1
            socks.close()

        ended_at = datetime.now()
        scan_completed = ended_at - started_at
        print("\n{:d} open ports".format(no_ports))
        print("Scan Completed in {}\n".format(scan_completed))

    except socket.error:
        print("Error connecting to the server\n")
        return

    except KeyboardInterrupt:
        print("Scan Stopped\n")
