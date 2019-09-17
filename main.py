#!/user/bin/env python

import os, sys, urllib.request, argparse, json
from bs4 import BeautifulSoup
#from pprint import pprint

parser = argparse.ArgumentParser(description='HTML to JSON')
parser.add_argument('url', type=str, help='Input url to download html file')
args = parser.parse_args()

print("Checking internet connection...")
if urllib.request.urlopen("http://google.com").getcode() == 200:
    print("Network connection ok")
else:
    sys.exit("Network connection failed, exit")

print(f"Input html file: {args.url}")
response = urllib.request.urlopen(args.url)

if response.headers['content-type'] == 'text/html; charset=UTF-8':
    print(f"{args.url} is a valid html file, continue process...")
else:
    sys.exit("This is not valid html, exit")

soup = BeautifulSoup(response, 'html.parser')

feeds = soup.find_all('link', attrs={"type": "application/rss+xml"})
print(str(feeds.get('href')))
type(feeds)

dic = {'rss' : [], 'atom' :  []}
print(dic)
json = json.dumps(dic)
print(json)


