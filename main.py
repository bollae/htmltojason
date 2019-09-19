#!/user/bin/env python3.7

#    name='htmltojson',
#    version='0.1.0',
#    author='Eszter Bolla',
#    author_email='bolla.eszter@gmail.com',
#    description='An utility for convert rss and atom links from html to json'


import os
import sys
import urllib.request
import argparse
import json
from bs4 import BeautifulSoup

# This sciript has one input argument. Create and check the input argus.
parser = argparse.ArgumentParser(description='HTML to JSON')
parser.add_argument('url', type=str, help='Input url to download html file. Format: http(s)://<url>')
args = parser.parse_args()

# The script download the html files on the Internet.
# This section checks the network connection availability with request for gooogle.com
def main():
    print("Checking internet connection...")
    if urllib.request.urlopen("http://google.com").getcode() == 200:
        print("Network connection ok")
    else:
        sys.exit("Network connection failed, exit")

# The script works with html tags, so need to check the input is valid html docs.
# The script search text/html string in htmls's header.
    print(f"Input html: {args.url}")
    response = urllib.request.urlopen(args.url)
    if 'text/html' in response.headers['content-type']:
        print(f"{args.url} is a valid html file, continue process...")
    else:
        sys.exit("This is not valid html, exit")

# This section parse the html with BeautifulSoup and find
# the links tag that have a type attribute with rss or atom feeds value.
    soup = BeautifulSoup(response, 'html.parser')
    rss = soup.find_all('link', attrs={"type": "application/rss+xml"})
    atom = soup.find_all('link', attrs={"type": "application/atom+xml"})
    dic = {'rss': [], 'atom': []}


# The follwing lines check the link href value. If it is relative link,
# ignore them, if it si absolute path, put a dictionary and export json.

    for link in atom:
        if 'http' in link.get('href'):
            print(f"Found {link.get('href')}")
            dic['atom'].append(link.get('href'))
        else:
            print(f"It is not found any atom feed with absolut path in {args.url}")

    for link in rss:
        if 'http' in link.get('href'):
            print(f"Found {link.get('href')}")
            dic['rss'].append(link.get('href'))
        else:
            print(f"It is not found any rss feed with absolut path in {args.url}")
    exportdata = json.dumps(dic)
    print(f"Job completed, the following json has been made: {exportdata}")
    return exportdata
main()
