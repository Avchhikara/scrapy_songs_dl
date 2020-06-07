"""
This is used to download the item and then save them in the location mentioned

"""

import os
import requests
# import urllib
import json

from tqdm import tqdm


class DownloadAndSave:
    def __init__(self, url, name):
        self.url = url
        self.name = self.get_name(url)
        self.location = "/home/avnish/Downloads/songs/"
        # print(self.name)
        # r = requests.get(self.url)
        self.__save()

    def __save(self):
        pass
        r = requests.get(self.url)
        # now, save the data
        # pirint(os.path.join(self.location, self.name))
        
        open(os.path.join(self.location, self.name), "wb").write(r.content)
    
    def get_name(self, url_str):
        arr = url_str.split("/")   
        name = arr.pop().replace(" ", "_")
        return name[0:-1] if not name.endswith('.mp3') else name


if __name__ == "__main__":
    # print(os.path.join)
    # first opening up the file
    f = open('out.json', 'r')
    data = json.loads(f.read())
    f.close()
    for song in tqdm(data):
        # print(song)
        d = DownloadAndSave(song['url'], song['text'])

    # d = DownloadAndSave('http://s320.ve.vc/data/320/48311/295717/Raat Gayi Baat Gayi - Happy Raikoti (DjPunjab.Com).mp3"', "test_is_great.mp3")
