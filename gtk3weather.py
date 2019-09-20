#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import urllib.request
import re
import subprocess

cfg_file = "cities.txt" # create config file with your city list

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):    

        grid = Gtk.Grid()
        grid.set_column_spacing(0)
        self.add(grid)            
        
        entry_1 = Gtk.Entry()
        grid.attach(entry_1, 0, 0, 1, 1)
        entry_1.set_width_chars(10)        

        combo = Gtk.ComboBoxText()
        grid.attach(combo, 0, 1, 1, 1)

        if os.path.exists(cfg_file):
            lines_list = open(cfg_file).read().splitlines()
            lines_list = list(filter(None, lines_list))
        else:
            lines_list = open(cfg_file, "w+")

        for t in lines_list:
            combo.append_text(t)
        combo.set_active(0)

        button = Gtk.Button(label="Add City")
        grid.attach(button, 1, 0, 2, 1)
        button.connect("clicked", self.on_add, entry_1, combo)

        button2 = Gtk.Button(label="Show")
        grid.attach(button2, 1, 1, 1, 1)
        button2.connect("clicked", self.on_show, combo)

        button3 = Gtk.Button(label="Remove City")
        grid.attach(button3, 2, 1, 1, 1)
        button3.connect("clicked", self.on_remove, combo)

        self.label_1 = Gtk.Label(label=" City")
        grid.attach(self.label_1, 0, 2, 1, 1)
        self.label_1.set_xalign(0);
        self.label_1.set_yalign(0);
        self.label_2 = Gtk.Label(label=" Condition")
        grid.attach(self.label_2, 0, 3, 1, 1)
        self.label_2.set_xalign(0);
        self.label_2.set_yalign(0);
        self.label_3 = Gtk.Label(label=" Temperature")
        grid.attach(self.label_3, 0, 4, 1, 1)
        self.label_3.set_xalign(0);
        self.label_3.set_yalign(0);
        self.label_4 = Gtk.Label(label=" Wind")
        grid.attach(self.label_4, 0, 5, 1, 1)
        self.label_4.set_xalign(0);
        self.label_4.set_yalign(0);
        self.label_5 = Gtk.Label(label=" Precipitation")
        grid.attach(self.label_5, 0, 6, 1, 1)
        self.label_5.set_xalign(0);
        self.label_5.set_yalign(0);
        self.label_6 = Gtk.Label(label=" Humidity")
        grid.attach(self.label_6, 0, 7, 1, 1)
        self.label_6.set_xalign(0);
        self.label_6.set_yalign(0);
        self.label_7 = Gtk.Label(label=" Updated")
        grid.attach(self.label_7, 0, 8, 1, 1)
        self.label_7.set_xalign(0);
        self.label_7.set_yalign(0);

        self.label_8 = Gtk.Label(label="")
        grid.attach(self.label_8, 1, 2, 2, 1)
        self.label_8.set_xalign(0);
        self.label_8.set_yalign(0);
        self.label_9 = Gtk.Label(label="")
        grid.attach(self.label_9, 1, 3, 2, 1)
        self.label_9.set_xalign(0);
        self.label_9.set_yalign(0);
        self.label_10 = Gtk.Label(label="")
        grid.attach(self.label_10, 1, 4, 2, 1)
        self.label_10.set_xalign(0);
        self.label_10.set_yalign(0);
        self.label_11 = Gtk.Label(label="")
        grid.attach(self.label_11, 1, 5, 2, 1)
        self.label_11.set_xalign(0);
        self.label_11.set_yalign(0);
        self.label_12 = Gtk.Label(label="")
        grid.attach(self.label_12, 1, 6, 2, 1)
        self.label_12.set_xalign(0);
        self.label_12.set_yalign(0);
        self.label_13 = Gtk.Label(label="")
        grid.attach(self.label_13, 1, 7, 2, 1)
        self.label_13.set_xalign(0);
        self.label_13.set_yalign(0);
        self.label_14 = Gtk.Label(label="")
        grid.attach(self.label_14, 1, 8, 2, 1)
        self.label_14.set_xalign(0);
        self.label_14.set_yalign(0);

        self.set_border_width(5)
        self.set_title("Google Weather")
        self.connect("destroy", Gtk.main_quit)

    def on_show(self, widget, combo):
        getcitycombo = combo.get_active_text()
        getcitycombo = getcitycombo.replace(' ','+')

        agent  = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.88"
        source = urllib.request.Request('https://www.google.com/search?q=weather+'+getcitycombo+'', headers={'User-Agent':agent})
        array  = urllib.request.urlopen(source).read().decode('utf-8')

        # find and cut only needed weather data
        updated         = re.findall('<div class="vk_gy vk_sh" id="wob_dts">(.*?)</div>',array, re.U)
        temperature     = re.findall('<span class="wob_t" id="wob_tm" style="display:inline">(.*?)</span>',array, re.U) 
        precipitation   = re.findall('<span id="wob_pp">(.*?)</span>',array, re.U) 
        humidity        = re.findall('<span id="wob_hm">(.*?)</span>',array, re.U) 
        wind            = re.findall('<span class="wob_t" id="wob_ws">(.*?)</span>',array, re.U) 
        condition       = re.findall('<span class="vk_gy vk_sh" id="wob_dc">(.*?)</span></div></span>',array, re.U) 

        condition       = '\n'.join(condition)
        temperature     = '\n'.join(temperature)
        wind            = '\n'.join(wind)
        precipitation   = '\n'.join(precipitation)
        humidity        = '\n'.join(humidity)
        updated         = '\n'.join(updated)

        getcitycombo = getcitycombo.replace('+',' ')
        self.label_8.set_label(' '+getcitycombo)
        self.label_9.set_label(' '+condition)
        self.label_10.set_label(' '+temperature+'°')
        self.label_11.set_label(' '+wind)
        self.label_12.set_label(' '+precipitation)
        self.label_13.set_label(' '+humidity)
        self.label_14.set_label(' '+updated)
        return 

    def on_add(self, widget, entry_1, combo):
        getcity = entry_1.get_text()
        f = open(cfg_file, 'a+') 
        f.write(getcity+'\n')
        f.close()
        lines_list = open(cfg_file).read().splitlines()
        lines_list = list(filter(None, lines_list)) 
        combo.remove_all()
        entry_1.set_text("")
        
        for t in lines_list:            
            combo.append_text(t)      
        return

    def on_remove(self, widget, combo):
        remove_item = combo.get_active_text()
        #subprocess.call(['sed','-i','/.*'+remove_item+'.*/d',cfg_file]) #for unix
        with open(cfg_file,"r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if remove_item not in line:
                    f.write(line)
            f.truncate()
        combo.remove_all()
        lines_list = open(cfg_file).read().splitlines()
        lines_list = list(filter(None, lines_list)) # fastest  
        
        for t in lines_list:            
            combo.append_text(t)
        return

win = MyWindow()
win.show_all()
Gtk.main()

