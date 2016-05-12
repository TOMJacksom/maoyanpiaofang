# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup



def crawl(url):
    rs = requests.get(url)
    ok = rs.text
    bs = BeautifulSoup(ok)

    pf = bs.find("div", "content strip")
    #print "片名\t\t上映天数\t\t实时票房\t\t票房占比\t\t排片占比\t\t累计票房"
    for movie in pf.find_all("ul"):
        name = movie.find("li", "c1").find("b").text
        shangying = movie.find("li", "c1").find("br").find_next_siblings().pop(0).text
        instant = movie.find("li", "c2").find("b").text
        pfzhanbi = movie.find("li", "c3").text
        ppzhanbi = movie.find("li", "c4").text
        totalpf = movie.find("li", "c5").text.strip()
        print name.ljust(20) + "||", "实时票房:  "+instant, "     "+shangying, "       |||总票房: "+ totalpf, "    票房占比：" + pfzhanbi, "     排片占比：" + ppzhanbi


if __name__ == '__main__':
    crawl("http://pf.maoyan.com/")
