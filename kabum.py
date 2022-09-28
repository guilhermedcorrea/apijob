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
from datetime import datetime
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from datetime import datetime
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + '/home/debian/Documentos/apijob/kabumdbapi.db'
            
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class MarcaProduto(db.Model):

    __tablename__ = 'marcaproduto'
    idmarca = db.Column(db.Integer,  primary_key = True)
    marca = db.Column(db.String(100))
    bitativo = db.Column(db.Boolean, nullable=True)
    datacadastro = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    bitativo = db.Column(db.Boolean)
 
    

    def __repr__(self):
        return  f'<Marca>"{self.marca}"'


class Produtos(db.Model):
    """
    Armazena Informações referentes aos produtos usados no calculo do frete
    Recebe chave estrangeira da tabea marca
    """
    __tablename__ = 'produto'
    idproduto = db.Column(db.Integer, primary_key = True)
    skuproduto = db.Column(db.String(300),unique=False , nullable=True)
    nomeproduto =db.Column(db.String(1000),unique=False , nullable=True)
    idmarca = db.Column(db.Integer, db.ForeignKey('marcaproduto.idmarca'))
    urlpaginaproduto = db.Column(db.String(2000),unique=False , nullable=True)
    peso = db.Column(db.Float,unique=False , nullable=True)
    altura = db.Column(db.Float,unique=False , nullable=True)
    largura = db.Column(db.Float,unique=False , nullable=True)
    comprimento = db.Column(db.Float,unique=False , nullable=True)
    bitativo = db.Column(db.Boolean,unique=False ,nullable=True)
    dataalterado = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
   
    def __repr__(self):
        return  f'<SKU>"{self.idproduto}"'


class WebDriver(ABC):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")
    #options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--no-sandbox')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options, executable_path=r'/home/debian/Documentos/apijob/app/chromedriver/chromedriver/chromedriver')
   
    @abstractmethod
    def get_urls_produtos(self, *args, **kwargs):pass
    

class Kabum(WebDriver):
    def __init__(self):
        self.lista_dicts = {}
        self.lista_urls = []
        self.data = str(datetime.today().strftime('%Y-%m-%d %H:%M'))

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
        self.driver.get("https://www.kabum.com.br")

    def get_urls_produtos(self, *args):
        if isinstance(args,tuple):
      
            for arg in args:
                self.driver.get(arg)
                time.sleep(10)

                self.driver.implicitly_wait(15)
        
                time.sleep(4)
                self.scroll_page()
                urls_produtos = self.driver.find_elements(By.XPATH, '//*[@id="listing"]/div[3]/div/div[2]/div/main/div/a')
                for urls in urls_produtos:
                    self.lista_urls.append(urls.get_attribute("href"))
            
              
    def get_produtos(self):
        #for produtos in self.lista_urls:
        listas = ["https://www.kabum.com.br/produto/219453/smartphone-motorola-moto-edge-20-pro-256gb-5g-12gb-ram-octa-core-108mp-tela-6-7-capa-protetora-branco-xt2153-1","https://www.kabum.com.br/produto/305781/smartphone-samsung-galaxy-s22-8gb-ram-128gb-camera-tripla-50mp-tela-6-1-preto-sm-s901ezkrzto","https://www.kabum.com.br/produto/306106/tablet-lenovo-tab-p11-plus-64gb-wifi-tela-11-android-11-grafite-za940394br","https://www.kabum.com.br/produto/189710/soundbar-tcl-2-1-canais-bluetooth-320w-rms-subwoofer-sem-fio-preto-ts7010","https://www.kabum.com.br/produto/201431/receiver-av-smart-onkyo-7-2-canais-8k-dolby-atmos-dts-virtual-x-tx-nr5100","https://www.kabum.com.br/produto/112807/projetor-lg-cinebeam-smart-tv-140-uhd-4k-hdr10-1500-ansi-lumens-hdmi-usb-bluetooth-wi-fi-branco-hu70la","https://www.kabum.com.br/produto/206623/smartwatch-samsung-galaxy-watch4-bluetooth-40mm-preto-sm-r860nzkpzto","https://www.kabum.com.br/produto/148877/fone-de-ouvido-samsung-galaxy-buds-pro-cancelamento-de-ruido-violeta-sm-r190nzvpztohttps://www.kabum.com.br/produto/306107/tablet-lenovo-tab-p11-plus-64gb-4g-wifi-tela-11-android-11-grafite-za9l0313br","https://www.kabum.com.br/produto/147827/caixa-de-som-jbl-partybox-on-the-go-100w-rms-portatil-bluetooth-microfone-sem-fio-jblpartyboxgobbr2https://www.kabum.com.br/produto/285560/iphone-12-64gb-verde-5g-6-1-12mp-mgj93br-a","https://www.kabum.com.br/produto/154979/samsung-smart-tv-70-uhd-4k-70au7700-processador-crystal-4k-tela-sem-limites-visual-livre-de-cabos-alexa-built-in-un70au7700gx"]
        for lista in listas:
            self.driver.get(lista)

            dict_items = {}

            self.driver.implicitly_wait(15)
            try:
                dict_items['PAGINA_PRODUTO'] = lista
          
            except IndexError as e:
                error = "NotFound"
            
            dict_items['BIT'] = 1

            dict_items['DATAATUAL'] = self.data

            try:
                nome_item = self.driver.find_elements(By.XPATH, '//*[@id="__next"]/main/article/section/div[3]/div[1]/div/h1')[0].text
                dict_items['NOMEPRODUTO'] = nome_item
                
            except IndexError as e:
                error = "NotFound"
            try:
                referencia = self.driver.find_elements(By.XPATH, '//*[@id="__next"]/main/article/section/div[1]/div/div/span[2]')[0].text
                referencia = str(referencia).split(":")[-1]
              
                dict_items['REFERENCIA'] = referencia
            except IndexError as e:
                error = "NotFound"

            try:
                marca = self.driver.find_elements(By.XPATH, '//*[@id="productImage"]')[0]
                marca_p = marca.get_attribute('alt')
            
                dict_items['MARCA'] = marca_p
            except IndexError as e:
                error = "NotFound"

            try:
                precos = self.driver.find_elements(By.XPATH,'//*[@id="blocoValores"]/div[2]/div/h4')[0].text
                dict_items['PRECOS'] = precos
               
            except IndexError as e:
                error = "NotFound"


            yield dict_items

    @staticmethod
    def insert_marca_produto(*args, **kwargs):
        with db.engine.connect() as conn:
          
            marcas = MarcaProduto(marca = kwargs.get('marca'), bitativo = kwargs.get('bit')
            , datacadastro = kwargs.get('data'))
            db.session.add(marcas)
            db.session.commit()

 

kabum = Kabum()
kabum.index()

kabum.get_urls_produtos('https://www.kabum.com.br/promocao/MENU_ELETRONICOS')
dict_produtos = kabum.get_produtos()
for produto in dict_produtos:
    marca = str(produto.get(produto['MARCA']))
    #print(produto.get('MARCA'), produto.get('DATAATUAL'))

    with db.engine.connect() as conn:
        
        prod = Produtos(nomeproduto=produto['NOMEPRODUTO'] ,skuproduto = produto['REFERENCIA'],
                 urlpaginaproduto = produto['PAGINA_PRODUTO'] ,bitativo= 1)
       
        db.session.add(prod)
        db.session.commit()
        
 


