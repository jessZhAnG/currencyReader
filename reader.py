import urllib
import sys
import re

web = r'http://www.boc.cn/sourcedb/whpj/enindex.html'
td = r'</td>'
td1 = r'<td bgcolor="#FFFFFF">'
def read_currency(cur):
    cur = cur.upper()
    
    f = urllib.urlopen(web)
    
    found = False
    while 1:
       text = f.readline().strip()
       if text.lower() == '</html>':
          break
       try:
          loc = text.index(cur)
          if loc > 0:
             found = True
             break
       except:
          pass
    
    if found is True:
       bank_buy_wire = f.readline().strip()
       bank_sell = f.readline().strip()
       bank_buy = f.readline().strip()
       
       refine_buy_wire = re.sub(td,"",re.sub(td1,"",bank_buy_wire))
       refine_sell = re.sub(td,"",re.sub(td1,"",bank_sell))
       refine_buy = re.sub(td,"",re.sub(td1,"",bank_buy))
       
       print "Exchange Rate For",cur
       print "Bank Buy", refine_sell
       print "Bank Sell", refine_buy
       print "Bank Buy (wire)", refine_buy_wire
       print
       print "Source: Bank of China"
       
    else:
       print "We dont find a currency exchange rate you entered!"
       


if __name__ == '__main__':
   #check arguments
   argc = len(sys.argv)
   
   if argc != 2:
      print 'just put the currency as the first argument!'
      print 'program is about to exit!'
      sys.exit(5)
   
   argv = sys.argv[1]
   
   print 'Wait a Moment while reading data'
   print 
   read_currency(argv)
