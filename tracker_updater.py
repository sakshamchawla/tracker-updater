import requests
import subprocess
import argparse
import urllib

qbit_host = 'http://127.0.0.1:1234'
login_data = {'username': 'admin', 'password': 'adminadmin'}
trackers_url = 'https://raw.githubusercontent.com/ngosang/trackerslist/refs/heads/master/trackers_all.txt'

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
   
    
def make_get(url):
    r = requests.get(url)
    return r.text
   
    
def get_trackers():
    trackers = make_get(trackers_url) 
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
        sid = make_post(get_url(qbit_host, 'login'), login_data, None)
        trackers = get_trackers()
        for tracker in trackers:
            code = make_post(get_url(qbit_host, 'addtrack'), get_trackers_request(args.torrentId, tracker), get_cookies(sid))
            print(code)

if __name__ == '__main__':
    main()