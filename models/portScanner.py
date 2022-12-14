#!/usr/bin/python3
"""Fireball port scanner"""

import socket
import subprocess
from datetime import datetime
from models.commonPorts import all_ports


def Scanner(ipaddress, ports=0, portLr=0):
    """Function that scans for open port"""

    try:
        ipv4 = socket.gethostbyname(ipaddress)
    except Exception:
        print("Error resolving the hostname. Check the hostname and try again")
        return
    subprocess.call('clear', shell=True)
    socket.setdefaulttimeout(0.5)

    no_ports = 0
    """Print Port Scanner Bannner"""
    print("=" * 80)
    print("Scan started. Please wait, this might take some seconds...")
    started_at = datetime.now()
    print("=" * 80)

    try:
        print('\nScan report for {}\n'.format(ipv4))
        if ports == 0:
            for port in range(1, 65536):
                socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                conn = socks.connect_ex((ipv4, port))
                if conn == 0:
                    print("Port {:d}:   Open".format(port), end='')
                    no_ports += 1
                    key = str(port)
                    if key in all_ports.keys():
                        print("     {}".format(all_ports[key]))
                    else:
                        print("     unknown")
            socks.close()

        elif isinstance(ports, list):
            try:
                for port in ports:
                    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(0.5)
                    conn = socks.connect_ex((ipv4, int(port)))
                    if conn == 0:
                        print("Port {:d}:   Open".format(int(port)), end='')
                        no_ports += 1
                        key = port
                        if key in all_ports.keys():
                            print("     {}".format(all_ports[key]))
                        else:
                            print("     unknown")
                socks.close()
            except Exception as err:
                print("Scan is NULL because {}".format(err))

        elif ports and portLr:
            for port in range(ports, portLr + 1):
                socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                conn = socks.connect_ex((ipv4, port))
                if conn == 0:
                    print("Port {:d}:   Open".format(port), end='')
                    no_ports += 1
                    key = str(port)
                    if key in all_ports.keys():
                        print("     {}".format(all_ports[key]))
                    else:
                        print("     unknown")
            socks.close()

        ended_at = datetime.now()
        scan_completed = ended_at - started_at
        print("\n{:d} open ports".format(no_ports))
        print("Scan Completed in {}\n".format(scan_completed))

    except socket.error:
        print("Error, couldn't scan for open ports\n")
        return

    except KeyboardInterrupt:
        socks.close()
        print("\nScan Stopped\n")
