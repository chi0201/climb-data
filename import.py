from ctypes import sizeof
from logging.handlers import BaseRotatingHandler
import requests 
from bs4 import BeautifulSoup 
import csv

size_str = []

r = requests.get("https://online.carrefour.com.tw/zh/%E9%A3%B2%E6%96%99%E9%9B%B6%E9%A3%9F/%E8%8C%B6%E9%A3%B2%2F%E5%92%96%E5%95%A1/%E7%B6%A0%E8%8C%B6%2F%E7%83%8F%E9%BE%8D%E8%8C%B6%2F%E5%85%B6%E4%BB%96%E8%8C%B6%E9%A3%B2?start=0#" )
soup = BeautifulSoup( r.text, "html.parser" ) #將網頁資料以html.parser
sel = soup.find_all( 'div', class_ = 'commodity-desc' )

#siz = soup.find_all( 'span', class_ = 'packageQty')  # maybe can delete
#for i in siz :
    #print( i.select_one("span" ).getText() )

data_siz = soup.select("div.box-img a")
for data in data_siz :
    if len( data.get('data-variant').split() ) == 3 :
        size_str.append( data.get('data-variant').split()[2] )
        #print( data.get('data-variant').split() )
    else :
        size_str.append( "1" )
    

price = soup.find_all( 'div', class_ = 'current-price')

for s, Qty, money in zip(sel, size_str, price) :
    print( [s.select_one( 'a' ).getText(), Qty, money.select_one('em').getText()] )


"""
for i in range( 0, 217, 24) :
    #將網頁資料Get下來
    r = requests.get("https://online.carrefour.com.tw/zh/%E9%A3%B2%E6%96%99%E9%9B%B6%E9%A3%9F/%E8%8C%B6%E9%A3%B2%2F%E5%92%96%E5%95%A1/%E7%B6%A0%E8%8C%B6%2F%E7%83%8F%E9%BE%8D%E8%8C%B6%2F%E5%85%B6%E4%BB%96%E8%8C%B6%E9%A3%B2?start=" + str(i) + "#" )
    if r.status_code == 200 :
        print( 'Html get success' )
        soup = BeautifulSoup( r.text, "html.parser" ) #將網頁資料以html.parser
        sel = soup.find_all( 'div', class_ = 'commodity-desc' )
        #siz = soup.find_all( 'span', class_ = 'packageQty')

        data_siz = soup.select("div.box-img a")
        for data in data_siz :
            if len( data.get('data-variant').split() ) == 3 :
                size_str.append( data.get('data-variant').split()[2] )
                #print( data.get('data-variant').split() )
            else :
                size_str.append( "1" )
        
        price = soup.find_all( 'div', class_ = 'current-price')
        with open ( 'output.csv', 'a', newline = '' ) as csvfile :
            writer = csv.writer( csvfile ) #, delimiter = ' ' ) 
            for s, Qty, money in zip(sel, size_str, price) :
                writer.writerow( [s.select_one( 'a' ).getText(), Qty, money.select_one('em').getText()] )
        #for s, Qty, money in zip(sel, size, price) :
        #    print( s.select_one( 'a' ).getText(), Qty.text, money.select_one('em').getText() )
   
    else :
        print( 'Html get fail.' ) 
"""
