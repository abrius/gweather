#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import urllib.request
import re
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QLineEdit

cfg_file = ".gweather.cfg" # create config file with your city list

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.combo = QComboBox(self)
        lines_list = open(cfg_file).read().splitlines()
        lines_list = list(filter(None, lines_list))

        for t in lines_list:
            self.combo.addItem(t)
        
        self.combo.resize(100, 30)
        self.combo.move(5, 40)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(5, 5)
        
        self.button = QPushButton('Add City',self)
        self.button.resize(200,30)
        self.button.move(110, 5)
        self.button.clicked.connect(self.on_add)
        
        self.button2 = QPushButton('Show',self)
        self.button2.resize(80, 30)
        self.button2.move(110, 40)
        self.button2.clicked.connect(self.on_show)
        
        self.button3 = QPushButton('Remove City',self)
        self.button3.resize(115, 30)
        self.button3.move(195, 40) 
        self.button3.clicked.connect(self.on_remove)      

        self.qlabel1 = QLabel('City',self)
        self.qlabel1.move(7,70)
        
        self.qlabel2 = QLabel('Condition',self)
        self.qlabel2.move(7,90)
        
        self.qlabel3 = QLabel('Temperature',self)
        self.qlabel3.move(7,110)
        
        self.qlabel4 = QLabel('Wind',self)
        self.qlabel4.move(7,130)
        
        self.qlabel5 = QLabel('Precipitation',self)
        self.qlabel5.move(7,150)
        
        self.qlabel6 = QLabel('Humidity',self)
        self.qlabel6.move(7,170)

        self.qlabel7 = QLabel('Updated',self)
        self.qlabel7.move(7,190)    
               
        self.qlabel8 = QLabel('',self)
        self.qlabel8.move(110,70)
        self.qlabel8.resize(225,28)
        self.qlabel9 = QLabel('',self)
        self.qlabel9.move(110,90)
        self.qlabel9.resize(225,28)
        self.qlabel10 = QLabel('',self)
        self.qlabel10.move(110,110)
        self.qlabel11 = QLabel('',self)
        self.qlabel11.move(110,130)
        self.qlabel12 = QLabel('',self)
        self.qlabel12.move(110,150)
        self.qlabel13 = QLabel('',self)
        self.qlabel13.move(110,170)
        self.qlabel14 = QLabel('',self)
        self.qlabel14.move(110,190)   
        self.qlabel14.resize(225,28)

        self.setGeometry(50,50,315,220)
        self.setWindowTitle("Google Weather")
        self.show()

    def on_show(self):

        combo_value = self.combo.currentText()    

        agent  = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.88"
        source = urllib.request.Request('https://www.google.com/search?q=weather+'+combo_value+'', headers={'User-Agent':agent})
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

        self.qlabel8.setText(' '+combo_value)
        self.qlabel9.setText(' '+condition)
        self.qlabel10.setText(' '+temperature+'°')
        self.qlabel11.setText(' '+wind)
        self.qlabel12.setText(' '+precipitation)
        self.qlabel13.setText(' '+humidity)
        self.qlabel14.setText(' '+updated)
        return
        
    def on_add(self):
        entry_value = self.textbox.text()
        f = open(cfg_file, 'a+') 
        f.write(entry_value+'\n')
        f.close()
        lines_list = open(cfg_file).read().splitlines()
        lines_list = list(filter(None, lines_list)) 
        self.combo.clear()
        self.textbox.setText("")
        
        for t in lines_list:            
            self.combo.addItem(t)
        return
        
    def on_remove(self):
        remove_item = self.combo.currentText()
        subprocess.call(['sed','-i','/.*'+remove_item+'.*/d',cfg_file])
        self.combo.clear()
        lines_list = open(cfg_file).read().splitlines()
        lines_list = list(filter(None, lines_list)) # fastest  
        
        for t in lines_list:            
            self.combo.addItem(t)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
