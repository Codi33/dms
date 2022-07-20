import signal
import socket
import sys
from os.path import exists
from threading import Thread
from time import sleep
import os

from settings import settings

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

last_time = True


class ClientThread(Thread):
    def __init__(self, client_address, client_socket):
        Thread.__init__(self)
        self.csocket = client_socket
        print("new connection:", client_address)

    def run(self) -> None:
        global last_time
        while True:
            data = self.csocket.recv(4096)
            if data == b'':  # User disconnected
                break
            msg = data.decode()
            if msg == settings.passphrase:
                last_time = True
                self.csocket.send(b'Success')
            else:
                self.csocket.send(b'Failed')
            print(msg)


def accept_clients():
    while True:
        server.listen(1)
        clisock, cliaddr = server.accept()
        newthread = ClientThread(cliaddr, clisock)
        newthread.start()


def start_server(host, port):
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    print("server started")


def close_program():
    sys.exit()


def timer(seconds):
    global last_time
    while True:
        sleep(seconds)  # TODO: Should be a better solution than sleep
        print("no time left")
        if last_time:
            last_time = False
        else:
            print('alarm')
            # Do your actions here
            if exists('module.sh'):
                os.system('./module.sh')  # chmod +x module.sh

            # force shutdown
            os.kill(os.getpid(), signal.SIGINT)  # TODO: Find another safe way to exit


def main():
    settings.init()
    start_server(settings.host, settings.port)
    accept_thread = Thread(target=accept_clients)
    accept_thread.start()  # Start accepting clients
    timer_thread = Thread(target=timer, args=[settings.hours])  # Start timer thread
    timer_thread.start()
    timer_thread.join()


if __name__ == '__main__':
    main()
