from bs4 import BeautifulSoup as soup
import requests
import csv
from time import sleep
from random import randint


csv_file = open('crawlerWR.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "GP", "Targets", "RecYds", "RecTD", "Fumble", "FantasyPoints", "FPperGame"])
years = {"2017/season", "2018/season", "2019/ytd"}
url = "https://www.cbssports.com/fantasy/football/stats/TE/{}/stats/nonppr/"

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
        targets = allstats[1].text.strip()
        receptions = allstats[2].text.strip()
        recyds = allstats[3].text.strip()
        rectds = allstats[6].text.strip()
        fumble = allstats[7].text.strip()
        fpoints = allstats[8].text.strip()
        fpergame = allstats[9].text.strip()
        print(name, gp, targets, receptions, recyds, rectds, fumble, fpoints, fpergame)
        csv_writer.writerow([name, gp, targets, receptions, recyds, rectds, fumble, fpoints, fpergame])

csv_file.close()