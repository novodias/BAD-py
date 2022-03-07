import re
import requests
import json
from pyquery import PyQuery
from anime import Anime
from animesfolder import animepath

class downloadmanager:
    def __init__( self, amount, anime: Anime ):
        self.taskdownload = amount
        self.urlsdownload = {}
        self.urlsfailed = {}
        self.anime = anime
        
    def getdownloadlinks(self):      
        for index in range( self.anime.index, len(self.anime.episodes) ):
            print('Baixando episódio: [' + str(self.anime.episodes[index]) + '/' + str(self.anime.episodes[-1]) + ']')
            self.urlsdownload[self.anime.episodes[index]] = downloadmanager.getresponseurl( self, index )
            downloadmanager.downloadfile(self, self.urlsdownload[self.anime.episodes[index]], self.anime.episodes[index])
        
    def getresponseurl(self, index):
        downloadlink = self.anime.links[self.anime.episodes[index]]
        pq = PyQuery(downloadlink)

        downloadlink = pq(self.anime.quality).attr('href')

        response = requests.get(downloadlink)
        pq = PyQuery(response.content)
        nextdata = json.loads(pq('#__NEXT_DATA__').text())

        countlink = len('https://download.betteranime.net/')
        datalink = downloadlink[countlink:len(downloadlink)]
        path = "/_next/data/" + nextdata["buildId"] + "/" + datalink + ".json"

        url = 'https://download.betteranime.net' + path

        header = {
            "authority": "download.betteranime.net",
            "method": "GET",
            "path": path,
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
            "referer": downloadlink,
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Linux",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
        }

        r = requests.get(url, headers=header)
        responsejson = r.json()
        return responsejson['pageProps']['anime']['path']

    def downloadfile(self, downloadlink: str, num):
        name = re.sub(r'[^\w\-_\. ]', '', self.anime.name)
        local_filename = animepath.getdir(name) + name + "-" + str(num)
        
        r = requests.get(downloadlink, stream=True)
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)