 #!/usr/bin/python2

# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time ,re 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Registro(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, command_executor='http://localhost:4444/wd/hub')



    def test_search_in_python_org(self):

        driver = self.driver

        driver.get("http://mobile.ar.bumeran.biz")
        self.assertIn("Empleos en Argentina", driver.title)
        driver.find_element_by_xpath("//*[@id='header-nologueado']/div/ul/li[4]/a").click()
        driver.find_element_by_xpath("//*[@id='nombre']").click()
        driver.find_element_by_xpath("//*[@id='nombre']").clear()
        driver.find_element_by_xpath("//*[@id='nombre']").send_keys("gonzalo")
        driver.find_element_by_id("apellido").click()
        usuario = driver.find_element_by_id("apellido")
        usuario.send_keys("bariandaran")
        driver.find_element_by_xpath("//*[@id='email']").click()
        driver.find_element_by_xpath("//*[@id='email']").clear()
        usuario = driver.find_element_by_xpath("//*[@id='email']")
        usuario.send_keys("g@navent.com")
        driver.find_element_by_css_selector("div.col-sm-6.form-group > #password").clear()
        driver.find_element_by_css_selector("div.col-sm-6.form-group > #password").send_keys("123456")
        driver.find_element_by_id("puesto").click()
        driver.find_element_by_id("puesto").clear()
        driver.find_element_by_id("puesto").send_keys("ingeniero")
        Select(driver.find_element_by_id("zona")).select_by_visible_text("Capital Federal")
        time.sleep(3)
        driver.find_element_by_id("registroButton").click()





    def tearDown(self):

        self.driver.close()


           
if __name__ == "__main__":

   unittest.main()
   
   