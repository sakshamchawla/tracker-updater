import requests
import subprocess
import argparse


host = ''
login_data = {'username': 'admin', 'password': 'adminadmin'}

def get_url(host, op):
    if op == 'login':
        return f'{host}/api/v2/auth/login'
    elif op == 'addtrack':
        return f'{host}/api/v2/torrents/addTrackers'

def make_post(url, body, headers):
    r = requests.post(url, data=body)
    if url.endswith('login'):
        return r.cookies.get('SID')
    return r.json()
    
def make_get(url, params):
    r = requests.get(url, params=params)
    print(r.status_code)
    
def get_trackers():
    with open('trackerslist/trackers_all.txt', 'r') as f:
        trackers = f.read()
        # trackers = trackers.split("\n")
        # trackers = [t for t in trackers if t != None and t != '']
        return trackers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('torrentId', type=str)
    args = parser.parse_args()
    if args.torrentId:
        print(args.torrentId)
        # subprocess.run(['./git_updater.sh'], check=True)
        # make_post(get_url(host, 'login'), login_data)
        # trackers = get_trackers()
    

if __name__ == '__main__':
    main()