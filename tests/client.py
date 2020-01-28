from netsc import Client

class MyClient(Client):
    attrs = ['a']


class C2:
    def __init__(self, o):
        self.a = o
    def m(self):
        return self.a


client = MyClient(C2(64))

client.connect(('localhost', 8192))

print(client.m())

client.poll()