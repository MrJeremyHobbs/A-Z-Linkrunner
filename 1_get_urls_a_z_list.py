from bs4 import BeautifulSoup
import os

# clean-up
try:
    os.remove('urls.txt')
except FileNotFoundError:
    pass

# grab URLS and titles
#
# To get a raw HTML file of your A-Z list (assuming you can). Go to your A-Z list
# and choose the option to show ALL links. Then press CTRL+U (chrome) to show the

#

soup = BeautifulSoup(open("a_z_urls.html", encoding="utf-8").read())

for a in soup.find_all('a', href=True):
    if a['href'].startswith("http"):
        title = a.contents[0]
        url = a['href']

        if title != " ":
            # write to file
            with open('urls.txt', 'a', newline="\n", encoding="utf-8") as txtfile:
                txtfile.write(f'{title}\t{url}\n')