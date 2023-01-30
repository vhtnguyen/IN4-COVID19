import socket
import threading
import dataBase as db
import sys
import os
import time
import schedule
from datetime import datetime
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class SV:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 8888
        self.ADDR = (self.IP, self.PORT)
        self.SIZE = 2048
        self.FORMAT = "utf-8"
        self.DISCONNECT_MSG = "DISCONNECTED!"
        self.CLIENT_LIST = []
        self.ADDR_LIST = []
        self.SERVER_RUNNING = True
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.LASTUPDATED = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.ACTIVECONN = 0
        self.USERNAME = ""
        self.ui = None
        self.graph = None
        self.news = None

    def updateClient(self, conn):
        print("update clientUI\n")

    def takeUI(self, ui):
        self.ui = ui

    def updateUI(self):
        self.ui.status = self.svInfo()
        self.ui.add_list = self.addrInfo()
        self.ui.updateUI()

    def updateSV(self):
        self.LASTUPDATED = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # db.getData()
        self.updateUI()
        print("server updated!")

    def updateSchedule(self):
        self.updateSV()
        schedule.every(60).minutes.do(self.updateSV)
        while True:
            if self.SERVER_RUNNING == False:
                break
            schedule.run_pending()
            time.sleep(1)
        return schedule.CancelJob

    def addrInfo(self):
        al = "\n"
        for i in self.ADDR_LIST:
            al += str(i) + "\n"
        return al

    def svInfo(self):
        self.ACTIVECONN = len(self.CLIENT_LIST)
        if self.SERVER_RUNNING:
            stt = "STATUS: RUNNING"
        else:
            stt = "STATUS: NOT RUNNING"
        lastud = "Last updated: " + str(self.LASTUPDATED)
        act = "ACTIVE CONNECTIONS: " + str(self.ACTIVECONN)
        return lastud + "\n" + stt + "\n" + act

    def send_msg(self, conn, msg):
        try:
            conn.send(msg.encode(self.FORMAT))
        except:
            pass

    def recv_msg(self, conn):
        try:
            res = conn.recv(self.SIZE).decode(self.FORMAT)
            return res
        except:
            pass

    def remove_conn(self, conn, addr):
        for cn in self.CLIENT_LIST:
            if cn == conn:
                self.CLIENT_LIST.remove(cn)
                break
        for adr in self.ADDR_LIST:
            if adr == addr:
                self.ADDR_LIST.remove(adr)
                break
        return self.DISCONNECT_MSG

    def disconnect_SV(self):
        for i in self.CLIENT_LIST:
            self.send_msg(i, self.DISCONNECT_MSG)
            i.close()
        self.CLIENT_LIST.clear()
        self.ADDR_LIST.clear()
        self.connected = False
        return self.DISCONNECT_MSG

    def shutdown_SV(self):
        self.disconnect_SV()
        self.SERVER_RUNNING = False
        sys.exit(0)

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        self.connected = True
        self.updateUI()
        while self.connected:
            try:
                msg = self.recv_msg(conn)
                print(f" {addr} [REQUEST]{msg}")
                if msg == self.DISCONNECT_MSG:
                    self.send_msg(conn, self.remove_conn(conn))
                    self.connected = False
                elif msg == "login":
                    self.send_msg(conn, "ok")
                    usr = self.recv_msg(conn)
                    self.send_msg(conn, "ok")
                    pw = self.recv_msg(conn)
                    self.send_msg(conn, "ok")
                    res = db.login(usr, pw)
                    print(res)
                    self.send_msg(conn, res)
                elif msg == "search":
                    self.send_msg(conn, "ok")
                    nameprv = self.recv_msg(conn)
                    res = db.search(nameprv)
                    self.send_msg(conn, res)
                elif msg == "logout":
                    self.send_msg(conn, self.remove_conn(conn, addr))
                    self.connected = False
                elif msg == self.DISCONNECT_MSG:
                    self.connected = False
                    self.send_msg(conn, self.DISCONNECT_MSG)
                    self.remove_conn(conn, addr)
                elif msg == "chart":
                    self.send_msg(conn, "ok")
                    res = str(db.getInfo7day())
                    self.recv_msg(conn)
                    self.send_msg(conn, res)
                elif msg == "today":
                    self.send_msg(conn, "ok")
                    res = str(db.getInfoToday())
                    self.recv_msg(conn)
                    self.send_msg(conn, res)
                elif msg == "signup":
                    self.send_msg(conn, "ok")
                    fullname = self.recv_msg(conn)
                    self.send_msg(conn, "ok")
                    username = self.recv_msg(conn)
                    self.send_msg(conn, "ok")
                    password = self.recv_msg(conn)
                    self.send_msg(conn, "ok")
                    pin = self.recv_msg(conn)
                    self.send_msg(conn, "ok")

                    filesize = os.path.getsize("userData.json")
                    self.recv_msg(conn)
                    if filesize == 0:
                        self.send_msg(conn, "usename accept")
                        db.addUser0(fullname, username, password, pin)

                    else:
                        if db.checkExist(username) == False:
                            self.send_msg(conn, "usename accept")
                            db.addUser(fullname, username, password, pin)

                        elif db.checkExist(username) == True:
                            self.send_msg(conn, "username exist")
                elif msg == "forgot password":
                    self.send_msg(conn, "ok")
                    username = self.recv_msg(conn)
                    self.send_msg(conn, "ok")
                    pin = self.recv_msg(conn)
                    self.send_msg(conn, "ok")
                    new_password = self.recv_msg(conn)
                    self.send_msg(conn, "ok")

                    self.recv_msg(conn)

                    if db.checkExist(username) == False:
                        self.send_msg(conn, "user not exist")
                    elif db.checkExist(username) == True:
                        if db.checkPIN(username, pin) == True:
                            self.send_msg(conn, "password changed")
                            db.changePassword(username, new_password)
                        elif db.checkPIN(username, pin) == False:
                            self.send_msg(conn, "incorrect")
                else:
                    pass
            except socket.error:
                self.connected = False
                self.remove_conn(conn, addr)
            self.updateUI()
        conn.close()

    def runSV(self):
        print("[STARTING] Server is starting...")
        self.server.bind(self.ADDR)
        self.server.listen(5)
        self.server.settimeout(5)
        print(f"[LISTENING] Server is listening on {self.IP}:{self.PORT}")
        # testsd()
        while self.SERVER_RUNNING:
            conn = None
            addr = None
            try:
                conn, addr = self.server.accept()
                self.CLIENT_LIST += [conn]
                self.ADDR_LIST += [addr]
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
            except socket.timeout:
                pass
            except OSError:
                self.SERVER_RUNNING = False
        self.server.close()


sv = SV()


def getSV():
    global sv
    return sv


def main():
    global sv
    t1 = threading.Thread(target=sv.updateSchedule)
    t2 = threading.Thread(target=sv.runSV)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
