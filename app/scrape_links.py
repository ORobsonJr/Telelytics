"""
This file is where we'll scrape all links from html code that will be provided using another file.


"""

from re import findall


class Capta_tik():
    def __init__(self, username: str, content_page):
        self.user = username
        self.content = content_page #Html code of tiktok account


    def __main__(self): #Return all files 
        """
        Return all urls in list format
        """
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = findall(regex, self.content)
        raw_urls =  [x[0] for x in url] #Return a list with all url scraped
        dest_url = f'https://www.tiktok.com/{self.user}/video/'
        with_s = [idx for idx in raw_urls if idx.startswith(dest_url)]
                
        return with_s #Return just tiktok videos





        




    

    











