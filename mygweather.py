#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Ernestas Žaglinskas
# fb: 	  facebook.com/abrius   
# mail:   virtualybe@gmail.com
# support only python2

import urllib2
import re
import shutil


#### SETTINGS ####  (don't remove browser agent, don't work without it. You can put your own agent) 
agent 	 	= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.90"
city 		= "Kuršėnai"
home_dir 	= "/home/abrius/"
icon_dir 	= "/home/abrius/gweather/"
#### SETTINGS ####


# read source 
source 		= urllib2.Request('https://www.google.com/search?q=weather+'+city+'',headers={'User-Agent':agent})
opening		= urllib2.urlopen(source) 
array	 	= opening.read() 

# find/cut only needed weather data
ic				= re.findall('onebox/weather/64/(.*?).png',array, re.U) 
updated			= re.findall('<div class="vk_gy vk_sh" id="wob_dts">(.*?)</div>',array, re.U) 
temperature		= re.findall('<span class="wob_t" id="wob_tm" style="display:inline">(.*?)</span>',array, re.U) 
precipitation 	= re.findall('<span id="wob_pp">(.*?)</span>',array, re.U) 
humidity		= re.findall('<span id="wob_hm">(.*?)</span>',array, re.U) 
wind			= re.findall('<span class="wob_t" id="wob_ws">(.*?)</span>',array, re.U) 
condition		= re.findall('<span class="vk_gy vk_sh" id="wob_dc">(.*?)</span></div></span>',array, re.U) 

# data from array
ic				= ic[0]
icon 			= ic+".png"
updated 		= updated[0] 
temperature		= temperature[0]
precipitation 	= precipitation[0]
humidity 		= humidity[0]
wind 			= wind[0]
condition		= condition[0]

# remove week day name from update status, 
# show only time, ex: Updated: 20:25 
# (you can remove this block, if you want, then you get: Updated: 20:25, saturday)
updated 	= updated.replace('pirmadienis','') 	# monday
updated 	= updated.replace('antradienis','') 	# tuesday
updated 	= updated.replace('trečiadienis','')	# wednesday
updated 	= updated.replace('ketvirtadienis','') 	# thursday
updated 	= updated.replace('penktadienis','') 	# friday
updated 	= updated.replace('šeštadienis','') 	# saturday
updated 	= updated.replace('sekmadienis','') 	# sunday
updated 	= updated.replace(', ','')				# remove comma and space 


# translate from Lithuania to English language,
# because city is in Lithuania country 
# (if remove this condition block, then condition be in your language)
condition 	= condition.replace('Debesuota', 					'Cloudy')
condition 	= condition.replace('Sniegas',						'Snow')
condition 	= condition.replace('sniegas',						'snow')
condition 	= condition.replace('Saulėta',						'Sunny')
condition 	= condition.replace('Lietus',						'Rain')
condition 	= condition.replace('ir',							'and')
condition 	= condition.replace('Trumpas nestiprus lietus', 	'Light Rain')
condition 	= condition.replace('Truputį pasnigs', 				'Light snow')
condition 	= condition.replace('Daugumoje rajonų debesuota', 	'Mostly Cloudy')
condition 	= condition.replace('Daugumoje rajonų saulėta', 	'Mostly Sunny')
condition 	= condition.replace('Protarpiais debesuota', 		'Partly Cloudy')
condition 	= condition.replace('Giedra, protarpiais debesuota','Clear, partly cloudy')

# copy icon from gweather folder to home folder and rename it to gweather.png, afer that conky show gweather.png image.
if icon == "partly_cloudy.png": shutil.copy2(icon_dir+'28.png', home_dir+'gweather.png') # partly_cloudy
if icon == "rain.png": 			shutil.copy2(icon_dir+'11.png', home_dir+'gweather.png') # rain
if icon == "rain_light.png": 	shutil.copy2(icon_dir+'9.png',  home_dir+'gweather.png') # rain_light 
if icon == "rain_heavy.png": 	shutil.copy2(icon_dir+'12.png', home_dir+'gweather.png') # rain_heavy
if icon == "cloudy.png": 		shutil.copy2(icon_dir+'26.png', home_dir+'gweather.png') # cloudy
if icon == "sunny.png": 		shutil.copy2(icon_dir+'36.png', home_dir+'gweather.png') # sunny
if icon == "snow.png": 			shutil.copy2(icon_dir+'14.png', home_dir+'gweather.png') # snow
if icon == "snow_light.png":	shutil.copy2(icon_dir+'13.png', home_dir+'gweather.png') # snow_light
f = open(icon,'wb')
f.write(urllib2.urlopen('https://ssl.gstatic.com/onebox/weather/64/'+icon).read())
f.close()

# output
print ("City:          "+city)
print ("Condition:     "+condition)
print ("Temperature:   "+temperature+'°')
print ("Wind:          "+wind)
print ("Humidity:      "+humidity)
print ("Precipitation: "+precipitation)
print ("Updated:       "+updated)
