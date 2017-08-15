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


class PythonOrgSearch(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, command_executor='http://localhost:4444/wd/hub')
        


    def test_search_in_python_org(self):

        driver = self.driver
        driver.get("http://mobile.ar.bumeran.biz")
        self.assertIn("Empleos en Argentina", driver.title)
        driver.find_element_by_link_text("INGRESAR").click()     #hace click en ingresar
        driver.find_element_by_id("username").click()            #hace click en nombre de usuario
        usuario = driver.find_element_by_id("username").clear()  #limpia el campo nombre de usuario
        usuario = driver.find_element_by_id("username")          # guarda en la variable usuario el campo nombre de usuario para desp ingresar los datos
        usuario.send_keys("gba@.com")                            # se envian los datos al campo nombre
        driver.find_element_by_id("password").click()            # hace click en el campo password 
        usuario = driver.find_element_by_id("password").clear()  # limpia el campo password
        usuario = driver.find_element_by_id("password")          # guarda en la variable usuario el campo password para desp ingresar los datos
        usuario.send_keys("")                                    # envia los datos al campo password
        driver.find_element_by_id("loginButton").click()         # hace click en el boton login
        time.sleep(5)                                            
        driver.get("http://mobile.ar.bumeran.biz/candidatos/curriculum")
                   

                   # CARGA DE DATOS PERSONALES
        driver.find_element_by_id("cv-edit-btn").click()          # hace click para desplegar campos del cv
        time.sleep(3)       
        driver.find_element_by_id("nombre").clear()               # limpia el campo nombre
        usuario = driver.find_element_by_id("nombre")             # guarda en la variable usuario el campo nombre para desp ingresar los datos
        usuario.send_keys("gonzalo")                              # envia los datos a nombre
        driver.find_element_by_id("apellido").clear()             # limpia el campo apellido
        usuario = driver.find_element_by_id("apellido")           # guarda en la variable usuario el campo apellido para desp ingresar los datos
        usuario.send_keys("bariandaran")                          # envia los datos al campo apellido
        driver.find_element_by_id("fechaNacimiento").clear()      # limpia el campo fecha de nacimiento
        usuario = driver.find_element_by_id("fechaNacimiento")    # guarda en la variable usuarios el campo fecha de nacimiento 
        usuario.send_keys("1991-03-13")                           # ingresa la fecha
        usuario = driver.find_element_by_css_selector("span.circle").click()                #hace click en el elemento masculino
        Select(driver.find_element_by_id("estadoCivil")).select_by_visible_text("Soltero/a") # despliega la ventana estado civil y selecciona soltero
        Select(driver.find_element_by_id("tipoDocumento")).select_by_visible_text("D.N.I.")  # despliega la ventana tipo de doc y selecciona D.N.I
        usuario = driver.find_element_by_id("nroDocumento").clear()                          # limpia el campo dni
        usuario = driver.find_element_by_id("nroDocumento")                                  # guarda en la variable usuario el campo nro documento para desp ingresar los datos
        usuario.send_keys("35863498")                                                        # envia la clave a nro de documento    
        time.sleep(4)                                                          # espera 4 segundos
        driver.find_element_by_id("guardarDatosPersonales").click()            #guarda los cambios


                       #PREFERENCIA, SALARIO LABORAL
        driver.get("http://mobile.ar.bumeran.biz/candidatos/curriculum")
        driver.find_element_by_xpath("//*[@id='preferencia-salarial']/div[2]/span").click()
        driver.find_element_by_xpath("//*[@id='salario']").click()
        driver.find_element_by_xpath("//*[@id='salario']").clear()
        usuario = driver.find_element_by_xpath("//*[@id='salario']")
        usuario.send_keys("1.000")  
        driver.find_element_by_id("salarioButton").click()

                           #EXPERIENCIA LABORAL
        driver.get("http://mobile.ar.bumeran.biz/candidatos/curriculum")
        driver.find_element_by_id("empresa").click()
        driver.find_element_by_id("empresa").clear()
        usuario = driver.find_element_by_id("empresa")
        usuario.send_keys("navent")
        Select(driver.find_element_by_id("industria")).select_by_visible_text("Internet")
        driver.find_element_by_id("puesto").click()
        driver.find_element_by_id("puesto").clear()
        usuario = driver.find_element_by_id("puesto")
        usuario.send_keys("ingeniero")
        Select(driver.find_element_by_id("nivelExperiencia")).select_by_visible_text("Junior")
        Select(driver.find_element_by_id("paisExperiencia")).select_by_visible_text("Argentina")
        driver.find_element_by_id("fechaInicio").clear()
        driver.find_element_by_id("fechaInicio").click()
        usuario = driver.find_element_by_id("fechaInicio")
        usuario.send_keys("2016-01-01") 
        driver.find_element_by_id("fechaFin").click()
        driver.find_element_by_id("fechaFin").clear()
        usuario = driver.find_element_by_id("fechaFin")
        usuario.send_keys("2017-07-01")
        driver.find_element_by_id("area").click()
        Select(driver.find_element_by_id("area")).select_by_visible_text("Legales")
        time.sleep(3)
        Select(driver.find_element_by_id("subarea")).select_by_visible_text("Legal")
        time.sleep(3)
        driver.find_element_by_id("btn-guardar-experiencia").click()

                                
                             #ESTUDIOS
        driver.get("http://mobile.ar.bumeran.biz/candidatos/curriculum")
        time.sleep(3)
        Select(driver.find_element_by_id("paisEducacion")).select_by_visible_text("Argentina")
        Select(driver.find_element_by_id("tipoEstudio")).select_by_visible_text("Universitario")
        Select(driver.find_element_by_id("estadoEstudio")).select_by_visible_text("En Curso")
        driver.find_element_by_id("titulo").click()
        driver.find_element_by_id("titulo").clear()
        usuario = driver.find_element_by_id("titulo")
        usuario.send_keys("ingenieria en sistemas de informacion")
        driver.find_element_by_xpath("//*[@id='310']").click()      
        driver.find_element_by_id("fechaInicioEstudio").click()
        usuario= driver.find_element_by_id("fechaInicioEstudio")
        usuario.send_keys("2014-03-01")
        driver.find_element_by_id("fechaFinEstudio").click()
        usuario = driver.find_element_by_id("fechaFinEstudio")
        driver.find_element_by_id("al-presente-estudio").click()  
        driver.find_element_by_id("institucionTypeAhead").click()   
        driver.find_element_by_id("institucionTypeAhead").clear()
        driver.find_element_by_xpath("//*[@id='educacion']/div[1]/div/form/div[5]/div[1]/span/div/div[2]/div[1]").click()
        time.sleep(2)
        Select(driver.find_element_by_id("rango")).select_by_visible_text("desde 1 hasta 10")
        driver.find_element_by_id("promedio").click()
        driver.find_element_by_id("promedio").clear()
        usuario = driver.find_element_by_id("promedio")
        usuario.send_keys("6")
        driver.find_element_by_id("registrarEducacion").click()
        time.sleep(3)


                               #OBJETIVO LABORAL
        
        driver.find_element_by_xpath("//div[@id='objetivo_container']/div[2]/span").click()
        driver.find_element_by_id("objetivo").clear()
        usuario = driver.find_element_by_id("objetivo")
        usuario.send_keys("Formar parte de un equipo de trabajo y consolidarme profesionalmente en una empresa donde los logros personales y el desempeno sean reconocidos, ademas de permitir oportunidades de desarrollo personal y profesional")
        driver.find_element_by_id("objetivoButton").click()
        time.sleep(3)

                              
                             #IDIOMA
        Select(driver.find_element_by_id("idioma")).select_by_visible_text("Italiano")
        Select(driver.find_element_by_id("nivelOral")).select_by_visible_text("Intermedio")
        Select(driver.find_element_by_id("nivelEscrito")).select_by_visible_text("Intermedio")
        driver.find_element_by_id("guardarIdioma").click()
         
                                 #CONOCIMIENTO TECNICOS
        driver.get("http://mobile.ar.bumeran.biz/candidatos/curriculum")
        Select(driver.find_element_by_id("tipoId")).select_by_visible_text("Bases de Datos")
        time.sleep(3)
        Select(driver.find_element_by_id("conocimientoEspecifico")).select_by_visible_text("MySQL")
        Select(driver.find_element_by_id("nivelCalificador")).select_by_visible_text("Intermedio")
        driver.find_element_by_xpath("//*[@id='informatica']/div[1]/div/form/a[1]").click()


                                   #REFERENCIAS

        driver.get("http://mobile.ar.bumeran.biz/candidatos/curriculum")
        driver.find_element_by_xpath("(//a[contains(text(),'CANCELAR')])[10]").click()





    #def tearDown(self):

    #self.driver.close()


           
if __name__ == "__main__":

   unittest.main()
   
   
   