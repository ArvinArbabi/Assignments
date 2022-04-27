# this code gathers the amount of times a certain word appears in a website
from datetime import date
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
import urllib.request, re

# the URL of the website described as a constant 
WEBSITE_URL = 'http://www.nasonline.org'
# the words that are selected to be counted in the url described as a constant
TOPICS = ["research", "climate", "evolution", "cultural", "leadership", "awards"]
# empty dictionary to store the topics and the amount of times they appear
word_count = {}

# HTMLParser class that parses the html data
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        # for loop that reads through the data provided by the website to count
        # the amount of times 'TOPICS' appears
        for pattern in TOPICS:    
            count = len(re.findall(pattern, data, re.IGNORECASE))
            if pattern in word_count:
                word_count[pattern] += count
            else:
                word_count[pattern] = count

# main function that opens and closes the url
def crawl_website():
    # prints today's date
    today = date.today()
    print("today's date is:", today)

    # opens and closes url and also checks for exceptions
    try:
        with urllib.request.urlopen(WEBSITE_URL) as res:
            html_content = res.read().decode('utf-8')
    except HTTPError:
        print("not connected to internet")
    except URLError:
        print("Invalid URL!")
    finally:
        if res != None: 
            res.close()
    
    parser = MyHTMLParser()
    parser.feed(html_content)
    parser.close()
    # formats the text
    for topic in word_count:
        print("{} appears {} times.".format(topic, word_count[topic]))

# calls the function
crawl_website()

# ===============================================================================================================================[test run]=======
# PS C:\work\assignments\lab9>  c:; cd 'c:\work\assignments\lab9'; & 'C:\Users\arvin_5blwkdx\AppData\Local\Microsoft\WindowsApps\python3.9.exe' 'c:\Users\arvin_5blwkdx\.vscode\extensions\ms-python.python-2022.4.1\pythonFiles\lib\python\debugpy\launcher' '64656' '--' 'c:\work\assignments\lab9\ArvinArbabiLab9.py'
# today's date is: 2022-04-19
# research appears 7 times.
# climate appears 1 times.
# evolution appears 1 times.
# cultural appears 3 times.
# leadership appears 2 times.
# awards appears 4 times.
# PS C:\work\assignments\lab9>