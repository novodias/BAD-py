from animesfolder import animepath
from pyquery import PyQuery
from anime import Anime

class extractor:
    
    def getanimeinfo(animeurl):
        pq = PyQuery(animeurl)
        animename = pq('#page-content > main > div.infos_left > div > h2').text()
        animelength = pq('#page-content > main > div.infos_left > div > p:nth-child(8) > span').text()
        language = pq('#page-content > main > div.infos_left > div > p:nth-child(11)').text()
        quality = pq('#page-content > main > div.infos_left > div > p:nth-child(3) > span:nth-child(2)').text()
        genresweb = pq('#page-content > main > div.infos_left > div > div.anime-genres')
        
        genres = []
        for g in genresweb.children():
            genres.append(PyQuery(g).text)
        
        episodes = []
        links = {}
        episodesweb = pq('#episodesList')
        episodesweb.children().remove_class('list-group-item')
        for e in episodesweb.children():
            url = PyQuery(e).children().attr('href')
            if ( url != None ):
                # print(str(extractor.getkeyepisode(url)) + ": " + url)
                key = extractor.getkeyepisode(url)
                links[key] = url + "/download"
                episodes.append(key)
        
        print("Anime: " + animename)
        print("Episódios: " + animelength)
        print(language)
        print("Qualidade: " + quality)
        
        animeexists = animepath.folderexists( animename )
    
        if (animeexists == True):
            files = animepath.getfilesfolder( animename )
            for f in files:
                num = extractor.getkeyepisode( f )
                episodes.pop( episodes.index(num) )
                links.pop( num )
                
        startcount = extractor.getstartcount( episodes )
        quality = extractor.getquality()
                
        return Anime( animename, links, episodes, animeurl, startcount, quality )

    def getkeyepisode(url):
        one = url.rfind('-') + 1
        numbers = ""
        for i in range( 0, 3 ):
            try:
                numbers += url[one + i]
                # print(numbers)
            except IndexError:
                break
        return int(numbers)
    
    def getstartcount(episodes):
        print("Deseja começar de qual episódio? " + str(episodes[0]) + " á " + str(episodes[-1]))
        try:
            startcount = int(input())
            
            if ( startcount < episodes[0] ): 
                print("Selecionado o primeiro episódio.")
                startcount = episodes[0]
            if ( startcount > episodes[-1] ):
                print("Selecionado o último episódio.")
                startcount = episodes[-1]
                
            return startcount
        except:
            print( "Não é um número válido!" )
            return extractor.getstartcount(episodes) 
        
    def getquality():
        print( "Selecione a qualidade de vídeo: \n1. [SD]\n2. [HD]\n3. [FULL HD]" )
        select = input()
        
        sd = '#page-content > div.container.my-5 > section > div.contact-content.d-flex.justify-content-between.py-4.px-5 > div:nth-child(1) > div > a.btn.btn-primary.mb-2'
        hd = '#page-content > div.container.my-5 > section > div.contact-content.d-flex.justify-content-between.py-4.px-5 > div:nth-child(1) > div > a.btn.btn-secondary.mb-2'
        fullhd = '#page-content > div.container.my-5 > section > div.contact-content.d-flex.justify-content-between.py-4.px-5 > div:nth-child(1) > div > a.btn.btn-danger.mb-2'
        
        if ( select == '1' ):
            return sd
        elif ( select == '2' ):
            return hd
        elif ( select == '3' ):
            return fullhd
        else:
            print( "Número não incluído nas opções, selecionado o SD." )
            return sd