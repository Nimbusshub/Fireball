#!/usr/bin/python3

"""Connection listener"""

import socket
import threading
import subprocess
import getopt
from typing import Any
from models.scanUsage import usageListener
import shlex
import fileinput

port = 0
target_ip = ''
listen = False
execute = ''
dest = ''
command = False


def Listener(args_split: list):
    """Execute and parse the commands"""

    """A key/value pair of the commands parsed"""
    try:
        opts, _ = getopt.getopt(args_split, "hle:t:p:cu:")
    except getopt.GetoptError:
        usageListener()
        return

    """Reinitializes the global variables based on users input"""
    for opt, arg in opts:
        if opt in ['-h']:
            usageListener()
        elif opt in ['-l']:
            globals()['listen'] = True
        elif opt in ['-e']:
            globals()['execute'] = arg
        elif opt in ['-t']:
            globals()['target_ip'] = arg
        elif opt in ['-p']:
            globals()['port'] = int(arg)
        elif opt in ['-c']:
            globals()['command'] = True
        elif opt in ['-u']:
            globals()['dest'] = arg

    """Check what the user wants the listener to do"""
    if listen is False and len(target_ip) > 2 and port > 0:
        buffer = input('-> ')
        buffer += '\n'

        """Transmit and sender data"""
        client_sender(buffer.encode('utf-8'))

    if listen is True and port > 0:
        """Listen for a connection"""
        server_listener()


def client_sender(buffer):
    """Sends out data to the target"""

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = client.connect_ex((target_ip, port))
    if conn == 0:
        if len(buffer):
            client.send(buffer)
        try:
            while True:
                """Receives data from connection"""
                recvData_len = 1
                response = ''

                while recvData_len:
                    recvData = client.recv(4096)
                    recvData_len = len(recvData)
                    response += recvData.decode()

                    if recvData_len < 4096:
                        break

                if response:
                    print(response)

                    """Prompt user for more data"""
                    buffer = input('-> ')  # Cmd.use_rawinput()
                    buffer += '\n'
                    client.send(buffer.encode('utf-8'))
        except KeyboardInterrupt:
            print("Session terminated")
            client.close()

    else:
        print("Connection Refused")
        client.close()


def execute_handler(command):
    command = command.strip()
    try:
        out = subprocess.check_output(
            shlex.split(command), stderr=subprocess.STDOUT, shell=True)
    except Exception:
        out = "Command cannot be executed.\r\n"

    return out


def server_listener():
    """Establishes connection"""

    """Establish the interface to listen on"""
    if not len(target_ip):
        globals()['target_ip'] = '0.0.0.0'

    print("Listening on [{}] at {}".format(target_ip, port))
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((target_ip, port))
        server.listen(5)

        while True:
            client_socket, _ = server.accept()

            """Thread for connection handling"""
            client_thread = threading.Thread(
                target=client_handler, args=(client_socket,))
            client_thread.start()

            client_thread.join()
    except Exception as err:
        print("Conection Terminated because ", err)
        server.close()
        return


def client_handler(client_socket):
    """File upload, command and shell execution handler"""

    if len(dest):
        """File uploader"""
        file_buffer = b''

        while True:
            recvData = client_socket.recv(4096)
            if not recvData:
                break
            else:
                file_buffer += recvData
                print(len(file_buffer))
        try:
            with open(dest, 'wb') as file:
                file.write(file_buffer)

            """Show if file have been written"""
            client_socket.send(
                "File saved successfully to {}".format(dest).encode())

        except Exception:
            client_socket.send(
                "Failed to save file to {}".format(dest).encode())

    elif len(execute):
        """Command execution"""
        output = execute_handler(execute)
        client_socket.send(output.encode())

    elif command:
        """Command shell execution"""
        command_buffer = b''
        while True:
            try:
                client_socket.send(b'$> ')

                while '\n' not in command_buffer.decode():
                    command_buffer += client_socket.recv(64)

                response = execute_handler(command_buffer.decode())
                if response:
                    client_socket.send(response)
                command_buffer = b''

            except Exception as err:
                print("Server Terminated because {}".format(err))
                client_socket.close()
            except KeyboardInterrupt:
                exit()
