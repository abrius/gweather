#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re

# Your agent, can check here: http://whatsmyua.com/  
# (without agent google detect app or programing language and does not show source)
city 	= "Pekin" 
agent 	= "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"
source 	= urllib.request.Request('https://www.google.com/search?q=weather+'+city+'', headers={'User-Agent':agent})
array 	= urllib.request.urlopen(source).read().decode('utf-8')

# find/cut only needed weather data
updated         = re.findall('<div class="wob_dts" id="wob_dts">(.*?),',array, re.U)
temperature     = re.findall('id="wob_tm" style="display:inline">(.*?)</span>',array, re.U) 
precipitation   = re.findall('<span id="wob_pp">(.*?)</span>',array, re.U) 
humidity        = re.findall('<span id="wob_hm">(.*?)</span>',array, re.U) 
wind            = re.findall('<span class="wob_t" id="wob_ws">(.*?)</span>',array, re.U) 
condition       = re.findall('<div class="wob_dcp" id="wob_dcp"><span id="wob_dc">(.*?)</span></div></span>',array, re.U) 

# output
print ("Google weather")
print ("--------------")
print ("City:          "+city)
print ("Condition:     "+condition[0])
print ("Temperature:   "+temperature[0])
print ("Wind:          "+wind[0])
print ("Humidity:      "+humidity[0])
print ("Precipitation: "+precipitation[0])
print ("Updated:       "+updated[0])
