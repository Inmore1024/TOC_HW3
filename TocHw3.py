# -*- coding: UTF-8 -*-

#	HW3
#	Name:潘柏豪
#	ID:F74006276
#	Description:
#		自網址讀入讀入jsonn檔後,依所給市區作篩選,
#		再用find()找出地址中有相關路名者,最後將所
#		有符合條件者之總金額作平均
#
#	How-to-use:
#		命令列格式必須要與以下相符:
#			python TocHW3.py 網址 鄉鎮市區 路名 年月份

from datetime import datetime, timedelta
import urllib2, logging, csv, re, json, sys

if len(sys.argv) != 5:
	print 'Input Error!!'
	sys.exit(1)

url = sys.argv[1]
logging.info(url)
cc = urllib2.urlopen(url)
csv_read = csv.reader(cc)
ss = json.load(cc)

ans = 0
cnt = 0
ym = int(sys.argv[4])
if ym < 1000:
	ym = ym * 100
for i in ss:
	arg1 = sys.argv[2].decode('utf-8')
	if i[u'鄉鎮市區'] == arg1:
		strchk = i[u'土地區段位置或建物區門牌']
		arg2 = sys.argv[3].decode('utf-8')
		chk = strchk.find(arg2)
		ymchk = i[u'交易年月']
		if ymchk >= ym:
			if chk >= 0:
				ans += i[u'總價元']
				cnt += 1

print int(ans / cnt)
