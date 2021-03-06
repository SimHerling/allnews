import requests  # it allows us to take html files
import re
from bs4 import BeautifulSoup  # for scraping

# # GET POSTOJ'S HTML
# res = requests.get('https://www.postoj.sk/v-skratke')
# with open('../media_code/postoj_html.txt',mode='w+') as html_raw:
#     html_raw.write(res.text)
#     html_raw.close()
# # soup = BeautifulSoup(res.text, 'html.parser')
# # most_read_articles = soup.select('.track-me-pls')
# # print(most_read_articles[0])

# # GET HN ONLINE'S HTML
# res = requests.get('https://hnonline.sk/finweb')
# with open('../media_code/hnfinweb_html.txt',mode='w+') as html_raw:
#     html_raw.write(res.text)
#     html_raw.close()

# # GET HN ONLINE'S HTML
# res = requests.get('https://hnonline.sk/svet')
# with open('../media_code/hnsvet_html.txt',mode='w+') as html_raw:
#     html_raw.write(res.text)
#     html_raw.close()
#
# # GET HN ONLINE'S HTML
# res = requests.get('https://hnonline.sk/slovensko')
# with open('../media_code/hnslovensko_html.txt',mode='w+') as html_raw:
#     html_raw.write(res.text)
#     html_raw.close()

# GET PRAVDA'S HTML
res = requests.get('https://pravda.sk')
with open('../media_code/pravda_html.txt',mode='w+') as html_raw:
    html_raw.write(res.text)
    html_raw.close()

## Postoj Parsing
with open('../media_code/postoj_html.txt', mode='r') as html_raw:
    soup = BeautifulSoup(html_raw.read(), 'html.parser')
    html_raw.close()

postoj_todays_articles = soup.find("div", {"id": "today-popular-articles"})
postoj_weeklys_articles = soup.find("div", {"id": "week-popular-articles"})

# load the index file file
with open("../templates/index_backup.html") as indx:
    txt = indx.read()
    soup_indx = BeautifulSoup(txt, 'html.parser')
    soup_indx.hr.insert_after(postoj_todays_articles)
    # soup_indx.hr.insert_after(postoj_weeklys_articles)
    indx.close()

# save the file again
with open("../templates/index.html", "w") as outf:
    outf.write(str(soup_indx.prettify(formatter="html")))
    outf.close()




## Pravda Parsing
with open('../media_code/pravda_html.txt', mode='r') as html_raw:
    soup = BeautifulSoup(html_raw.read(), 'html.parser')
    html_raw.close()

pravda_todays_articles = soup.find("ol", {"class": "interval-list-1"})
pravda_weeklys_articles = soup.find("ol", {"class": "interval-list-3"})

# print(pravda_todays_articles)

# load the index file file
with open("../templates/index.html") as indx:
    txt = indx.read()
    soup_indx = BeautifulSoup(txt, 'html.parser')
    soup_indx.script.insert_before(pravda_todays_articles)
    # soup_indx.hr.insert_after(pravda_weeklys_articles)
    indx.close()

# save the file again
with open("../templates/index.html", "w") as outf:
    outf.write(str(soup_indx.prettify(formatter="html")))
    outf.close()