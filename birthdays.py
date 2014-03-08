#!/usr/bin/python
import datetime
f =  open('birthday_dates.txt','w')
yfrom = 1920
yto = 2014
c = datetime.date(yfrom,1,1)
delta = datetime.timedelta(days=1)
while c.year <= yto:
	d = str(c.day).zfill(2)
	m = str(c.month).zfill(2)
	y = str(c.year)
	
	f.write(d+m+y+"\n")
	f.write(m+d+y+"\n")
	f.write(y+m+d+"\n")
	f.write(y+d+m+"\n")
	f.write(m+y+d+"\n")
	f.write(d+y+m+"\n")
	c += delta
f.close()
