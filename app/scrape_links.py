import os
import random
import time

import requests,re, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import ray
#url = sys.argv[0]

lista = []

#argumentos

file = input('Type file name: ')
#file = 's.html'
user = input('Type @username: ')
#user = '@saude_da_mente'
try: stopped = sys.argv[3]
except: stopped = None

class Capta_tik():
    def extratch_link(self, user):
        if(os.path.exists(file)):
            pass

        else:
            return print(f'Arquivo {file} não encontrado na pasta, certifique-se de que o mesmo exista')


    def get_url(self): #retorna todos links
        arq = open(file, 'r')
        arquivo = arq.read()
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, arquivo)
        return [x[0] for x in url]




    def url_filter(self): #retorna urls filtradas
        urls = Capta_tik().get_url()
        url_destino = (f'https://www.tiktok.com/{user}/video/')

        with_s = [idx for idx in urls if idx.lower().startswith(url_destino.lower())]
        return with_s

    def save_(self, link_video):
        try:
            time.sleep(3)
            driver.find_element(By.ID, 'main_page_text').send_keys(link_video)
            time.sleep(2)
            driver.find_element(By.ID, 'main_page_text').send_keys(Keys.ENTER)
            time.sleep(4)
            try: driver.find_element(By.XPATH, '//a[@class="pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark vignette_active"]').click()
            except: pass

        except:
            time.sleep(5)
            pass




    def __main__(self):


        try:
            C = Capta_tik()
            C.extratch_link(user)
            print(f"""
Paramêtros escolhidos:
User: {user}
Arquivo: {file}
Onde parou: {stopped}


""")


        except IndexError:
            print("""Sintaxe correta:\npython3 main.py [@USERNAME] [FILE.html]
            Requisitos: Baixar arquivo .html
            Inserir nome de usuário
            
            """)


            quit()


    def parall(self):
        C = Capta_tik()
        z = C.url_filter()
        print(f"{len(z)} Vídeos do {sys.argv[0]} encontrados")
        print(z)

        #@ray.remote
        def process1(): #Deixa pré armado
            count = 0

            if stopped == None:
                for i, p in enumerate(z):
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[i]) #Número janela
                    driver.get('https://ssstik.io/pt')
                    C.save_(p)
                    print(f'[{i}]Link: {p} aberto')
                    count += 1

            else:
                print('Método stopped')
                for i, p in enumerate(z):
                    if p or i == stopped:
                        driver.execute_script("window.open('');")
                        driver.switch_to.window(driver.window_handles[i]) #Número janela
                        driver.get('https://ssstik.io/pt')
                        C.save_(p)
                        print(f'[{i}]Link: {p} aberto')
                        count += 1

                    else: pass






        process1()
        input('Pressione <ENTER> quando acabar')
        #process2()








#Capta_tik().__main__()
#driver = webdriver.Chrome(executable_path='/home/linuxlite/Spaumer/chromedriver')
Capta_tik().parall()





