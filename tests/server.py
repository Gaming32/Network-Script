from netsc import Server

class MyServer(Server):
    bind_addr = ('', 8192)
    attrs = ['a']

class C1:
    def __init__(self, o):
        self.a = o
    def m(self):
        return self.a


server = MyServer(C1(16))

server.accept()

server.poll()

print(server.a)