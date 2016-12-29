# FTP_Python
python3+pyftpdlib=ftp server

#use info
1.基于python3+window7
2.pip install pyftpdlib     安装ftp库
3.python ftp_server.py      运行ftp应用
4.在浏览器内输入ftp://127.0.0.1浏览ftp内容
5.config_ftp.py是基本的配置内容，有具体的说明
6.ftp_server.py是主程序文件，读取配置文件内容，绑定端口，启动监听服务
7.baseftp.ini是基本的用户名，密码，权限，访问目录等配置


#issue solution
OSError: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
在cmd命令内，使用netstat -ano查看TCP/IP/PORT/PID等信息，发现21端口被占用,使用taskkill /PID pidnumber /F将此进程杀死，还是报错,最后发现是因为自己前一段时间有启用Internet信息服务(IIS)管理器启动了FTP相关服务,控制面板-》管理工具-》Internet 信息服务(IIS)管理器，双击打开，可看到具体配置内容,停用相关内容后，杀掉占用21端口的进程，再次启动自己的ftp服务即可成功

