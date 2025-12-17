import requests
import subprocess
import argparse
import urllib

host = ''
login_data = {'username': 'admin', 'password': 'adminadmin'}

def get_url(host, op):
    if op == 'login':
        return f'{host}/api/v2/auth/login'
    elif op == 'addtrack':
        return f'{host}/api/v2/torrents/addTrackers'
    elif op == 'list':
        return f'{host}/api/v2/torrents/info'

def make_post(url, body, cookies):
    r = requests.post(url, data=body, cookies=cookies)
    if url.endswith('login'):
        return r.cookies.get('SID')
    return r.status_code
   
    
def make_get(url, params):
    r = requests.get(url, params=params)
    print(r.status_code)
   
    
def get_trackers():
    with open('trackerslist/trackers_all.txt', 'r') as f:
        trackers = f.read()
        trackers = trackers.split("\n")
        trackers = [t for t in trackers if t != None and t != '']        
        return trackers


def get_trackers_request(torrentId, url):
    return {
        'hash': torrentId,
        'urls': url
    }


def get_cookies(sid):
    return {
        'SID': sid
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('torrentId', type=str)
    args = parser.parse_args()
    if args.torrentId:
        subprocess.run(['./git_updater.sh'], check=True)
        sid = make_post(get_url(host, 'login'), login_data, None)
        trackers = get_trackers()
        for tracker in trackers:
            code = make_post(get_url(host, 'addtrack'), get_trackers_request(args.torrentId, tracker), get_cookies(sid))
    

if __name__ == '__main__':
    main()