
from __future__ import unicode_literals
from __future__ import print_function
from os.path import abspath, join, dirname
import random
import webbrowser
import asyncio
import re
from selenium import webdriver
import string
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains


async def main():
    print('Hello ...')
    await asyncio.sleep(2)
    print('... World!')
    
async def main2():
    print('Hello ...')
    await asyncio.sleep(20)
    print('... World!')

full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())



web = webdriver.Chrome()
url = "https://www.footlocker.com/account/create"
web.get(url)

asyncio.run(main())

destination = open('dashe1.json', 'w')





names_file = open('emails.txt', 'r')
name_read = names_file.readlines()
1


n = 0 

m = 1

     
        
for x in range(m):
    firstname = "Vinit"
    fn = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/div[4]/input")
    for char in firstname:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       fn.send_keys(char)
       
    lastname = "Shah"
    ln = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/div[5]/input")
    for char in lastname:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       ln.send_keys(char)
       
    day = str(random.randint(10,12))
    date = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/fieldset/div[2]/div[1]/input")
    for char in day:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       date.send_keys(char)
       
    month = str(random.randint(10,30))
    mon = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/fieldset/div[2]/div[3]/input")
    for char in month:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       mon.send_keys(char)
       
       
    year = str(random.randint(1980,2003))
    yea = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/fieldset/div[2]/div[5]/input")
    for char in year:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       yea.send_keys(char)
       
    zipcode = "07047"
    zc = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/div[6]/input")
    for char in zipcode:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       zc.send_keys(char)
       
    email = name_read
    mail = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/div[8]/input")
    for char in email:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       mail.send_keys(char)
       
    pass_length = random.randint(15, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    pw = "".join(random.choice(characters) for i in range(pass_length))
    passw = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/div[9]/div[1]/input")
    for char in pw:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       passw.send_keys(char)
       
    phone = "551"+str(random.randint(100000,999999))+str(random.randint(1,9))
    pho = web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/div[10]/input")
    for char in phone:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       pho.send_keys(char)
       
    web.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div/section/div/form/div[11]/button").click()
    
    print(email)
    print(pw)


names_file.close()
    



