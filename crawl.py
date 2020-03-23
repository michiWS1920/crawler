from bs4 import BeautifulSoup as soup
import requests
import csv
from time import sleep
from random import randint


csv_file = open('crawlerRB.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "GP", "RushAttempts", "RushYds", "RushTD", "ReceivingYds", "ReceivingTD",  "Fumble", "FantasyPoints", "FPperGame"])
years = {"2017/season", "2018/season", "2019/ytd"}
url = "https://www.cbssports.com/fantasy/football/stats/RB/{}/stats/nonppr/"

for year_url in years:
    source = requests.get(url.format(year_url))
    sleep(randint(8,15))
    stats = soup(source.content, "html.parser")

    body = stats.find("tbody")

    for item in body:
        try:
            name = item.find("a").text.strip()
        except:
            pass
        allstats = item.find_all("td", {"class": "TableBase-bodyTd--number"})
        gp = allstats[0].text.strip()
        rushattempts = allstats[1].text.strip()
        rushyds = allstats[2].text.strip()
        rushtds = allstats[4].text.strip()
        receivingyds = allstats[6].text.strip()
        receivingtd = allstats[9].text.strip()
        fumble = allstats[10].text.strip()
        fpoints = allstats[11].text.strip()
        fpergame = allstats[12].text.strip()
        print(name, gp, rushattempts, rushyds, rushtds, receivingyds, receivingtd, fumble, fpoints, fpergame)
        csv_writer.writerow([name, gp, rushattempts, rushyds, rushtds, receivingyds, receivingtd, fumble, fpoints, fpergame])

csv_file.close()

