# htmltojason

#Task
We are developing a blog aggregation service. For the search engine we need a component that identifies links pointing to RSS or Atom feeds.
TASK
Given an HTML document as standard input (you may assume that it is a valid HTML
4.0.1 document), we expect a JSON formatted standard output that contains all the links (the href attributes of all <a> and <link> tags) from the input that point to RSS or Atom feeds, grouped by their type (i.e. into "rss" and "atom" groups).

We consider a link pointing to RSS or Atom feed if the URL is accessible, and served with the proper Content-Type header. Relative links in the input file can be ignored.

You may assume that the system running the script has a reliable network connection and the script
has access to the network. Indenting the output is not necessary, but it has to be a valid JSON format with the proper scheme. You don’t have to validate the internal structure of the RSS or Atom
files, it shall belong to another component of the service.

EXAMPLEOUTPUT
{
"atom": [ "http://example.net/feed", "http://t.co/asdfsf23fdsw234"
],
"rss": [ "http://example.com/rss.xml", "https://example.org/rss2.rss"
]
}

The output must contain both the "rss" and "atom" groups, if there is no link for any of them, they shall be empty arrays.

