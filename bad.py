from animeinfo import extractor
from downloadmanager import downloadmanager

def main():
    print('BADownloader')
    
    url = geturl()
    
    anime = extractor.getanimeinfo(url)
    anime.writeDebug()
    
    manager = downloadmanager(1, anime)
    
    print("Começando download:")
    manager.getdownloadlinks()
    
def geturl():
    print('Insira a url do anime: ')
    url = input()

    if (url.startswith("https://betteranime.net") == False):
        return geturl()
        
    return url

main()