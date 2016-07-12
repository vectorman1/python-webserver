import errno
import logging
import os
import signal
import socket

from addons.modules import calculate
from addons.modules.respond import getrespondcode
from addons.modules.returncontent import getcontent
from addons.classes.Logger import Logger

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1024

accessLog = open('logs/access.log', 'a')

added = calculate.add(1, 6)
logger = Logger()

print calculate

def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return


def handle_request(client_connection):
    try:
        request = client_connection.recv(1024)
        print(request.decode())
        logger.logaccess(request)
        http_response = getrespondcode(request)
        http_response = http_response + getcontent(request)

        client_connection.sendall(http_response)

    except TypeError as ex:
        logger.logerror(str(ex) + '\n')
        print 'logged exception'
        


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()

        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over

if __name__ == '__main__':
    serve_forever()