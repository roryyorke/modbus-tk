#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TCP client for deadlock bug example

Repeatedly queries of server as fast as possible.
"""

from __future__ import print_function

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp, hooks
import logging

logger = modbus_tk.utils.create_logger("console", level=logging.DEBUG)

def main():
    master = modbus_tcp.TcpMaster(port=5020)
    master.set_timeout(5.0)
    logger.info("connected")

    while True:
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 3))
        

if __name__ == '__main__':
    main()
