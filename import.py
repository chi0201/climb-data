from ctypes import sizeof
from logging.handlers import BaseRotatingHandler
from pickle import TRUE
from pkgutil import iter_importers
from unittest.mock import sentinel
import requests 
from bs4 import BeautifulSoup 
import csv
from hanziconv import HanziConv

r = requests.get("https://online.carrefour.com.tw/zh/homepage/" )
if r.status_code == 200 :
    soup = BeautifulSoup( r.text, "html.parser" )
    types = soup.select( 'div.top1 left-item' )
    print( types )
    #for type in types :
     #   print( type.h3.string )


"""
size_str = []
# catch "飲料"
for i in range( 0, 700, 24) :
    #將網頁資料Get下來
    r = requests.get("https://online.carrefour.com.tw/zh/%E9%A3%B2%E6%96%99%E9%9B%B6%E9%A3%9F/%E8%8C%B6%E9%A3%B2%2F%E5%92%96%E5%95%A1?start=" + str(i) + "#" )
    if r.status_code == 200 :
        print( 'Html get success-' + str(i) )
        soup = BeautifulSoup( r.text, "html.parser" ) #將網頁資料以html.parser

        sel = soup.find_all( 'div', class_ = 'commodity-desc' )  #取得物品名稱

        size_str.clear()
        span_siz = soup.select("div.box-img")                    #取得幾入裝
        for span in span_siz :
            if span.find( 'span' ) == None :
                size_str.append( '1入' ) 
            else :
                size_str.append( span.find('span').text )

        
        price = soup.find_all( 'div', class_ = 'current-price')   #取得價格
        with open ( 'output.csv', 'a', newline = '' ) as csvfile :
            writer = csv.writer( csvfile ) 
            for s, Qty, money in zip(sel, size_str, price) :
                writer.writerow( [HanziConv.toTraditional(s.select_one( 'a' ).getText()), 
                                  Qty, 
                                  money.select_one('em').getText()] )
   
    else :
        print( 'Html get fail.' ) 
"""
