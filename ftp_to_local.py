#!/usr/bin/python
from ftplib import FTP
import os

hostname=os.environ.get('HOSTNAME')
login_id=os.environ.get('LOGIN')
password=os.environ.get('SECRET')

#Connect to FTP
ftp = FTP(hostname)
ftp.login(login_id,password, 'utf-8')
print("Connected to FTP ...")
print(ftp.getwelcome())


# List files in FTP
local_path = '/home/Backup/Magrathea/'

local_files=os.listdir(local_path)

ftp_files = ftp.nlst()

for check_file in ftp_files:
    if check_file not in local_files:
        local_files.append(check_file)
print("Ftp files count")
print(len(ftp_files))
print("Local files count")
print(len(local_files))

# Fetch files from FTP and zips file datewise
print("Downloading files from FTP ...")

for new_file in ftp_files:
    ftp.retrbinary('RETR ' +new_file, open(local_path+new_file, 'w').write)
    
print("files download to /home/Backup/Magrathea/")

#Close FTP connection
print("Closing FTP connection ...")
ftp.close()