#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 Lai Yao Hao <laiyaohao96@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from selenium import webdriver
from time import sleep
import random


class TempBot:
	def __init__(self,username,password):
		options = webdriver.ChromeOptions()
		options.add_argument("--disable-blink-features")
		options.add_argument("--disable-blink-features=AutomationControlled")
		self.driver = webdriver.Chrome(options=options)
		
		sleep(2)
		self.driver.get('https://myaces.nus.edu.sg/htd/htd')
		self.driver.find_element_by_xpath("//input[@name='UserName']").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name='Password']").send_keys(password)
		sleep(3)
		self.driver.find_element_by_id("submitButton").click()
		self.temp = str(round(random.uniform(35.8,36.9),1))
		sleep(5)
		
	
	def decl_temp(self):
		self.driver.find_element_by_xpath("//input[@name='symptomsFlag'][@value='N']").click()
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name='familySymptomsFlag'][@value='N']").click()
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name='temperature']").send_keys(self.temp)
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name='Save']").submit()
		sleep(5)
		self.driver.quit()

NUSnetID = input("Please enter your NUSNetID: ")
fullUser = "nusstu\\" + NUSnetID
password = input("And your password: ")
temp_bot = TempBot(fullUser,password)
temp_bot.decl_temp()
