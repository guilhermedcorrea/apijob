from abc import ABC, abstractmethod
import lxml.html as parser
import requests
import csv
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from random import randint
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from itertools import chain


class MelhorEnvio:
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    #options.add_argument("--incognito")
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")
    #options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--no-sandbox')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options, executable_path=r'/home/debian/Documentos/apijob/app/chromedriver/chromedriver/chromedriver')
    
    def __init__(self):
        self.transportadoras = []
        self.modalidades = []
        self.prazos = []
        self.valor = []
    def scroll_page(self):

        lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True

 
    def index(self):
        """Recebe os valores vindos da query e repassa nos campos send_keys para a tela de cota frete"""
        self.driver.get("https://melhorenvio.com.br/?utm_source=google&utm_medium=cpm&utm_campaign=google&gclid=CjwKCAjwm8WZBhBUEiwA178UnEDYFZINOQsPTh90mAMwFPME2pJ-MjZjRTX-MWtB8y-_N6h-DUq3aBoC6hAQAvD_BwE")


    def limpar_campos(self):
        """Deleta os campos ja preenchidos"""
        self.scroll_page()
        self.driver.implicitly_wait(30)
 
        #self.driver.find_element(By.CSS_SELECTOR,'#height').send_keys(u'\ue009' + u'\ue003')

        #self.driver.find_element(By.CSS_SELECTOR,'#width').send_keys(u'\ue009' + u'\ue003')

        #self.driver.find_element(By.CSS_SELECTOR,'#length').send_keys(u'\ue009' + u'\ue003')
        
        #self.driver.find_element(By.CSS_SELECTOR,'#weight').send_keys(u'\ue009' + u'\ue003')
      
       
        self.driver.find_element(By.ID,'height').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.ID,'height').send_keys(Keys.DELETE)
    
        self.driver.find_element(By.ID,'width').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.ID,'width').send_keys(Keys.DELETE)

        self.driver.find_element(By.ID,'length').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.ID,'length').send_keys(Keys.DELETE)

        self.driver.find_element(By.ID,'weight').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.ID,'weight').send_keys(Keys.DELETE)

        self.driver.find_element(By.ID,'insuranceValue').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.ID,'insuranceValue').send_keys(Keys.DELETE)
        
        

    def cotar_frete(self,*ars, **kwargs):
        self.scroll_page()
        self.driver.implicitly_wait(30)
        valor = kwargs.get('valor')
        pesop = kwargs.get('peso')
        origem = kwargs.get('origem')
        destino = kwargs.get('destino')
        valorf =  kwargs.get('valor')
      
     
        comprimento = kwargs.get('comprimento')
    
        valor=  kwargs.get('valor')
        
        print(valor,pesop,origem,destino ,valorf,)
     
        time.sleep(1)
        cep_origem = self.driver.find_element(By.XPATH, '//*[@id="from"]')
        cep_origem.send_keys(origem)

     
        cep_destino = self.driver.find_element(By.XPATH, '//*[@id="to"]')
        cep_destino.send_keys(destino)

    
        time.sleep(1)
        altura = self.driver.find_element(By.CSS_SELECTOR,'#height')
        
        altura.send_keys(altura)

        
        largura = self.driver.find_element(By.XPATH,'#width')
        largura.send_keys(comprimento)
        time.sleep(1)
        
        comprimento = self.driver.find_element(By.XPATH,'#length')
        comprimento.send_keys(10)

        
        peso = self.driver.find_element(By.XPATH,'#weight')
        peso.send_keys(pesop)

        
        valor = self.driver.find_element(By.XPATH,'//*[@id="insuranceValue"]')
        valor.send_keys(valorf)

 

        confirma_busca = self.driver.find_element(By.XPATH, '//*[@id="calculate"]').click()
     
        
    def get_valores(self):
        time.sleep(1)
        self.scroll_page()
        self.driver.implicitly_wait(30)

        self.scroll_page()
        transportadoras = self.driver.find_elements(By.XPATH, '//*[@id="calculator"]/div/div[1]/div[1]/table/tr/td[1]/img')
        for transportadora in transportadoras:
         
            self.transportadoras.append(transportadora.get_attribute('alt'))

        modalidades = self.driver.find_elements(By.XPATH, '//*[@id="calculator"]/div/div[1]/div[1]/table/tr/td[2]')
        for modalidade in modalidades:
          
            self.modalidades.append(modalidade.text)
 
        prazos = self.driver.find_elements(By.XPATH, '//*[@id="calculator"]/div/div[1]/div[1]/table/tr[2]/td/div/span[1]')
        for prazo in prazos:
          
            self.prazos.append(prazo.text)

        valores = self.driver.find_elements(By.XPATH, '//*[@id="calculator"]/div/div[1]/div[1]/table/tr/td[5]/p')
        for valor in valores:
            preco = valor.text.replace("R$","").replace("*","").replace(".","").replace(",",".").strip()
        
            self.valor.append(preco)
    

    def retorna_dicts(self):
        time.sleeep(4)
        lista_dicts = []
        for i in range(len(self.transportadoras)):
            dict_fretes = {}

            try:
                dict_fretes['TRANSPORTADORA'] = self.transportadoras[i]
            except:
                dict_fretes['TRANSPORTADORA'] = 'nao atendida'
            
            try:
                dict_fretes['MODALIDADE'] = self.modalidades[i]
            except:
                dict_fretes['MODALIDADE'] = 'nao atendida'
            
            try:
                dict_fretes['PRAZO'] = self.prazos[i]
            except:
                dict_fretes['PRAZO'] = 'nao atendida'
            
            try:
                dict_fretes['VALOR'] = self.valor[i]
            except:
                dict_fretes['VALOR'] = 'nao atendida'

            #lista_dicts.append(dict_fretes)
            yield dict_fretes
        self.driver.quit()
     
        









    
