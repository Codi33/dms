# test_client.py

import socks
import socket

# bkwjssoultczfqfsq4biacayd5llxipctpaslybwqqyquikywb4lm3qd.onion - phone address
# 2d4h3yo3udlpkfcechaukvuj6ntxdvee3a3enpbkdlxmiflbydckqbyd.onion - pc address


def connect_tor():
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050, True)
    conn = socks.socksocket()
    conn.connect(('2d4h3yo3udlpkfcechaukvuj6ntxdvee3a3enpbkdlxmiflbydckqbyd.onion', 5555))  # Change to your settings
    return conn


def connect_raw():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    conn.connect(('127.0.0.1', 5555))  # Change to your settings
    return conn


def main(conn=None):
    if conn:
        conn.send(b'passwd')  # passphrase
        data = conn.recv(4096)
        if data == b'Success':
            print("Success")
        elif data == b'Failed':
            print("Failed")
        else:
            print("Unknown error")


if __name__ == '__main__':
    main(connect_tor())
