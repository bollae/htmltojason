<h3>Export RSS and Atom feeds URLs from HTML to JSON</h3>

<h4>Task</h4>
Given an HTML document as standard input (you may assume that it is a valid HTML
4.0.1 document), we expect a JSON formatted standard output that contains all the links (the href attributes of all <a> and <link> tags) from the input that point to RSS or Atom feeds, grouped by their type (i.e. into "rss" and "atom" groups).

We consider a link pointing to RSS or Atom feed if the URL is accessible, and served with the proper Content-Type header. Relative links in the input file can be ignored.

You may assume that the system running the script has a reliable network connection and the script
has access to the network. Indenting the output is not necessary, but it has to be a valid JSON format with the proper scheme. You don’t have to validate the internal structure of the RSS or Atom
files, it shall belong to another component of the service.

EXAMPLE OUTPUT <br>
{<br>
"atom": [ "http://example.net/feed", "http://t.co/asdfsf23fdsw234"<br>
],<br>
"rss": [ "http://example.com/rss.xml", "https://example.org/rss2.rss"<>br
]<br>
}<br>
The output must contain both the "rss" and "atom" groups, if there is no link for any of them, they shall be empty arrays.

<h4>Install, requirements</h4>
The script has written in Python3.7.<br>
OS: CentOS Linux ebolla1c.mylabserver.com 3.10.0-957.12.1.el7.x86_64 #1 SMP Mon Apr 29 14:59:59 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
I've installed git and python 3.7:<br>
yum install git<br>
yum groupinstall -y "development tools"<br>
wget http://python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz<br>
tar xf Python-3.7.2.tar.xz<br>
./configure --enable-optimization<br>
make altinstall<br>
pip3.7 install --upgrade pip<br>
pip3.7 list<br>
Package        Version<br>
-------------- -------<br>
beautifulsoup4 4.8.0  <br>
bs4            0.0.1  <br>
pip            19.2.3 <br>
setuptools     41.2.0 <br>
soupsieve      1.9.3  <br>

It don't need to install the script, only the Python enviroment. Just clone my github repository:
git clone https://github.com/bollae/htmltojason.git

<h4>Usage</h4>
 The script has one positional argument: url. Use the following format: http(s)://url.
 The script downloads the html page, checks it and explores the html code to find rss and atom feed with absolut path. The script search the content type (application/rss+xml or application/atom+xml). Fedds with relative path will be ignored.
<h4>Tests, examples</h4>
<h5>Run script without arguments and use -h</h5>
htmltojason# python3.7 main.py<br>
usage: main.py [-h] url <br>
main.py: error: the following arguments are required: url<br>
htmltojason]# python3.7 main.py -h<br>
usage: main.py [-h] url<>br
<br>
HTML to JSON<br>
<br>
positional arguments: <br>
  url         Input url to download html file. Format: http(s)://url<br>
<br>
optional arguments:<br>
  -h, --help  show this help message and exit<br>
<h5>Found RSS and Atom feeds</h5>
htmltojason]# python3.7 main.py https://firecakesworld.com/feed<br>
Checking internet connection...<br>
Network connection ok<br>
Input html: https://firecakesworld.com/feed<br>
https://firecakesworld.com/feed is a valid html file, continue process...<br>
Found https://firecakesworld.com/feeds/atom<br>
Found https://firecakesworld.com/feeds/rss<br>
Job completed, the following json has been made: {"rss": ["https://firecakesworld.com/feeds/rss"], "atom": ["https://firecakesworld.com/feeds/atom"]}<br>
<h5>Found RSS or Atom feeds</h5>
htmltojason]# python3.7 main.py https://wwd.com/rss-feeds/<br>
Checking internet connection...<br>
Network connection ok<br>
Input html: https://wwd.com/rss-feeds/<br>
https://wwd.com/rss-feeds/ is a valid html file, continue process...<br>
Found https://wwd.com/feed/<br>
Found https://wwd.com/comments/feed/<br>
Found https://wwd.com/rss-feeds/feed/<br>
Job completed, the following json has been made: {"rss": ["https://wwd.com/feed/", "https://wwd.com/comments/feed/", "https://wwd.com/rss-feeds/feed/"], "atom": []}<br>
