# __*__ coding:utf-8 __*__

#本机绑定ip
ip = "0.0.0.0"
#本机绑定端口
port = "21"
#上传速度 300Kb/sec
max_upload = 300 * 1024
#下载速度 300Kb/sec
max_download = 300 * 1024
#最大连接数
max_cons = 256
#最多ip连接数
max_pre_ip = 10
#被动连接端口
passive_ports = (9200,9300)
#是否容许匿名访问
enable_anonymous = False
#是否打开日志记录
enable_logging = True
#日志记录文件名称
logging_name = r"pyftp.log"
#公网ip
masquerade_address = "127.0.0.1"
#欢迎标题
welcome_banner = r"Welcome to zhunn private ftp."
#默认匿名用户路径
anonymous_path = r"E:\\"
#用户名配置文件
user_config_file = r"baseftp.ini"

