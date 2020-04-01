#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import struct
import socket


def handle_conn(conn, addr, handlers):
    print(addr, "comes")
    while True:
        length_prefix = conn.recv(4)  # 请求长度前缀
        if not length_prefix:  # 连接关闭了
            print(addr, "bye")
            conn.close()
            break  # 退出循环，处理下一个连接
        length, = struct.unpack("I", length_prefix)
        body = conn.recv(length)   # 请求消息体
        request = json.loads(body.decode("utf8"))
        in_ = request["in"]
        params = request["params"]
        print(in_, params)
        handler = handlers[in_]  # 查找请求处理器
        handler(conn, params)  # 处理请求


def loop(sock, handlers):
    while True:
        conn, addr = sock.accept()  # 接受连接
        handle_conn(conn, addr, handlers)


def ping(conn, params):
    send_result(conn, "pong", params)


def send_result(conn, out, result):
    response = json.dumps({"out": out, "result": result})  # 相应消息体
    length_prefix = struct.pack("I", len(response))
    conn.sendall(length_prefix)
    conn.sendall(response.encode("utf8"))


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 打开reuse addr选项
    sock.bind(("localhost", 8080))
    sock.listen(1) # 监听客户端连接

    handlers = {"ping": ping}
    loop(sock, handlers)











































