# Installing
To install use the command `python -m pip install Network-Script`.
# Basic Tutorial
## Server
To start off import the `Server` class:
``` python
from netsc import Server
```
Then create a subclass of the `Server` class, defining `bind_addr` and possibly `sock_family`, `sock_type`, and `sock_proto`:
``` python
class MyServer(Server):
    bind_addr = ('', 1920)
```
Then create an instance, define the object it wraps, and accept a connection:
``` python
server = MyServer(wrapped_obj)
server.accept()
```
## Client
To start off import the `Server` class:
``` python
from netsc import Client
```
Then create a subclass of the `Server` class, possibly defining `sock_family`, `sock_type`, and `sock_proto`:
``` python
class MyClient(Client):
    pass
```
Then create an instance, define the object it wraps, and connect to a server:
``` python
client = MyClient(wrapped_obj)
client.connect(('localhost', 1920))
```