
from requests import get 
from selenium import webdriver
from selenium.webdriver import ChromeOptions

class CODE():
    def __init__(self, link, path_file):
        self.url = link #Html code of tiktok account
        self.file_p = path_file #Path where driver is stored

    def __main__(self):
        """
        We'll need use selenium to get the source code, because tiktok identify
        that we're using a automation data and will ask a re-captcha test
        """

        options_ = ChromeOptions()
        try: options_.headless = True
        except: options_.add_argument("--headless") #Problem with version
        driver = webdriver.Chrome(executable_path=self.file_p, options=options_)
        driver.get(self.url) #Opening profile url
        return driver.page_source

        
       
    
        
