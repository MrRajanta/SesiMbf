#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : search_name.py                     #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import os, re, sys, json
dari  bs4  impor  BeautifulSoup  sebagai  parser
e  =  i . find ( 'div' )
				if '+' in str(name) or name == None:
					continue
				lain 
					full_name = str(name.text.encode('utf-8'))
					if 'profile.php?id=' in str(i):
						uid = re.findall(r'\?id=(.*?)&', str(i))
					else:
						uid = re.findall('/(.*?)\?refid=', str(i))
					if len(uid) == 1:
						id.append({'uid': uid[0], 'name': full_name})
					sys.stdout.write("\r - %s                                        \r\n[\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Writing Id don't close."%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
					if len(id) == max or len(id) > max:
						statusStop = True
						break
			if statusStop == False:
				if 'Lihat Hasil Selanjutnya' in str(html):
					url_search = html.find('a', string='Lihat Hasil Selanjutnya')['href']
				else: break
			else: break
		except KeyboardInterrupt:
			print('\n\n\033[0;91mKeyInterrupt, stopped!!\033[0m')
			break
	try:
		for filename in os.listdir('dump'):
			os.remove('dump/'+filename)
	except: pass
	print('\n\nOutput: '+output)
	save  =  open ( output , 'w' 
	simpan . tulis ( json . dumps ( id ))
	simpan . tutup ()
