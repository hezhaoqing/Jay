Socket套接字格式：
socket(family,type[,protocal])     使用给定的地址族（网络层）、套接字类型（传输层）、协议编号（默认为0）来创建套接字。

常用地址家族，即family：
socket.AF_UNIX：基于文件，实现同一主机不同进程之间的通信
socket.AF_INET：基于网络，适用于IPv4
socket.AF_INET6：基于网络，使用于IPv6

常用连接类型，即type：
socket.SOCK_STREAM：即TCP/IP
socket.SOCK_DGRAM：即UDP


创建1个socket
s=socket.socket()   ###  默认为创建1个tcp的socket，即s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


服务端socket函数
s.bind(address)     ### 将套接字绑定到地址, 在AF_INET下,以元组（host,port）的形式表示地址.
s.listen(backlog)   ### 开始监听TCP传入连接。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
s.accept()          ### 接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。

客户端socket函数
s.connect(address)  ### 连接到address处的套接字。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
s.connect_ex(adddress)    ### 功能与connect(address)相同，但是成功返回0，失败返回errno的值。

服务端客户端公共函数
s.close()

......

很多。。
