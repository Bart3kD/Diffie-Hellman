p = 200000000309
g = 200000000235

def calcPublicSecret( secret):
    if secret > g:
        return False
    return pow(g, secret) % p
def calcSharedSecret( privSecret, publicSecret):
    return pow(publicSecret, privSecret) % p

secret = calcPublicSecret(10)

print(f"PublicSecret {secret}")
print(f"Shared {calcSharedSecret(12, secret)}")