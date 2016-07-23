### 简介
> 在开发项目时需要C进程不停的发消息给服务端服务端在吧消息转发给前端.服务端与前端之间用socket.io. C进程和服务端之间用什么传输?
找到了一个神器: Zmq, zmq支持 python, java ,c/c++, javascript等等,几乎所有开发语言都支持.这就满足了我们的项目需求.

## 问题描述
然而我在开发中遇到一个棘手的问题: zmq 的消息都是阻塞式的,也就是说如果不做处理,客户端给服务端发送消息, 客户端一直等待服务端的响应, 知道收到响应
为止,这是非常要命的, 比如我发一个zmq请求一直没有等到响应,那么socket.recv()将一直阻塞下去,不能执行下面的代码.这是我们不想看到的.

## 解决方案
我在开发中使用了 zmq 的poller机制实现了类似HTTP请求的request/reply模式 可以设置请求超时.不让其一直阻塞下去

## 使用方法

``` python
# 使用了flatbuffers 包装消息,详情自行google

# 默认(3000ms 超时)
ZmqRQInstance().zmq_request(MsgTpye.ZMQ_MSGTYPE_SET_USER, json.dumps(para)))

# 自定义超时时间 5000ms
ZmqRQInstance().zmq_request(MsgTpye.ZMQ_MSGTYPE_GET_USER, json.dumps({}), 1000 * 5)
```

## 效果
![image](https://github.com/kuangch/ZmqRQhelper/blob/master/zmq.png)