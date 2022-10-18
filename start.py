"""
Main file, where the magic happen :)

All features will be acessible using start.py, if you pretend to create new features or files, you
need design the file to be compatible with start.py

"""

from app.scrape_links import Capta_tik 
from app.source_code import CODE
from app.downloader import DOWNLOAD as DW
from os.path import exists
from os.path import abspath

url_user = input('Digite o link do perfil do usuário incluindo o https://www: ex.:(https://www.tiktok.com/@seuusario): ')
user = ''

def process_data():
    global user, url_user
    #Separate user from link
    user = '@' + url_user.split('@')[1]
    if user.find('/') != -1:
        user = user.split('/')[0]

    if url_user.find('https://www.') == -1:
        url_user = 'https://www.' + url_user

process_data()
    



path_f = abspath('app') + '/chromedriver'

__author__ = open('app/data.config', 'r').read()

if __name__ == '__main__':

    if exists(path_f) ==False:
        DW().__main__()
       



    print("""
    {AUTHOR}

    Data to fetch...
    USERNAME: {USER} 
    URL: {URL} 

    """.format(
        AUTHOR = __author__,
        USER = user,
        URL = url_user
    ))


    raw_data = CODE(link=url_user, path_file=path_f).__main__() #Get the html code
    SCRAPE = Capta_tik(
        username=user,            #Return all tiktok links in a list format
        content_page=raw_data
    ).__main__()


    if len(SCRAPE) <=0: #Opppss
        print("""[ERROR] Ops... Podem ter acontecido três erros aqui:
            *O perfil tem 0 vídeos
            *O algoritmo do tiktok identificou que estamos usando uma automação
            *O programa falhou

            Nesse caso foi criado um arquivo chamado site.html na pasta app do qual você poderá\nabrir no seu navegador ou apenas cole esse link no seu browser, {PAGE}.

            Obs.: Caso não entenda o que aconteceu você pode abrir um issue através do github e eu poderei te ajudar :).

            Link para abrir issue: https://github.com/ORobsonJr/Telelytics/issues

         """)
    
    print(SCRAPE)
    



