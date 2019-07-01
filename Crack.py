import platform,os
import requests
import argparse
import hashlib
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-s', help='Your Hash', dest='hash')
parser.add_argument('-w', help='wordlist', dest='wordlist')
parser.add_argument('-d', help='File containing hashes', dest='dir')
parser.add_argument('-i', help='identify Hash Type', dest='identify')

args = parser.parse_args()

clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s
███████╗██╗   ██╗ ██████╗██╗  ██╗    ██╗  ██╗ █████╗ ███████╗██╗  ██╗
██╔════╝██║   ██║██╔════╝██║ ██╔╝    ██║  ██║██╔══██╗██╔════╝██║  ██║
█████╗  ██║   ██║██║     █████╔╝     ███████║███████║███████╗███████║
██╔══╝  ██║   ██║██║     ██╔═██╗     ██╔══██║██╔══██║╚════██║██╔══██║
██║     ╚██████╔╝╚██████╗██║  ██╗    ██║  ██║██║  ██║███████║██║  ██║
╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  %s%s
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[92m
    """ % (B, W,R))


banner()


def Site2(hashvalue):
    data = requests.get('http://www.nitrxgen.net/md5db/' + hashvalue).text
    if len(data) != 0:
        return data
    else:
        return "None"


def Site(hashvalue, hashtype):
    if hashtype is "None":
        return "None"
    if hashtype == "md5":
        data = Site2(hashvalue)
        if data != "None":
            return data    
    
    data = requests.get('http://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=vector@getsimpleemail.com&code=ee7520f3e642deb4' % (hashvalue, hashtype)).text
    if len(data) != 0:
        if "CODE ERREUR" in data:
            return "None"
        return data
    else:
        return "None"




def get_hash(data,id="None"):
    if id == "sha256":
        return hashlib.sha256(str(data).encode('utf-8')).hexdigest()
    elif id == "sha1":
        return hashlib.sha1(str(data).encode('utf-8')).hexdigest()
    elif id == "sha224":
        return hashlib.sha224(str(data).encode('utf-8')).hexdigest()
    elif id == "sha512":
        return hashlib.sha512(str(data).encode('utf-8')).hexdigest()
    elif id == "sha384":
        return hashlib.sha384(str(data).encode('utf-8')).hexdigest()
    elif id == "md5":
        return hashlib.md5(str(data).encode('utf-8')).hexdigest()
    else:
        return "None"

def get_hash_id(hash):
    if len(hash) == 64:
        return "sha256"
    elif len(hash) == 40:
        return "sha1"
    elif len(hash) == 56:
        return "sha224"
    elif len(hash) == 128:
        return "sha512"
    elif len(hash) == 96:
        return "sha384"
    elif len(hash) == 32:
        return "md5"
    else:
        return "None"


def Crack(hash,id,list):
    if id is "None":
        return "None"
    data_ = open(list, encoding = "ISO-8859-1").read().split()
    for data in data_:
        hash_data = get_hash(data,id)
        if hash_data == hash:
            return data
            break
    return "None"



if args.dir is None and args.hash is None and args.identify is None and args.wordlist is None:
    os.system("python3 "+sys.argv[0]+" -h")


elif args.hash is not None:
    print("%s[+] Please Wait ...\n%s"%(W,W))
    if args.wordlist is not None: 
        data = Crack(args.hash,get_hash_id(args.hash),args.wordlist)
        if data != "None":
            print("[+] Found :%s"%(Y),data,"\n")
        else:
            print("[-] Not Found","\n")
    else:
        data = Site(args.hash,get_hash_id(args.hash))
        if data != "None":
            print("[+] Found :%s"%(Y),data,"\n")
        else:
            print("[-] Not Found","\n")


elif args.identify is not None:
    print("%s[+] Please Wait ...\n%s"%(W,W))
    if get_hash_id(args.identify) != "None":
        print("[+] Hash Type :",get_hash_id(args.identify).upper(),"\n")
    else:
        print("[-] Sorry , Can't Identify This Hash !!","\n")


elif args.dir is not None:
    print("%s[+] Please Wait ...\n%s"%(W,W))
    hashs = open(args.dir).read().split()
    if args.wordlist is not None:
        for hash in hashs:
            data = Crack(hash,get_hash_id(hash),args.wordlist)
            if data != "None":
                print("%s[+] Found :\n%s"%(G,G),hash,"=>",data,"\n")
            else:
                print("%s[-] Not Found\n%s"%(R,R),hash,"\n")
    else:
        for hash in hashs:
            data = Site(hash,get_hash_id(hash))
            if data != "None":
                print("%s[+] Found :\n%s"%(G,G),hash,"=>",data)
            else:
                print("%s[-] Not Found\n%s"%(R,R),hash,"\n")

