#!/usr/bin/python
f = open('phone_numbers_bg.txt','w')

for n1 in range (0,1):
	for n2 in range(8,10):
		for n3 in range(9,5,-1):
			for n4 in range(9,-1,-1):
				for n5 in range(9,-1,-1):
					for n6 in range(9,-1,-1):
						for n7 in range(9,-1,-1):
							for n8 in range(9,-1,-1):
								for n9 in range(9,-1,-1):
									for n10 in range(9,-1,-1):
										#print str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+str(n10)
										f.write(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+str(n10)+"\n")
										
f.close();
