#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import struct
import socket
# 套接字服务器大致 API，参数略
# sock = socket.socket()  # 创建一个服务器套接字
# sock.bind()  # 绑定端口
# sock.listen()  # 监听连接
# sock.accept()  # 接受新连接
# sock.close()  # 关闭服务器套接字

# value_in_bytes = struct.pack("I", 1024)  # 将一个整数编码成 4 个字节的字符串
# value, = struct.unpack("I", value_in_bytes)  # 将一个 4 字节的字符串解码成一个整数
# 注意等号前面有个逗号，这个非常重要，它不是笔误。
# 因为 unpack 返回的是一个列表，它可以将一个很长的字节串解码成一系列的对象。
# value 取这个列表的第一个对象。

# raw = json.dumps({"hello": "world"})  # 序列化
# po = json.loads(raw)  # 反序列化
#
# def receive(sock, n):
#     rs = []  # 读取结果
#     while n > 0:
#         r = sock.recv(n)
#         if not r:  # EOF
#             return rs
#         rs.append(r)
#         n -= len(r)
#     return ''.join(rs)


def rpc(sock, in_, params):
    request = json.dumps({"in": in_, "params": params})  # 请求消息体
    length_prefix = struct.pack("I", len(request))  # 请求长度前缀
    sock.sendall(length_prefix)
    sock.sendall(request.encode("utf8"))
    length_prefix = sock.recv(4)  # 相应长度前缀
    length, = struct.unpack("I", length_prefix)
    body = sock.recv(length)  # 接受相应消息体
    response = json.loads(body.decode("utf8"))
    return response["out"], response["result"]  # 返回相应类型和结果


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    for i in range(10):
        out, result = rpc(s, "ping", "ireader %d" % i)
        print(out, result)
        time.sleep(1)

    s.close()




















