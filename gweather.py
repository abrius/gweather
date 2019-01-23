#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: https://github.com/abrius

import urllib2
import re

# Your agent, can check here: http://whatsmyua.com/
agent 			= "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"
city 			= "London" 	
source 			= urllib2.Request('https://www.google.com/search?q=weather+'+city+'',headers={'User-Agent':agent})
opening 		= urllib2.urlopen(source) 
array	 		= opening.read() 

updated			= re.findall('<div class="vk_gy vk_sh" id="wob_dts">(.*?)</div>',array, re.U) 
temperature		= re.findall('<span class="wob_t" id="wob_tm" style="display:inline">(.*?)</span>',array, re.U) 
precipitation 	= re.findall('<span id="wob_pp">(.*?)</span>',array, re.U) 
humidity		= re.findall('<span id="wob_hm">(.*?)</span>',array, re.U) 
wind			= re.findall('<span class="wob_t" id="wob_ws">(.*?)</span>',array, re.U) 
condition		= re.findall('<span class="vk_gy vk_sh" id="wob_dc">(.*?)</span></div></span>',array, re.U) 

updated 		= updated[0] 
temperature		= temperature[0]
precipitation 	= precipitation[0]
humidity 		= humidity[0]
wind 			= wind[0]
condition		= condition[0]

print ("Google weather")
print ("--------------")
print ("City:          "+city)
print ("Condition:     "+condition)
print ("Temperature:   "+temperature)
print ("Wind:          "+wind)
print ("Humidity:      "+humidity)
print ("Precipitation: "+precipitation)
print ("Updated:       "+updated)
