from ftplib import FTP_TLS
import os
import sys
import datetime
import json

date = datetime.datetime.now().strftime("%d-%m-%Y") #Argentine time format

r = open("secrets.json", "r")
data = json.load(r)
r.close()
ftp = FTP_TLS()
ftp.connect(data["IP"])
ftp.login(user=data["USERNAME"], passwd=data["PASSWORD"])
ftp.cwd(data["DIRECTORY"])
ftp.storbinary(f'STOR Chat.Prod-{date}.bak', open(os.path.join(sys.path[0],f'Chat.Prod-{date}.bak'),'rb'))
ftp.close()