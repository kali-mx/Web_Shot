
from selenium import webdriver
from time import sleep
import os,sys

# Author: Max Ahartz
# Created: 11-13-22
# Inspired by: Ebram Rezk

url = input ('Enter target IP. Example:http://10.10.185.20 -->')

gobust = "gobuster dir -u " + url + " -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt -k -t 30 -o dirnames.txt"
os.system(gobust)
os.system("grep ': 200' dirnames.txt | cut -d ' ' -f 1 | cut -d '/' -f 2 > names.txt")

driver = webdriver.Firefox()

with open('names.txt', 'r') as f:
    for name in f:
        uri = url + "/" + name
        print(uri)
        driver.get(uri)
        sleep(1)

        picture = "screenshot_" + name.replace("\n", "") + ".png"
        print(picture)
        driver.get_screenshot_as_file(picture)
f.close()        
driver.quit()

os.system("ristretto screenshot_*") #show me the pics!
quit()
