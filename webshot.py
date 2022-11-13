# Author: Max Ahartz
# Created: 11-13-22
# Inspired by: Ebram Rezk

from selenium import webdriver
from time import sleep
import os,sys

url = input ('Enter target IP.\nExample:http://10.10.185.20 -->')
word_list = "/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt"
gobust = "gobuster dir -u " + url + " -w " + word_list + " -k -t 100 -o dirnames.txt"
os.system(gobust)
os.system("grep ': 200' dirnames.txt | cut -d ' ' -f 1 | cut -d '/' -f 2 > names.txt")

driver = webdriver.Firefox()

with open('names.txt', 'r') as file:
    for name in file:
        uri = url + "/" + name
        print(uri)
        driver.get(uri)
        sleep(1)

        picture = "screenshot_" + name.replace("\n", "") + ".png"
        print(picture)
        driver.get_screenshot_as_file(picture)
file.close()        
driver.quit()

os.system("ristretto screenshot_*") #show me the pics!
