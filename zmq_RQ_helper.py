#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 kuangch All Rights Reserved.

# a single instance for zmq request

import zmq

from trans_msg import *
from zmq_conn_port import ZMQPort

from zmq_flatbuf_msg_api import send_flatbuf_msg


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


class ZmqRQInstance(object):
    """
    the single instance of send zmq request and get response(support request timeout)
    """
    __metaclass__ = Singleton

    # default timeout for request
    __DEFAULT_REQUEST_TIMEOUT = 1000 * 3

    # time interval to poll socket to check is it has messages
    __POLL_INTERVAL = 300

    # socket to talk to server
    __socket = None
    print("init RQ socket instance")

    def zmq_request(self, msg_type, msg_content, timeout=__DEFAULT_REQUEST_TIMEOUT):

        #  new socket to talk to server
        self.__socket = zmq.Context().socket(zmq.REQ)
        self.__socket.connect("tcp://localhost:" + ZMQPort.RQ)

        # init poller and register to socket that web can poll socket to check is it has messages
        poller = zmq.Poller()
        poller.register(self.__socket, zmq.POLLIN)

        send_flatbuf_msg(self.__socket, msg_type, msg_content)

        reqs = 0

        while reqs * self.__POLL_INTERVAL <= timeout:
            socks = dict(poller.poll(self.__POLL_INTERVAL))
            if self.__socket in socks and socks[self.__socket] == zmq.POLLIN:
                msg = self.__socket.recv()
                msgObj = TransMsg.GetRootAsTransMsg(msg, 0)
                return msgObj.Content()
            reqs = reqs + 1

        return False
