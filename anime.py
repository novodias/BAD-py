class Anime:
    
    def __init__(self, name, links: dict, episodes: list, url, startcount, quality):
        self.name = name
        self.links = links
        self.episodes = episodes
        self.lastepisode = episodes[-1]
        self.url = url
        self.startcount = startcount
        self.index = list.index(self.episodes, self.startcount)
        self.quality = quality
        
    def writeDebug(self):
        print("Anime: %s" % self.name)
        for i in self.links:
            print(self.links[i])
        print("Last Episode: " + str(self.lastepisode))
        print("URL: " + self.url)
        print("Startcount: " + str(self.startcount))
        print("Index: " + str(self.index))
        print("Quality: " + self.quality)