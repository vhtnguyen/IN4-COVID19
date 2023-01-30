import socket
import threading

IP = "192.168.1.9"
PORT = 8888
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNETED!"
SERVERSTATUS = None

connected = True
ui = None
username = ""
client = None


def getsock():
    global client, SERVERSTATUS
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SERVERSTATUS = True
        return client
    except:
        SERVERSTATUS = False
        return client


def client_conn(client, addr):
    global SERVERSTATUS
    try:
        client.connect(addr)
        ADDR = addr
        SERVERSTATUS = True
        return True
    except socket.error:
        SERVERSTATUS = False
        return False


def closeSK(client):
    try:
        client.close()
    except:
        pass


def recv_msg(client):
    global SERVERSTATUS
    if SERVERSTATUS:
        try:
            msg = client.recv(SIZE).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                SERVERSTATUS = False
                closeSK(client)
            return msg
        except socket.error:
            closeSK(client)
            return DISCONNECT_MSG
    else:
        closeSK(client)
        return DISCONNECT_MSG


def send_msg(client, msg):
    global SERVERSTATUS
    if SERVERSTATUS:
        try:
            client.send(msg.encode(FORMAT))
        except:
            closeSK(client)
            SERVERSTATUS = False


def getIP():
    return IP


def sendDisc(client):
    send_msg(client, "logout")
    recv_msg(client)


def hanoi(client):
    send_msg(client, "search")
    jp = "ha noi"
    if recv_msg(client) == "ok":
        send_msg(client, jp)
        data = recv_msg(client)
        return data


def hue(client):
    send_msg(client, "search")
    jp = "hue"
    if recv_msg(client) == "ok":
        send_msg(client, jp)
        data = recv_msg(client)
        return data


def saigon(client):
    send_msg(client, "search")
    jp = "TPHCM"
    if recv_msg(client) == "ok":
        send_msg(client, jp)
        data = recv_msg(client)
        return data


def search(client, nameprv):
    send_msg(client, "search")
    jp = nameprv
    if recv_msg(client) == "ok":
        send_msg(client, jp)
        data = recv_msg(client)
        return data
    else:
        return DISCONNECT_MSG


def getToday(client):
    send_msg(client, "today")
    if recv_msg(client) == "ok":
        send_msg(client, "ok")
        data = recv_msg(client)
        return data


def get7days(client):
    send_msg(client, "chart")
    if recv_msg(client) == "ok":
        send_msg(client, "ok")
        data = recv_msg(client)
        return data
