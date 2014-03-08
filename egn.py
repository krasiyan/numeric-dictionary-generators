#!/usr/bin/python
import datetime

def egn_checksum(egn):
	es = 0
	for i in range(9):
		es += int(egn[i])* weights[i]
	vs = es % 11
	if vs == 10: vs = 0
	return str(vs)
	
f = open('EGN.txt','w')
ys = raw_input('Start year - YYYY - def. 2012:')
ye = raw_input('End year - YYYY - def. 2012:')
regs = raw_input('Region start - def. 000:')
rege = raw_input('Region end - def. 999:')
sex = raw_input('Sex - 0m/1f - def. both:')
if ys == "": ys = 2012
else: ys = int(ys)

if ye == "": ye = 2012
else: ye = int(ye)

if regs == "": regs = 0
else: regs = int(regs)

if rege == "": rege = 999
else: rege = int(rege)

if sex == "": sex = -1
else: sex = int(sex)

d = datetime.date(int(ys),1,1)
delta = datetime.timedelta(days=1)
weights = [2,4,8,5,10,9,7,3,6]

while d.year <= ye:
	if (d.year / 100) >= 20: month = str(d.month + 40)
	if (d.year / 100) == 18: month = str(d.month + 20)
	else: month = str(d.month)
	
	egn = str(d.year)[2:4] + month.zfill(2) + str(d.day).zfill(2)
	
	for i in range(regs,rege+1):
		if int(sex) == 0 and (i % 10) % 2 != 0: continue
		if int(sex) == 1 and (i % 10) % 2 == 0: continue
		tegn = egn + str(i).zfill(3);
#		print tegn + egn_checksum(tegn)
		f.write(tegn + egn_checksum(tegn) + "\n")

	d += delta

f.close();
