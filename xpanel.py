import sys, socket
from PyQt5 import QtWidgets, QtCore
from extron import Ui_Main

class my_app(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.mon = QtCore.QTimer()
        self.mon.timeout.connect(self.monitor)
        self.ui.pushButton.clicked.connect(self.set_extron)
        self.mon.start(5000)

    def monitor(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)
        server_address = ('192.168.0.31', 23)
        err = sock.connect_ex(server_address)
        if err > 0:
            if self.ui.groupBox.isEnabled(): self.ui.groupBox.setEnabled(False)
        else:
            if not self.ui.groupBox.isEnabled(): self.ui.groupBox.setEnabled(True)
            sock.close()

#        try:
#            sock.connect(server_address)
#        except socket.error as e:
#            if self.ui.groupBox.isEnabled(): self.ui.groupBox.setEnabled(False)
#        else:
#            if not self.ui.groupBox.isEnabled(): self.ui.groupBox.setEnabled(True)
#            sock.close()

    def set_extron(self):
#        a = 'self.ui.Out1.currentIndex()'
#        s_1 = str(eval(a) + 1) + '*1!\r\n'
#        s_2 = str(self.ui.Out2.currentIndex() + 1) + '*2!\r\n'
#        s_3 = str(self.ui.Out3.currentIndex() + 1) + '*3!\r\n'
#        s_4 = str(self.ui.Out4.currentIndex() + 1) + '*4!\r\n'

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('192.168.0.31', 23)
        sock.connect(server_address)
        self.mess = sock.recv(1024)
        self.mess = 'administrator\r\n'
        sock.send(self.mess.encode())
        self.mess = sock.recv(1024)
        self.mess = 'admin\r\n'
        sock.send(self.mess.encode())
        self.mess = sock.recv(1024)

        for i in range(1,5):
            self.b = str(eval('self.ui.Out'+str(i)+'.currentIndex()') + 1) + '*'+str(i)+'!\r\n'
            sock.send(self.b.encode())
            self.mess = sock.recv(1024)
        sock.close()
'''    
        sock.send(s_1.encode())
        self.mess = sock.recv(1024)
        sock.send(s_2.encode())
        self.mess = sock.recv(1024)
        sock.send(s_3.encode())
        self.mess = sock.recv(1024)
        sock.send(s_4.encode())
        self.mess = sock.recv(1024)
        sock.close()
'''
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = my_app()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
