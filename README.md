# A-Z Linkrunner

A-Z Link runner is a script to take URLs from a library A-Z list (or other source) and check them for HTTP responses and generates a report.

# Getting Started

Go to your A-Z list and choose the option to show ALL links. Then press CTRL+U (chrome) or right-click and choose "Show Page Source".

This will display the raw HTML of your A-Z list. Select-All and copy the raw HTML to the clipboard.

Load a plain-text editor (such as Notepad or Notepad++) and paste the contents to that file. Call it "a_z_urls.html" and place it in the main script folder.

# Runing the Scripts

### Run 1_get_urls_a_z_list.py. 

This script will search through the raw HTML and pull out the links. It will generate a file called urls.txt in the main script folder.

### Run 2_check_urls_a_z_list.py

This script makes an HTTP call to each URL in the urls.txt file. It will generate a log.txt file that is tabbed delimited and includes the Title, URL, HTTP status code, redirect location, and a blank note field for later use.

You can find a reference of HTTP status codes here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

# Notes

You can use 2_check_urls_a-z_list.py to check any list of urls, including URLs from an Alma analytics report, an EZproxy config file, or similar source.

Keep in mind, though, that if your URL list includes hundreds of links from the same domain, this may cause the vendor to shut down access. In the case of an A-Z list, this is not a concern (single URL per resource), but with other uses, you'll want to add some code or pre-edit the URLs list to only show a single URL per domain source.