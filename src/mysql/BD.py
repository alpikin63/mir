import pymysql
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.122.1', username='nspk', password='Ty2hd.e0Sa')

time.sleep(1)

db = pymysql.connect(host="192.168.122.1",
                     user="nspk",
                     passwd="Ty2hd.e0Sa",
                     db="nspk")
cur = db.cursor()



