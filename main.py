#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 kuangch All Rights Reserved.

import json
from msg_type import MsgTpye
from zmq_RQ_helper import ZmqRQInstance

para = {
    'name': '黄陂酷歌',
    'feature': '帅',
    'QQ': '836953221',
    'weChat': 'k836953221',
    'phoneNumber': '13554333017'
}
print('\nget user info')
print(ZmqRQInstance().zmq_request(MsgTpye.ZMQ_MSGTYPE_GET_USER, json.dumps({})))

print('\nset user info')
print(ZmqRQInstance().zmq_request(MsgTpye.ZMQ_MSGTYPE_SET_USER, json.dumps(para)))

# zmq_RQ_helper default timeout is 3000ms and zmq_server default 3000ms return a response
# so it is enough time to get user info
print('\nget user info default timeout (3000ms)')
ret = ZmqRQInstance().zmq_request(MsgTpye.ZMQ_MSGTYPE_GET_USER, json.dumps({}))
if ret:
    print(ret)
else:
    print('请求超时')

# set timeout to 1000ms that will be timeout because zmq_server default 3000ms return a response
print('\nget user info set timeout 1000ms')
ret = ZmqRQInstance().zmq_request(MsgTpye.ZMQ_MSGTYPE_GET_USER, json.dumps({}), 1000)
if ret:
    print(ret)
else:
    print('请求超时')

# set timeout to 1000ms that will be timeout because zmq_server default 3000ms return a response
print('\nget user info set timeout 5000ms')
ret = ZmqRQInstance().zmq_request(MsgTpye.ZMQ_MSGTYPE_GET_USER, json.dumps({}), 1000 * 5)
if ret:
    print(ret)
else:
    print('请求超时')
