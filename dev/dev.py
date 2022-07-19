import requests  # it allows us to take html files
import re
from bs4 import BeautifulSoup  # for scraping

## CODE WHICH HITS THE POSTOJ REPEATADELY
# res = requests.get('https://www.postoj.sk/v-skratke')
# with open('../media_code/postoj_html.txt',mode='w+') as html_raw:
#     html_raw.write(res.text)
#     html_raw.close()
# soup = BeautifulSoup(res.text, 'html.parser')
# most_read_articles = soup.select('.track-me-pls')
# print(most_read_articles[0])


with open('../media_code/postoj_html.txt', mode='r') as html_raw:
    soup = BeautifulSoup(html_raw.read(), 'html.parser')
    html_raw.close()

todays_articles = soup.find("div", {"id": "today-popular-articles"})
weeklys_articles = soup.find("div", {"id": "week-popular-articles"})

# load the index file file
with open("../templates/index_backup.html") as indx:
    txt = indx.read()
    soup_indx = BeautifulSoup(txt, 'html.parser')
    soup_indx.hr.insert_after(todays_articles)
    # soup_indx.body.script.insert_before(todays_articles)
    indx.close()

# save the file again
with open("../templates/index.html", "w") as outf:
    outf.write(str(soup_indx.prettify(formatter="html")))
