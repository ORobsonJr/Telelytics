"""
This will automate the process of install chromedriver and move to path.

"""

from requests import get
import subprocess
from sys import platform
from os import system

class DOWNLOAD():
    def __init__(self):
        pass

    def get_chrome_version(self):
        #Discover chrome version and return it

        if platform == 'linux': #If system is linux...
            path = '/usr/bin/google-chrome'
            with subprocess.Popen([path, '--version'], stdout=subprocess.PIPE) as proc:
                version = proc.stdout.read().decode('utf-8').replace('Chromium', '').replace('Google Chrome', '').strip()
        
        elif platform == 'mac': #If system is mac...
            process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
            
            version = process.communicate()[0].decode('UTF-8').replace('Google Chrome', '').strip()
        elif platform == 'win':
            process = subprocess.Popen(
                ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
            )
            output = process.communicate()
            if output and output[0] and len(output[0]) > 0:
                version = output[0].decode('UTF-8').strip().split()[-1]
            else:
                process = subprocess.Popen(
                    ['powershell', '-command', '$(Get-ItemProperty -Path Registry::HKEY_CURRENT_USER\\Software\\Google\\chrome\\BLBeacon).version'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
                )
                version = process.communicate()[0].decode('UTF-8').strip()
        

        return version

    def __main__(self):
        print("""
        Faça download do chromedriver versão {VERSION} no sistema operadional {SO}. Clique no link abaixo e selecione a versão mais próxima da sua versão.
        https://chromedriver.storage.googleapis.com/index.html?

        Após ter feito o downloado no link acima com a versão mais próxima da sua, cole a localização dele por extenso abaixo.
        
        """.format(
            VERSION=DOWNLOAD().get_chrome_version(),
            SO=platform
            ))

        #Let's move the chrome driver to app file
        xpath = input("Cole o diretório aqui: ")

    
        system(f'mv {xpath} ./app') #Move file 
        quit()
        


