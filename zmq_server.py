#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 kuangch All Rights Reserved.
import time

import zmq
import json

from trans_msg import TransMsg
from zmq_flatbuf_msg_api import send_flatbuf_msg
from msg_type import MsgTpye
from zmq_conn_port import ZMQPort

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:" + ZMQPort.RQ)

user_info = None

while True:

    #  Wait for next request from client
    message = socket.recv()

    #  Do some 'work'
    msg_obj = TransMsg.GetRootAsTransMsg(message, 0)
    msg_type = msg_obj.Type()

    print('req type: %s' % msg_type)
    print('req para: %s' % msg_obj.Content())
    #  Send reply back to client

    if msg_type == MsgTpye.ZMQ_MSGTYPE_GET_USER:

        print('get user info')
        if user_info is not None:
            res = {
                'code': 0,
                'msg': 'get user info success',
                'data': user_info
            }
            send_flatbuf_msg(socket, msg_type, json.dumps(res))
        else:
            ret = {
                'code': -1,
                'msg': 'get user info failed',
            }
            send_flatbuf_msg(socket, msg_type, json.dumps(ret))

    if msg_type == MsgTpye.ZMQ_MSGTYPE_SET_USER:

        print('set user info')
        try:
            info = msg_obj.Content()
            user_info = json.loads(msg_obj.Content())
            ret = {
                'code': 0,
                'msg': 'set user info success',
            }
        except:
            ret = {
                'code': -1,
                'msg': 'set user info failed',
            }
        send_flatbuf_msg(socket, msg_type, json.dumps(ret))

    time.sleep(2)
