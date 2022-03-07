import os, re

class animepath:
    
    folder = "Animes/"
    
    def animesfolder():
        if (os.path.isdir(animepath.folder) == False):
            os.mkdir(animepath.folder)

    @staticmethod
    def folderexists(animename):
        animepath.animesfolder()
        
        animename = re.sub(r'[^\w\-_\. ]', '', animename)
        
        anime = animepath.folder + animename
        
        if (os.path.isdir(anime) == False):
            animepath.createdir(animename)
            return False
        
        if (os.listdir(anime) == []):
            return False
        
        return True
    
    @staticmethod
    def getfilesfolder(animename):
        animename = re.sub(r'[^\w\-_\. ]', '', animename)
        
        anime = animepath.folder + animename
        
        return os.listdir(anime)
    
    @staticmethod
    def createdir(animename):
        animepath.animesfolder()

        animename = re.sub(r'[^\w\-_\. ]', '', animename)
        
        dir = animepath.folder + animename
        
        os.mkdir(dir)
    
    @staticmethod
    def getdir(animename):
        animepath.animesfolder()

        animename = re.sub(r'[^\w\-_\. ]', '', animename)
        
        dir = animepath.folder + animename + '/'
        return dir
