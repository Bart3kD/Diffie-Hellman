class DH:
    def __init__(self):
        self.p = 200000033
        self.g = 200000022

    def getValues(self):
        return self.p,self.g
    
    def calcPublicSecret(self, secret):
        if secret > self.g:
            return False
        return pow(self.g, secret) % self.p
    def calcSharedSecret(self, privSecret, publicSecret):
        return pow(publicSecret, privSecret) % self.p

