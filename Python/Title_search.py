
import urllib.request, ssl, os, re

# set website to a variable
site = "http://cgi.soic.indiana.edu/~dpierz/news.html"

# open, read the page then close the page
context = ssl._create_unverified_context()
web_page = urllib.request.urlopen(site, context=context)
lines = web_page.read().decode(errors="replace")
web_page.close()

filename = os.path.basename(site)

# go through the page and find all the titles of the links under the news section
# titles are surrounded by itemprop="headline"> and </span>
titles = re.findall('(?<=itemprop="headline">).+?(?=</span>)',lines,re.DOTALL)

# print searchng then the site name
print("Searching:",site + "\n")

# from the list of the titles go though each one and print it out with it
# tabbed and a new line between each title
news_titles = [print("\t" + item + "\n") for item in titles]


# Get an input from the user 
term = input("Please enter a word to search for: ")


# go through the titles and print out the titles that contain the users search
# make sure to check for first letter capitalized or all lower case
for item in titles:
    if term.title() in item.title() or term.lower() in item.lower():
        print("\n" + item + "\n")

#search_results = [print(item + "\n") for item in titles if term.title() in item or term.lower() in item]
#print(search_results)
        


