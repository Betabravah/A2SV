class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoded = []
        for char in longUrl:
            encoded.append(str(ord(char)))
            encoded.append(' ')
        
        return ''.join(encoded)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        encoded = shortUrl.split()
        decoded = []
        
        for order in encoded:
            decoded.append(chr(int(order)))
            
        return ''.join(decoded)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))