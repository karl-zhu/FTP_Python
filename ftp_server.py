# __*__ coding:utf-8 __*__
import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from config_ftp import *

def init_ftp_server():
    authorizer = DummyAuthorizer()
    #读权限e：改变目录，l：列出文件，r：从服务器接收文件
	#写权限a：文件上传，d：删除文件，f：文件重命名，m：创建文件，w：写权限，m：文件传输模式
    for user in user_list:
        name,passwd,permit,homedir = user
        try:
            authorizer.add_user(name,passwd,homedir,perm=permit)
        except:
            print("配置文件错误请检查是否正确匹配了相应的用户名、密码、权限、路径")
            print(user)
    if enable_anonymous:
        authorizer.add_anonymous(anonymous_path)
    dtp_handler = ThrottledDTPHandler
    # 上传速度 下载速度
    dtp_handler.read_limit = max_download
    dtp_handler.write_limit = max_upload
    handler = FTPHandler
    handler.authorizer = authorizer
    #是否打开记录
    if enable_logging:
        logging.basicConfig(filename=logging_name,level=logging.INFO)
    handler.banner = welcome_banner
    handler.masquerade_address = masquerade_address
    handler.passive_ports = range(passive_ports[0],passive_ports[1])
    server = FTPServer((ip,port),handler)
    server.max_cons = max_cons
    server.max_cons_per_ip = max_pre_ip
    server.serve_forever()
	
def ignor_octothrpe(txt):
    for x,item in enumerate(txt):
        if item == "#":
            return txt[:x]
        pass
    return txt
	
def init_user_config():
    f = open(user_config_file,encoding='utf-8')
    while True:
        line = f.readline()
        if len(ignor_octothrpe(line))>3:
            user_list.append(line.split())
        if not line:
            break
			
if __name__ == "__main__":
    user_list=[]
    init_user_config()
    init_ftp_server()
	

