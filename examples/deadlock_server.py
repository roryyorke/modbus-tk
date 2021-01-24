#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TCP server for deadlock bug example

Comment out the 'hooks.install_hook()' call, deadlock stops.

Use deadlock_client.py to provoke deadlock.
"""

import sys

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp, hooks

import time

logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

def on_before_send(args):
    #modbus_tcp.TcpServer.before_send hook
    logger.info('before_send hook 1')
    server, sock, response = args
    logger.info('before_send hook 2')
    slave = server.get_slave(1)
    logger.info('before_send hook 3')
    values = slave.get_values('0', 0)
    logger.info('before_send hook 4')


def main():
    """main"""

    hooks.install_hook('modbus_tcp.TcpServer.before_send', on_before_send)

    try:
        #Create the server
        server = modbus_tcp.TcpServer(port=5020)
        logger.info("log starting")

        server.start()

        slave_1 = server.add_slave(1)
        slave_1.add_block('0', cst.HOLDING_REGISTERS, 0, 100)

        i = 0
        while True:
            logger.info('main 1')
            slave_1.set_values('0', 0, [i])
            logger.info('main 2')
            i = (i + 1) % 2 ** 16
            logger.info('main 3')

    finally:
        server.stop()


if __name__ == "__main__":
    main()
