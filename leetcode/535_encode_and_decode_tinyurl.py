class Codec:

    def __init__(self):
        self.cache = {}
        self.count = 0
        
    def encode(self, longUrl: str) -> str:
        self.cache[str(self.count)] = longUrl
        self.count+=1
        return "http://tinyurl.com/"+str(self.count-1)
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cache[shortUrl[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
