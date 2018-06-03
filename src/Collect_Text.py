#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
from requests import session
import csv
from bs4 import BeautifulSoup
import re
#スクレイピング(抽出)に特化した機能を持っている

ignore_list = ["特訓前と共通",""]

def Collect_text():
    print("")
    html = requests.get("https://imascg-slstage-wiki.gamerch.com/%E9%AB%98%E6%A3%AE%E8%97%8D%E5%AD%90#content_2_1")
    #soup = BeautifulSoup(html,"html.parser")

    soup = BeautifulSoup(html.text, 'html.parser')
    #print(soup)

    #print(type(soup))
    #print(soup.prettify())

    #テーブルを指定
    table = soup.findAll("td",{"data-col":"1"},{"style":"text-align:left;"})
    csvFile = open("Yurufuwa_text.csv","wt", newline = "", encoding = "utf-8")
    write = csv.writer(csvFile)

    try:
        for i in table:
            if i.get_text() not in ignore_list:
                yurufuwa_text = re.sub("○○", "プロデューサー", (i.get_text()))
                print(yurufuwa_text)
                write.writerow(yurufuwa_text)
    finally:
        csvFile.close()


    print("finish!!!")

if __name__ == "__main__":
    print("Collecting Text...")
    print("""
        　　　　　　　　　　 　 　 　 　 　 ＿＿＿|:./:./: |:.:|:ﾞ|ハ＼
        　　　　　　　　　　　 　 　_.　＜_.─:.:.:.:.:.:.:⌒＼）_）_）Yi＼＼
        　　　　　　 　 　 　 　 ／:.:.:.:.:.:.:.:.:.:.:.:.:.:. ＼:.:.:.:）_）//）_） )） )）
        　　　　　　　 　 　 .／:.:.:.:.:.:.:.:.:.:.:.:.:.: ＼:.:.:. ＼:.）_）//）_）　〃
        　　　　　 　 　 　 /:.:.:.:.:.:.:.:.:.∧ :. ＼:.:.:ﾞ＼:.:.:.:∨）_）_）人
        　　　　　　　　　 ′:.:.:ﾞ|:.:.:.| |　＼＼:＼ :.: ＼:.:.＼:.ハ　 )）
        　　　 　 　 　 　 |:.:.:.:.:.:|.:.:.:| |　　 ＼＜:.＼:.:.:.＼:.:.＼|
        　　　 　 　 　 　 |:.|l:.:.八: ├　　 　 >芥ｉ(卞、:.:. ＼ｰr─
        　　　 　 　 　 　 |:八:.:.:.: 芥心　　 　 弋zｿ |:.＼「ヽ: |
        　　　　　　　　　　 　＼:八 弋:〉　　 　　: : /:.:.:.:.|ノ）ﾉ
       ゆるふわ～ 　　　　　 　 　 |＼＼　　'　　　　 /:.ｲ:.:. |＼
        　　　　　　　　 　 　 ﾉ:.:.: 人 　 ー‐ ′ .　八:.き )）
        　　　　　　 　 　 　 ／:.:.:.:/＿ ＞　 __. イｉｉ/:.:/）:.:.＼
        　　　　　　　　　 〃/:.:.:.:.|: //ﾞ）　ノ//｝　〈:.:〈（.:.:.:.:.:.:）＼
        　　　　　　 　　　{{｜:.:.:.:.|//ノ（　　| | 　 　＼:.:）:.:.:.:/　　）
        　　　　 　 　 　 　 人:.:.:.:.Ｖ（　　　）| |ヽ　　_／:.:.:／　）（　 〉〉、
        　　　　　　　　　 /: | ＼:.:.∨（ 　　 |r'＼ ／:.:.:イ　　　　 ）//: |
        　　　 　 　 　 　 | :｜:| :）:人＿＿__>上（:.:.（　（　　　r／//／|
        　　　＿＿＿＿_| :｜:|イニニニイ : : : : ＞‐ゝ＿＿_）r// : : /
        　　　|＼＼ : : : ﾉ: : : : : : : : :|: : （/）: : : （/）| |＼ニﾆﾆイ: : .:/
        　　　|　|:＼＼:（ : .: : .: .:ヽ.: :| : : :|.: .: : : .: : :| | :/ : : : : ﾉ:.: .:/  
        """)
    Collect_text()