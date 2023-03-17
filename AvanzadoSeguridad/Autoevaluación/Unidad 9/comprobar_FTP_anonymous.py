#!/usr/bin/env python3

import ftplib

def ftpListDirectory(xxx):
    try:
        dirList = ftp.xxx()
        print(xxx)
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        return
    retList = []
    for fileName in xxx:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + xxx)
            retList.append(xxx)
            
    return retList

def anonymousLogin(xxx):
    try:
        ftp = ftplib.xxx(xxx)
        ftp.xxx('anonymous', 'anonymous')
        print(ftp.xxx())
        ftp.xxx(1)
        print(ftp.xxx())        
        print('\n[*] ' + str(xxx) +' FTP Anonymous Logon Succeeded.')
        return ftp
    except Exception as e:
        print(str(e))
        print('\n[-] ' + str(xxx) +' FTP Anonymous Logon Failed.')
        return False

host = 'ftp.be.debian.org'
ftp = anonymousLogin(xxx)
ftpListDirectory(xxx)
