#!/user/bin/env python

import os, sys, urllib.request

url = sys.argv[1]
if len (sys.argv) != 2 :
    sys.exit ("Usage: html_to_jsno <url>")


print("Checking internet connection...")
if urllib.request.urlopen("http://google.com").getcode() == 200:
    print("Network connection ok")
else:
    sys.exit("Network connection failed")
