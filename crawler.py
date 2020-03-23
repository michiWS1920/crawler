from bs4 import BeautifulSoup as soup
import requests
import csv
from time import sleep
from random import randint


csv_file = open('crawlerqb.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "GP", "PassYds", "TDPass", "Ints", "RushingYds", "RushTD", "Fumble", "FantasyPoints", "FPperGame"])
years = {"2017/season", "2018/season", "2019/ytd"}
url = "https://www.cbssports.com/fantasy/football/stats/QB/{}/stats/nonppr/"

for year_url in years:
    source = requests.get(url.format(year_url))
    sleep(randint(8,15))
    stats = soup(source.content, "html.parser")

    body = stats.find("tbody")

    for item in body:
        name = item.find("a").text.strip()
        allstats = item.find_all("td", {"class": "TableBase-bodyTd--number"})
        gp = allstats[0].text.strip()
        yds = allstats[3].text.strip()
        tdpass = allstats[5].text.strip()
        ints = allstats[6].text.strip()
        rushyds = allstats[9].text.strip()
        rushtd = allstats[11].text.strip()
        fumble = allstats[12].text.strip()
        fpoints = allstats[13].text.strip()
        fpergame = allstats[14].text.strip()
        print(name, gp, yds, tdpass, ints, rushyds, rushtd, fumble, fpoints, fpergame)
        csv_writer.writerow([name, gp, yds, tdpass, ints, rushyds, rushtd, fumble, fpoints, fpergame])

csv_file.close()

