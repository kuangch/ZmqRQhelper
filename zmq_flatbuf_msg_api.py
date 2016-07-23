#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 kuangch All Rights Reserved.

# all api is about msg translate by zmq

from trans_msg import *


def send_flatbuf_msg(socket, msg_type, msg_content):

    b = flatbuffers.Builder(0)
    if msg_content is not None:
        msg = b.CreateString(msg_content)
    else:
        msg = b.CreateString('')

    TransMsgStart(b)
    TransMsgAddType(b, msg_type)
    TransMsgAddContent(b, msg)
    msT = TransMsgEnd(b)
    b.Finish(msT)

    h = b.Head()
    socket.send(b.Bytes[h:])
