class DH:
    def __init__(self):
        self.p = 23
        self.g = 9
    
    def calcPublicSecret(self, secret):
        return pow(self.g, secret) % self.p
    def calcSharedSecret(self, privSecret, publicSecret):
        return pow(publicSecret, privSecret) % self.p